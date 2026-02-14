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
import requests
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
except ImportError:
    BS4_AVAILABLE = False
    print("⚠️ 警告: beautifulsoup4 未安装，网站内容分析功能将受限")
    print("   安装命令: pip install beautifulsoup4 lxml")

# 配置
PROJECT_DIR = Path("/home/wesley/.openclaw/workspace/openaix-core")
DATA_DIR = PROJECT_DIR / "data" / "evaluations"
URLS_FILE = PROJECT_DIR / "websites.txt"
BENCHMARK_SCRIPT = PROJECT_DIR / "benchmark.py"
VENV_PYTHON = PROJECT_DIR / "venv" / "bin" / "python3"
EVALUATED_LOG = DATA_DIR / "evaluated_sites.json"
BATCH_SIZE = 3  # 每小时评测数量

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


def analyze_website_content(url, timeout=10):
    """
    分析网站内容，提取关键信息用于数据库建设
    
    返回:
        dict: 包含网站定位、主要内容、AI可用信息等
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        }
        
        response = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)
        response.raise_for_status()
        
        content = response.text
        parsed_url = urlparse(response.url)
        
        analysis = {
            'url': url,
            'final_url': response.url,
            'domain': parsed_url.netloc,
            'title': '',
            'meta_description': '',
            'main_content_preview': '',
            'content_type': 'unknown',
            'ai_use_cases': [],
            'key_topics': [],
            'language': '',
            'has_structured_data': False,
            'extracted_at': datetime.now().isoformat()
        }
        
        if BS4_AVAILABLE and content:
            soup = BeautifulSoup(content, 'lxml')
            
            # 提取标题
            title_tag = soup.find('title')
            if title_tag:
                analysis['title'] = title_tag.get_text(strip=True)[:200]
            
            # 提取 meta description
            meta_desc = soup.find('meta', attrs={'name': 'description'}) or \
                       soup.find('meta', attrs={'property': 'og:description'})
            if meta_desc:
                analysis['meta_description'] = meta_desc.get('content', '')[:500]
            
            # 提取语言
            html_tag = soup.find('html')
            if html_tag and html_tag.get('lang'):
                analysis['language'] = html_tag.get('lang')
            
            # 提取主要内容预览
            content_selectors = ['main', 'article', '[role="main"]', '.content', 
                               '.main-content', '#content', '#main-content', 'body']
            
            main_text = ''
            for selector in content_selectors:
                element = soup.select_one(selector)
                if element:
                    text = element.get_text(separator=' ', strip=True)
                    text = ' '.join(text.split())
                    main_text = text[:1500]  # 取前1500字符
                    break
            
            analysis['main_content_preview'] = main_text
            
            # 提取关键主题（从 headings 中）
            headings = soup.find_all(['h1', 'h2', 'h3'])
            keywords = []
            for h in headings[:10]:
                text = h.get_text(strip=True)
                if text and len(text) > 3:
                    keywords.append(text[:100])
            analysis['key_topics'] = keywords[:5]
            
            # 检测结构化数据
            structured_selectors = ['script[type="application/ld+json"]', '[itemscope]']
            for selector in structured_selectors:
                if soup.select(selector):
                    analysis['has_structured_data'] = True
                    break
            
            # 检测内容类型
            domain_lower = analysis['domain'].lower()
            desc_lower = analysis['meta_description'].lower()
            
            if any(x in domain_lower for x in ['docs.', 'documentation', 'wiki', 'help']) or \
               'documentation' in desc_lower:
                analysis['content_type'] = 'documentation'
            elif any(x in domain_lower for x in ['news', 'blog', 'medium', 'substack']):
                analysis['content_type'] = 'news/blog'
            elif any(x in domain_lower for x in ['shop', 'store', 'amazon', 'ebay']) or \
                 soup.find('meta', attrs={'property': 'product:price'}):
                analysis['content_type'] = 'e-commerce'
            elif any(x in domain_lower for x in ['edu', 'university', 'college', 'mit.', 'harvard.']):
                analysis['content_type'] = 'education'
            elif any(x in domain_lower for x in ['github', 'gitlab', 'bitbucket']):
                analysis['content_type'] = 'code_repository'
            elif any(x in domain_lower for x in ['youtube', 'vimeo', 'tiktok', 'bilibili']):
                analysis['content_type'] = 'video_platform'
            elif soup.find('form'):
                analysis['content_type'] = 'web_application'
            else:
                analysis['content_type'] = 'general_website'
            
            # AI 使用场景建议
            ai_use_cases_map = {
                'documentation': [
                    '技术文档问答与检索',
                    'API 使用示例生成',
                    '错误排查与解决方案推荐',
                    '代码片段提取与解释',
                    '版本变更说明分析'
                ],
                'news/blog': [
                    '内容摘要与关键信息提取',
                    '行业趋势分析与预测',
                    '多语言翻译与本地化',
                    '情感分析与观点识别',
                    '热点话题追踪'
                ],
                'e-commerce': [
                    '产品价格监控与比较',
                    '商品描述智能优化',
                    '用户评价情感分析',
                    '库存状态监控',
                    '竞品分析报告生成'
                ],
                'education': [
                    '学习资料智能整理',
                    '课程推荐与规划',
                    '研究论文摘要与分析',
                    '知识点提取与知识图谱构建',
                    '学术资源检索'
                ],
                'code_repository': [
                    '代码审查与质量分析',
                    '项目文档自动生成',
                    '依赖关系与安全分析',
                    '功能模块识别与提取',
                    '贡献者行为分析'
                ],
                'video_platform': [
                    '视频内容转录与摘要',
                    '字幕生成与翻译',
                    '内容分类与标签提取',
                    '创作者分析',
                    '趋势视频识别'
                ],
                'web_application': [
                    '功能可用性监控',
                    '用户流程分析',
                    '表单数据处理',
                    '自动化测试支持',
                    '性能监控'
                ],
                'general_website': [
                    '网站内容摘要',
                    '信息分类与标签',
                    '关键词与主题提取',
                    '更新监控与变更检测',
                    'SEO 内容分析'
                ]
            }
            
            analysis['ai_use_cases'] = ai_use_cases_map.get(analysis['content_type'], 
                                                             ai_use_cases_map['general_website'])
            
            # 生成网站定位描述
            if analysis['title'] and analysis['meta_description']:
                analysis['site_positioning'] = f"{analysis['title']} - {analysis['meta_description'][:200]}"
            elif analysis['title']:
                analysis['site_positioning'] = analysis['title']
            else:
                analysis['site_positioning'] = f"{analysis['domain']} ({analysis['content_type']})"
        
        return analysis
        
    except requests.exceptions.Timeout:
        return {'error': '连接超时', 'url': url, 'content_type': 'timeout', 'extracted_at': datetime.now().isoformat()}
    except requests.exceptions.RequestException as e:
        return {'error': str(e), 'url': url, 'content_type': 'error', 'extracted_at': datetime.now().isoformat()}
    except Exception as e:
        return {'error': f'分析错误: {str(e)}', 'url': url, 'content_type': 'error', 'extracted_at': datetime.now().isoformat()}


def evaluate_website(url, output_dir):
    """评测单个网站（包含AIX评分和内容分析）"""
    timestamp = datetime.now().strftime('%H%M%S')
    domain = url.replace('https://', '').replace('http://', '').replace('/', '_')
    output_file = output_dir / f"{timestamp}_{domain}.json"
    report_file = output_dir / f"{timestamp}_{domain}.md"
    
    print(f"\n🔍 评测: {url}")
    
    # Step 1: 运行 AIX 评分
    cmd = [
        str(VENV_PYTHON),
        str(BENCHMARK_SCRIPT),
        url,
        "--output", str(report_file),
        "--json",
        "--timeout", "15"
    ]
    
    aix_result = None
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        
        if result.returncode == 0:
            json_file = str(report_file).replace('.md', '.json')
            if os.path.exists(json_file):
                with open(json_file, 'r') as f:
                    data = json.load(f)
                aix_result = data[0] if data else None
    except Exception as e:
        print(f"   ⚠️ AIX评分错误: {e}")
    
    # Step 2: 分析网站内容
    print(f"   📄 分析网站内容...")
    content_analysis = analyze_website_content(url, timeout=8)
    
    # Step 3: 合并结果
    evaluation = {
        "url": url,
        "timestamp": datetime.now().isoformat(),
        "result": aix_result,
        "content_analysis": content_analysis
    }
    
    # 保存结果
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(evaluation, f, indent=2, ensure_ascii=False)
    
    # 输出结果摘要
    if aix_result and aix_result.get("success"):
        score = aix_result["result"]["score"]
        grade = aix_result["result"]["grade"]
        content_type = content_analysis.get('content_type', 'unknown')
        print(f"   ✅ AIX: {score}/100 ({grade}) | 类型: {content_type}")
        return evaluation
    elif content_analysis and not content_analysis.get('error'):
        content_type = content_analysis.get('content_type', 'unknown')
        print(f"   ⚠️ AIX失败，内容分析完成 | 类型: {content_type}")
        return evaluation
    else:
        print(f"   ❌ 失败")
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
        
        # 先拉取再推送，避免冲突
        pull_result = subprocess.run(["git", "pull", "--rebase"], capture_output=True, text=True, timeout=30)
        if pull_result.returncode != 0:
            print(f"   ⚠️ 拉取失败，尝试强制推送: {pull_result.stderr[:100]}")
        
        push_result = subprocess.run(["git", "push"], capture_output=True, text=True)
        if push_result.returncode == 0:
            print("✅ 已推送到 GitHub")
        else:
            print(f"⚠️ 推送问题: {push_result.stderr[:200]}")
            
    except Exception as e:
        print(f"❌ Git 错误: {e}")


def git_pull():
    """拉取最新代码"""
    try:
        os.chdir(PROJECT_DIR)
        print("🔄 拉取最新代码...")
        result = subprocess.run(
            ["git", "pull", "--rebase"],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            print("   ✅ 代码已更新")
        else:
            print(f"   ⚠️ 拉取可能有冲突: {result.stderr[:100]}")
    except Exception as e:
        print(f"   ⚠️ 拉取失败: {e}")


def main():
    print("="*60)
    print("🤖 OpenAIX 自动评测系统 v2.0")
    print("="*60)
    print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📦 每小时评测: {BATCH_SIZE} 个网站")
    print()
    
    # 先拉取最新代码
    git_pull()
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
