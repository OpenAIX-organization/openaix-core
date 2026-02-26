#!/usr/bin/env python3
"""快速评测脚本 - 用于Cron任务"""
import subprocess
import sys
import json
from datetime import datetime
from pathlib import Path

PROJECT_DIR = Path("/home/wesley/.openclaw/workspace/openaix-core")
BENCHMARK_SCRIPT = PROJECT_DIR / "benchmark.py"
VENV_PYTHON = PROJECT_DIR / "venv" / "bin" / "python3"
DATA_DIR = PROJECT_DIR / "data" / "evaluations"
URLS_FILE = PROJECT_DIR / "websites.txt"
BATCH_SIZE = 5

def load_websites():
    """加载网站列表"""
    if URLS_FILE.exists():
        with open(URLS_FILE, 'r') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

def get_evaluated_sites():
    """获取已评测网站"""
    evaluated = set()
    log_file = DATA_DIR / "evaluated_sites.json"
    if log_file.exists():
        try:
            with open(log_file, 'r') as f:
                data = json.load(f)
                evaluated.update(data.get('sites', []))
        except:
            pass
    return evaluated

def select_websites(count):
    """选择未评测的网站"""
    all_sites = load_websites()
    evaluated = get_evaluated_sites()
    
    available = [url for url in all_sites if url not in evaluated]
    
    if len(available) < count:
        # 如果不够，重置已评测列表
        available = all_sites
    
    import random
    selected = random.sample(available, min(count, len(available)))
    return selected

def run_benchmark(urls):
    """运行评测"""
    cmd = [str(VENV_PYTHON), str(BENCHMARK_SCRIPT)] + urls + ['-p', '2', '-t', '10', '--json']
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    return result.returncode == 0, result.stdout, result.stderr

def update_evaluated_log(urls):
    """更新已评测日志"""
    log_file = DATA_DIR / "evaluated_sites.json"
    evaluated = get_evaluated_sites()
    evaluated.update(urls)
    
    with open(log_file, 'w') as f:
        json.dump({'sites': sorted(list(evaluated))}, f, indent=2)
    
    return len(evaluated)

def main():
    print("=" * 60)
    print("🤖 OpenAIX 自动评测系统 v2.0 (Cron)")
    print("=" * 60)
    print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📦 每小时评测: {BATCH_SIZE} 个网站\n")
    
    # 选择网站
    urls = select_websites(BATCH_SIZE)
    print(f"📊 已评测: {len(get_evaluated_sites())} 个")
    print(f"🎯 本次评测: {len(urls)} 个网站")
    for url in urls:
        print(f"   • {url}")
    print()
    
    # 运行评测
    success, stdout, stderr = run_benchmark(urls)
    
    if success:
        # 更新日志
        total_evaluated = update_evaluated_log(urls)
        print(f"✅ 评测完成! 总计已评测: {total_evaluated} 个网站")
        return 0
    else:
        print(f"❌ 评测失败")
        if stderr:
            print(f"错误: {stderr[:500]}")
        return 1

if __name__ == '__main__':
    sys.exit(main())
