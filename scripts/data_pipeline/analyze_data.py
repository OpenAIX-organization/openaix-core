#!/usr/bin/env python3
"""
OpenAIX 数据聚合分析脚本
解析所有评测报告并生成综合分析
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict
from statistics import mean, median, stdev

def parse_evaluation_file(filepath):
    """解析单个评测报告文件"""
    content = filepath.read_text(encoding='utf-8')
    data = {}
    
    # 提取基本信息
    url_match = re.search(r'\*\*Target\*\*: (https?://[^\s]+)', content)
    if url_match:
        data['url'] = url_match.group(1)
    
    score_match = re.search(r'\*\*Score\*\*: (\d+)/100', content)
    if score_match:
        data['score'] = int(score_match.group(1))
    
    grade_match = re.search(r'\*\*Grade\*\*: Class ([SABC])', content)
    if grade_match:
        data['grade'] = grade_match.group(1)
    
    site_type_match = re.search(r'\*\*Site Type\*\*: (\w+)', content)
    if site_type_match:
        data['site_type'] = site_type_match.group(1)
    
    # 提取维度分数
    snr_score = re.search(r'### Snr.*?- Score: (\d+)', content, re.DOTALL)
    if snr_score:
        data['snr_score'] = int(snr_score.group(1))
    
    semantic_score = re.search(r'### Semantic.*?- Score: (\d+)', content, re.DOTALL)
    if semantic_score:
        data['semantic_score'] = int(semantic_score.group(1))
    
    token_score = re.search(r'### Token Economy.*?- Score: (\d+)', content, re.DOTALL)
    if token_score:
        data['token_score'] = int(token_score.group(1))
    
    permissions_score = re.search(r'### Permissions.*?- Score: (\d+)', content, re.DOTALL)
    if permissions_score:
        data['permissions_score'] = int(permissions_score.group(1))
    
    api_score = re.search(r'### Api Availability.*?- Score: (\d+)', content, re.DOTALL)
    if api_score:
        data['api_score'] = int(api_score.group(1))
    
    # 提取 SNR 详细信息
    snr_percent = re.search(r'snr_percent: ([\d.]+)', content)
    if snr_percent:
        data['snr_percent'] = float(snr_percent.group(1))
    
    raw_tokens = re.search(r'raw_tokens: (\d+)', content)
    if raw_tokens:
        data['raw_tokens'] = int(raw_tokens.group(1))
    
    clean_tokens = re.search(r'clean_tokens: (\d+)', content)
    if clean_tokens:
        data['clean_tokens'] = int(clean_tokens.group(1))
    
    # 提取其他关键指标
    json_ld = re.search(r'json_ld_present: (True|False)', content)
    if json_ld:
        data['json_ld'] = json_ld.group(1) == 'True'
    
    llms_txt = re.search(r'llms_txt_present: (True|False)', content)
    if llms_txt:
        data['llms_txt'] = llms_txt.group(1) == 'True'
    
    has_api = re.search(r'has_api: (True|False)', content)
    if has_api:
        data['has_api'] = has_api.group(1) == 'True'
    
    return data

def analyze_all_data():
    """分析所有评测数据"""
    base_path = Path('/Users/wesley/Desktop/repo/openaix-core/data/evaluations')
    all_data = []
    
    # 递归查找所有 .md 文件（排除 summary 和 report）
    for md_file in base_path.rglob('*.md'):
        if 'summary' in md_file.name or 'report' in md_file.name:
            continue
        try:
            data = parse_evaluation_file(md_file)
            if 'score' in data:
                data['filename'] = md_file.name
                all_data.append(data)
        except Exception as e:
            print(f"Error parsing {md_file}: {e}")
    
    print(f"✅ 成功解析 {len(all_data)} 个评测报告\n")
    return all_data

def generate_statistics(data):
    """生成统计分析"""
    scores = [d['score'] for d in data]
    
    print("=" * 60)
    print("📊 OpenAIX 评测数据综合分析报告")
    print("=" * 60)
    
    # 基本统计
    print("\n## 一、基础统计")
    print(f"总评测网站数: {len(data)}")
    print(f"平均分数: {mean(scores):.1f}")
    print(f"中位数: {median(scores):.1f}")
    print(f"标准差: {stdev(scores):.1f}")
    print(f"最高分: {max(scores)}")
    print(f"最低分: {min(scores)}")
    
    # 等级分布
    print("\n## 二、等级分布")
    grades = defaultdict(int)
    for d in data:
        grades[d.get('grade', 'Unknown')] += 1
    
    for grade in ['S', 'A', 'B', 'C']:
        count = grades.get(grade, 0)
        pct = count / len(data) * 100
        bar = '█' * int(pct / 2)
        print(f"等级 {grade}: {count:3d} ({pct:5.1f}%) {bar}")
    
    # 维度统计
    print("\n## 三、五维度平均分")
    dimensions = ['snr_score', 'semantic_score', 'token_score', 'permissions_score', 'api_score']
    dim_names = {
        'snr_score': 'SNR (信噪比)',
        'semantic_score': 'Semantic (语义结构)',
        'token_score': 'Token Economy',
        'permissions_score': 'Permissions (权限)',
        'api_score': 'API Availability'
    }
    
    for dim in dimensions:
        values = [d[dim] for d in data if dim in d]
        if values:
            avg = mean(values)
            print(f"{dim_names[dim]:25s}: {avg:5.1f}/100")
    
    # 网站类型分析
    print("\n## 四、网站类型分析")
    site_types = defaultdict(list)
    for d in data:
        st = d.get('site_type', 'unknown')
        site_types[st].append(d['score'])
    
    for site_type, scores_list in sorted(site_types.items()):
        avg = mean(scores_list)
        count = len(scores_list)
        pct = count / len(data) * 100
        print(f"{site_type:15s}: {count:3d}个 ({pct:4.1f}%) | 平均分: {avg:.1f}")
    
    # 异常值分析
    print("\n## 五、TOP & BOTTOM 案例")
    sorted_data = sorted(data, key=lambda x: x['score'], reverse=True)
    
    print("\n🏆 高分案例 (Top 5):")
    for i, d in enumerate(sorted_data[:5], 1):
        url = d.get('url', d.get('filename', 'Unknown'))
        print(f"  {i}. {url:40s} - {d['score']}分 (等级{d.get('grade', '?')})")
    
    print("\n⚠️  低分案例 (Bottom 5):")
    for i, d in enumerate(sorted_data[-5:], 1):
        url = d.get('url', d.get('filename', 'Unknown'))
        print(f"  {i}. {url:40s} - {d['score']}分 (等级{d.get('grade', '?')})")
    
    # 关键发现
    print("\n## 六、关键发现")
    
    # llms.txt 统计
    llms_txt_count = sum(1 for d in data if d.get('llms_txt'))
    print(f"\n1. llms.txt 采用率: {llms_txt_count}/{len(data)} ({llms_txt_count/len(data)*100:.1f}%)")
    
    # JSON-LD 统计
    json_ld_count = sum(1 for d in data if d.get('json_ld'))
    print(f"2. JSON-LD 采用率: {json_ld_count}/{len(data)} ({json_ld_count/len(data)*100:.1f}%)")
    
    # API 可用性
    has_api_count = sum(1 for d in data if d.get('has_api'))
    print(f"3. API 可用性: {has_api_count}/{len(data)} ({has_api_count/len(data)*100:.1f}%)")
    
    # SNR 分析
    snr_values = [d['snr_percent'] for d in data if 'snr_percent' in d]
    if snr_values:
        print(f"4. 平均信噪比: {mean(snr_values):.1f}%")
        low_snr = sum(1 for s in snr_values if s < 10)
        print(f"   信噪比 < 10% 的网站: {low_snr}个 ({low_snr/len(snr_values)*100:.1f}%)")
    
    print("\n" + "=" * 60)
    
    return data

def export_to_json(data):
    """导出数据为JSON"""
    output_file = '/Users/wesley/Desktop/repo/openaix-core/data/analysis_summary.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"\n💾 数据已导出到: {output_file}")

if __name__ == '__main__':
    print("🔍 开始分析 OpenAIX 评测数据...\n")
    data = analyze_all_data()
    generate_statistics(data)
    export_to_json(data)
