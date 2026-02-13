#!/usr/bin/env python3
"""
OpenAIX 每小时自动评测脚本 v2.0
- 每小时评测5个网站
- 全局去重，不重复评测
- 优化目录结构：按日期分目录
- 更新 README 并推送到 GitHub
"""

import os
import sys
import json
import random
import subprocess
from datetime import datetime
from pathlib import Path

# 配置
PROJECT_DIR = Path("/home/wesley/.openclaw/workspace/openaix-core")
DATA_DIR = PROJECT_DIR / "data" / "evaluations"
URLS_FILE = PROJECT_DIR / "websites.txt"
BENCHMARK_SCRIPT = PROJECT_DIR / "benchmark.py"
VENV_PYTHON = PROJECT_DIR / "venv" / "bin" / "python3"
EVALUATED_LOG = DATA_DIR / "evaluated_sites.json"
BATCH_SIZE = 5  # 每小时评测数量

# 确保目录存在
DATA_DIR.mkdir(parents=True, exist_ok=True)

# 默认网站列表
DEFAULT_WEBSITES = [
    "https://openai.com",
    "https://anthropic.com",
    "https://claude.ai",
    "https://gemini.google.com",
    "https://docs.python.org",
    "https://github.com",
    "https://stackoverflow.com",
    "https://medium.com",
    "https://apple.com",
    "https://google.com",
    "https://microsoft.com",
    "https://amazon.com",
    "https://shopify.com",
    "https://notion.so",
    "https://figma.com",
    "https://vercel.com",
    "https://nextjs.org",
    "https://react.dev",
    "https://vuejs.org",
    "https://tailwindcss.com",
    "https://stripe.com",
    "https://twilio.com",
    "https://developer.mozilla.org",
    "https://docs.npmjs.com",
    "https://angular.io",
    "https://docs.astro.build",
    "https://netlify.com",
    "https://cloudflare.com",
    "https://aws.amazon.com",
    "https://linear.app",
    "https://substack.com",
    "https://dev.to",
    "https://meta.com",
    "https://twitter.com",
    "https://nodejs.org",
    "https://redis.io",
    "https://postgresql.org",
    "https://mongodb.com",
]


def load_websites():
    """加载网站列表"""
    if URLS_FILE.exists():
        with open(URLS_FILE, 'r') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return DEFAULT_WEBSITES


def get_evaluated_sites():
    """获取所有已评测过的网站（全局去重）"""
    evaluated = set()
    
    # 从日志文件读取
    if EVALUATED_LOG.exists():
        try:
            with open(EVALUATED_LOG, 'r') as f:
                data = json.load(f)
                evaluated.update(data.get('sites', []))
        except:
            pass
    
    # 从现有JSON文件扫描（兼容旧数据）
    for json_file in DATA_DIR.rglob('*.json'):
        if json_file.name == 'evaluated_sites.json':
            continue
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
                if data.get('url'):
                    evaluated.add(data['url'])
        except:
            pass
    
    return evaluated


def save_evaluated_sites(sites):
    """保存已评测网站列表"""
    data = {
        'sites': list(sites),
        'last_updated': datetime.now().isoformat(),
        'total_count': len(sites)
    }
    with open(EVALUATED_LOG, 'w') as f:
        json.dump(data, f, indent=2)


def select_websites(batch_size=BATCH_SIZE):
    """选择一批未评测的网站"""
    websites = load_websites()
    evaluated = get_evaluated_sites()
    
    # 过滤未评测的
    candidates = [url for url in websites if url not in evaluated]
    
    if len(candidates) < batch_size:
        print(f"⚠️ 剩余未评测网站仅 {len(candidates)} 个，不足 {batch_size} 个")
        print("   将从全部网站中随机选择（会重复评测）")
        candidates = websites
    
    # 随机选择 batch_size 个
    selected = random.sample(candidates, min(batch_size, len(candidates)))
    return selected


def evaluate_website(url, output_dir):
    """评测单个网站"""
    timestamp = datetime.now().strftime('%H%M%S')
    domain = url.replace('https://', '').replace('http://', '').replace('/', '_')
    output_file = output_dir / f"{timestamp}_{domain}.json"
    report_file = output_dir / f"{timestamp}_{domain}.md"
    
    print(f"\n🔍 评测: {url}")
    
    cmd = [
        str(VENV_PYTHON),
        str(BENCHMARK_SCRIPT),
        url,
        "--output", str(report_file),
        "--json",
        "--timeout", "15"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        
        if result.returncode == 0:
            json_file = str(report_file).replace('.md', '.json')
            if os.path.exists(json_file):
                with open(json_file, 'r') as f:
                    data = json.load(f)
                
                evaluation = {
                    "url": url,
                    "timestamp": datetime.now().isoformat(),
                    "result": data[0] if data else None
                }
                
                with open(output_file, 'w') as f:
                    json.dump(evaluation, f, indent=2)
                
                if evaluation["result"] and evaluation["result"].get("success"):
                    score = evaluation["result"]["result"]["score"]
                    grade = evaluation["result"]["result"]["grade"]
                    print(f"   ✅ {score}/100 ({grade})")
                    return evaluation
        
        print(f"   ❌ 失败")
        return None
        
    except Exception as e:
        print(f"   ❌ 错误: {e}")
        return None


def update_readme(evaluations):
    """更新 README 展示最新评测结果"""
    # 读取历史所有评测
    all_evals = []
    for json_file in DATA_DIR.rglob('*.json'):
        if json_file.name in ['evaluated_sites.json']:
            continue
        try:
            with open(json_file, 'r') as f:
                data = json.load(f)
                if data.get("result") and data["result"].get("success"):
                    all_evals.append(data)
        except:
            pass
    
    # 按URL去重，保留最新的
    seen_urls = {}
    for eval in sorted(all_evals, key=lambda x: x.get('timestamp', ''), reverse=True):
        url = eval['url']
        if url not in seen_urls:
            seen_urls[url] = eval
    
    unique_evals = list(seen_urls.values())
    
    if not unique_evals:
        print("⚠️ 没有评测数据")
        return
    
    # 统计信息
    total_sites = len(unique_evals)
    scores = [e['result']['result']['score'] for e in unique_evals]
    avg_score = sum(scores) / len(scores)
    
    # 分级统计
    grade_counts = {'S': 0, 'A': 0, 'B': 0, 'C': 0}
    for e in unique_evals:
        grade = e['result']['result']['grade']
        grade_letter = grade[6] if len(grade) > 6 else 'C'
        if grade_letter in grade_counts:
            grade_counts[grade_letter] += 1
    
    # 生成报告
    lines = []
    lines.append("## 📊 评测统计\n")
    lines.append(f"- **总计评测网站**: {total_sites} 个")
    lines.append(f"- **平均分数**: {avg_score:.1f}/100")
    lines.append(f"- **最后更新**: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    
    lines.append("### 等级分布\n")
    for grade in ['S', 'A', 'B', 'C']:
        count = grade_counts.get(grade, 0)
        bar = '█' * count
        lines.append(f"- **{grade}**: {count} {bar}")
    lines.append("")
    
    lines.append("### 最新评测结果\n")
    lines.append("| 网站 | 分数 | 等级 | 评测时间 |")
    lines.append("|------|------|------|----------|")
    
    for eval in unique_evals[:15]:
        url = eval["url"].replace("https://", "").replace("http://", "")[:28]
        result = eval["result"]["result"]
        score = result["score"]
        grade = result["grade"][6] if len(result["grade"]) > 6 else "?"
        time = eval["timestamp"][:16].replace("T", " ") if 'T' in eval["timestamp"] else eval["timestamp"][:16]
        lines.append(f"| {url} | {score} | {grade} | {time} |")
    
    lines.append("")
    
    readme_section = "\n".join(lines)
    
    # 更新 README
    readme_path = PROJECT_DIR / "README.md"
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    marker_start = "<!-- EVALUATION_RESULTS_START -->"
    marker_end = "<!-- EVALUATION_RESULTS_END -->"
    
    if marker_start in content and marker_end in content:
        parts = content.split(marker_start)
        new_content = parts[0] + marker_start + "\n\n" + readme_section + marker_end + content.split(marker_end)[1]
    else:
        new_content = content + "\n\n" + marker_start + "\n\n" + readme_section + marker_end + "\n"
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("✅ README 已更新")


def git_push():
    """推送到 GitHub"""
    try:
        os.chdir(PROJECT_DIR)
        
        subprocess.run(["git", "config", "user.email", "auto@openaix.org"], check=False, capture_output=True)
        subprocess.run(["git", "config", "user.name", "OpenAIX Bot"], check=False, capture_output=True)
        
        subprocess.run(["git", "add", "-A"], check=False, capture_output=True)
        
        result = subprocess.run(["git", "diff", "--cached", "--quiet"], capture_output=True)
        if result.returncode == 0:
            print("ℹ️ 无更改需提交")
            return
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        count = len(list(DATA_DIR.rglob('*.json'))) - 1  # 排除 evaluated_sites.json
        
        subprocess.run([
            "git", "commit", "-m", 
            f"📊 Auto eval: {count} sites - {timestamp}"
        ], check=False, capture_output=True)
        
        push_result = subprocess.run(["git", "push"], capture_output=True, text=True)
        if push_result.returncode == 0:
            print("✅ 已推送到 GitHub")
        else:
            print(f"⚠️ 推送问题: {push_result.stderr[:200]}")
            
    except Exception as e:
        print(f"❌ Git 错误: {e}")


def main():
    print("="*60)
    print("🤖 OpenAIX 自动评测系统 v2.0")
    print("="*60)
    print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📦 每小时评测: {BATCH_SIZE} 个网站")
    print()
    
    # 已评测网站
    evaluated = get_evaluated_sites()
    print(f"📊 已评测网站: {len(evaluated)} 个")
    
    # 选择网站
    urls = select_websites(BATCH_SIZE)
    print(f"🎯 本次评测: {len(urls)} 个网站")
    for url in urls:
        print(f"   • {url}")
    print()
    
    # 创建今日目录
    today = datetime.now().strftime('%Y%m%d')
    today_dir = DATA_DIR / today
    today_dir.mkdir(exist_ok=True)
    
    # 评测
    results = []
    new_evaluated = set()
    
    for url in urls:
        result = evaluate_website(url, today_dir)
        if result:
            results.append(result)
            new_evaluated.add(url)
    
    # 更新已评测列表
    evaluated.update(new_evaluated)
    save_evaluated_sites(evaluated)
    
    print(f"\n📈 本次成功: {len(results)}/{len(urls)}")
    
    if results:
        print("\n📝 更新 README...")
        update_readme(results)
        
        print("\n🚀 推送到 GitHub...")
        git_push()
        
        print("\n" + "="*60)
        print("✅ 完成!")
        print("="*60)
    else:
        print("\n" + "="*60)
        print("⚠️ 全部失败")
        print("="*60)
        sys.exit(1)


if __name__ == '__main__':
    main()
