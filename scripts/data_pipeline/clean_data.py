#!/usr/bin/env python3
"""
OpenAIX 数据清理脚本
- 移除0分记录（抓取失败）
- URL去重，保留最新评测
- 生成干净的数据集用于发布
"""

import json
import re
from pathlib import Path
from collections import defaultdict
from datetime import datetime
from statistics import mean, median

def extract_timestamp(filename):
    """从文件名提取时间戳"""
    # 格式: HHMMSS_domain.md
    match = re.match(r'(\d{6})_', filename)
    if match:
        return match.group(1)
    return '000000'

def clean_data():
    """清理数据"""
    input_file = Path('/Users/wesley/Desktop/repo/openaix-core/data/analysis_summary.json')
    
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"📥 原始数据: {len(data)} 条记录")
    
    # 步骤1: 过滤掉0分记录
    valid_data = [d for d in data if d.get('score', 0) > 0]
    print(f"✅ 移除0分记录: {len(data) - len(valid_data)} 条")
    print(f"📊 有效记录: {len(valid_data)} 条")
    
    # 步骤2: 按URL分组，保留最新的评测
    url_groups = defaultdict(list)
    for item in valid_data:
        url = item.get('url', '')
        if url:
            url_groups[url].append(item)
    
    # 对每个URL，选择最新的记录
    cleaned_data = []
    duplicates_removed = 0
    
    for url, items in url_groups.items():
        if len(items) > 1:
            # 按文件名时间戳排序，保留最新的
            items_sorted = sorted(items, key=lambda x: extract_timestamp(x.get('filename', '')), reverse=True)
            cleaned_data.append(items_sorted[0])
            duplicates_removed += len(items) - 1
        else:
            cleaned_data.append(items[0])
    
    print(f"🔄 去重处理: {duplicates_removed} 条重复记录被移除")
    print(f"✨ 最终干净数据: {len(cleaned_data)} 条唯一记录")
    
    return cleaned_data

def generate_statistics(data):
    """生成统计报告"""
    scores = [d['score'] for d in data]
    
    print("\n" + "="*60)
    print("📊 清理后数据统计报告")
    print("="*60)
    
    # 基础统计
    print(f"\n总网站数: {len(data)}")
    print(f"平均分数: {mean(scores):.1f}")
    print(f"中位数: {median(scores):.1f}")
    print(f"最高分: {max(scores)}")
    print(f"最低分: {min(scores)}")
    
    # 等级分布
    from collections import Counter
    grades = Counter(d.get('grade', 'Unknown') for d in data)
    
    print("\n等级分布:")
    for grade in ['S', 'A', 'B', 'C']:
        count = grades.get(grade, 0)
        pct = count / len(data) * 100
        bar = '█' * int(pct / 2)
        print(f"  等级 {grade}: {count:3d} ({pct:5.1f}%) {bar}")
    
    # 网站类型分析
    from collections import defaultdict
    site_types = defaultdict(list)
    for d in data:
        st = d.get('site_type', 'unknown')
        site_types[st].append(d['score'])
    
    print("\n网站类型分布:")
    for site_type, scores_list in sorted(site_types.items(), key=lambda x: -len(x[1])):
        avg = mean(scores_list)
        count = len(scores_list)
        pct = count / len(data) * 100
        print(f"  {site_type:15s}: {count:3d} ({pct:4.1f}%) | 均分: {avg:.1f}")
    
    # 关键指标
    llms_txt_count = sum(1 for d in data if d.get('llms_txt'))
    json_ld_count = sum(1 for d in data if d.get('json_ld'))
    has_api_count = sum(1 for d in data if d.get('has_api'))
    
    print("\n关键指标:")
    print(f"  llms.txt 采用率: {llms_txt_count}/{len(data)} ({llms_txt_count/len(data)*100:.1f}%)")
    print(f"  JSON-LD 采用率: {json_ld_count}/{len(data)} ({json_ld_count/len(data)*100:.1f}%)")
    print(f"  API 可用性: {has_api_count}/{len(data)} ({has_api_count/len(data)*100:.1f}%)")
    
    # TOP和BOTTOM
    sorted_data = sorted(data, key=lambda x: x['score'], reverse=True)
    
    print("\n🏆 高分网站 (Top 10):")
    for i, d in enumerate(sorted_data[:10], 1):
        url = d.get('url', 'Unknown')
        print(f"  {i:2d}. {url:40s} - {d['score']}分 ({d.get('grade', '?')})")
    
    print("\n⚠️  低分网站 (Bottom 10):")
    for i, d in enumerate(sorted_data[-10:], 1):
        url = d.get('url', 'Unknown')
        print(f"  {i:2d}. {url:40s} - {d['score']}分 ({d.get('grade', '?')})")

def export_data(data):
    """导出数据"""
    output_dir = Path('/Users/wesley/Desktop/repo/openaix-core/data/cleaned')
    output_dir.mkdir(exist_ok=True)
    
    # 导出JSON
    json_file = output_dir / 'openaix_rankings.json'
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"\n💾 JSON导出: {json_file}")
    
    # 导出CSV
    import csv
    csv_file = output_dir / 'openaix_rankings.csv'
    
    # 确定所有字段
    all_fields = set()
    for item in data:
        all_fields.update(item.keys())
    
    # 固定字段顺序
    fieldnames = ['url', 'score', 'grade', 'site_type', 
                  'snr_score', 'semantic_score', 'token_score', 
                  'permissions_score', 'api_score',
                  'snr_percent', 'raw_tokens', 'clean_tokens',
                  'json_ld', 'llms_txt', 'has_api', 'filename']
    
    # 添加其他字段
    for field in sorted(all_fields):
        if field not in fieldnames:
            fieldnames.append(field)
    
    with open(csv_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"💾 CSV导出: {csv_file}")
    
    # 生成Markdown报告
    md_file = output_dir / 'rankings_report.md'
    generate_markdown_report(data, md_file)
    print(f"📝 Markdown报告: {md_file}")
    
    return output_dir

def generate_markdown_report(data, output_file):
    """生成Markdown格式的报告"""
    from collections import Counter
    from statistics import mean
    
    scores = [d['score'] for d in data]
    grades = Counter(d.get('grade', 'Unknown') for d in data)
    
    # 按类型分组
    from collections import defaultdict
    site_types = defaultdict(list)
    for d in data:
        st = d.get('site_type', 'unknown')
        site_types[st].append(d)
    
    md_content = f"""# OpenAIX 网站AI友好度排行榜

> 数据更新时间: {datetime.now().strftime('%Y-%m-%d')}
> 评测网站总数: {len(data)} 个

## 📊 总体统计

| 指标 | 数值 |
|------|------|
| 平均分数 | {mean(scores):.1f}/100 |
| 中位数 | {median(scores):.1f}/100 |
| 最高分 | {max(scores)} |
| 最低分 | {min(scores)} |

## 🏆 等级分布

| 等级 | 数量 | 占比 | 描述 |
|------|------|------|------|
| S | {grades.get('S', 0)} | {grades.get('S', 0)/len(data)*100:.1f}% | 硅基原生 - 精英级别 |
| A | {grades.get('A', 0)} | {grades.get('A', 0)/len(data)*100:.1f}% | Agent友好 - 优秀 |
| B | {grades.get('B', 0)} | {grades.get('B', 0)/len(data)*100:.1f}% | 人类优化 - 良好 |
| C | {grades.get('C', 0)} | {grades.get('C', 0)/len(data)*100:.1f}% | 需要改进 |

## 📈 网站类型分析

| 类型 | 数量 | 占比 | 平均分 |
|------|------|------|--------|
"""
    
    for site_type, items in sorted(site_types.items(), key=lambda x: -len(x[1])):
        avg = mean([d['score'] for d in items])
        count = len(items)
        pct = count / len(data) * 100
        md_content += f"| {site_type} | {count} | {pct:.1f}% | {avg:.1f} |\n"
    
    # TOP 50
    sorted_data = sorted(data, key=lambda x: x['score'], reverse=True)
    
    md_content += f"""
## 🥇 TOP 50 网站

| 排名 | 网站 | 分数 | 等级 | 类型 |
|------|------|------|------|------|
"""
    
    for i, d in enumerate(sorted_data[:50], 1):
        url = d.get('url', 'Unknown')
        score = d['score']
        grade = d.get('grade', '?')
        site_type = d.get('site_type', 'unknown')
        md_content += f"| {i} | {url} | {score} | {grade} | {site_type} |\n"
    
    # 关键指标
    llms_txt_count = sum(1 for d in data if d.get('llms_txt'))
    json_ld_count = sum(1 for d in data if d.get('json_ld'))
    has_api_count = sum(1 for d in data if d.get('has_api'))
    
    md_content += f"""
## 🔍 关键发现

- **llms.txt 采用率**: {llms_txt_count}/{len(data)} ({llms_txt_count/len(data)*100:.1f}%)
- **JSON-LD 采用率**: {json_ld_count}/{len(data)} ({json_ld_count/len(data)*100:.1f}%)
- **API 可用性**: {has_api_count}/{len(data)} ({has_api_count/len(data)*100:.1f}%)

## 📥 数据下载

- [JSON格式](openaix_rankings.json)
- [CSV格式](openaix_rankings.csv)

---

*本报告由 OpenAIX 自动生成*
*项目地址: https://github.com/OpenAIX-organization/openaix-core*
"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(md_content)

if __name__ == '__main__':
    print("🧹 OpenAIX 数据清理工具\n")
    
    # 清理数据
    cleaned_data = clean_data()
    
    # 生成统计
    generate_statistics(cleaned_data)
    
    # 导出数据
    output_dir = export_data(cleaned_data)
    
    print(f"\n✅ 数据清理完成!")
    print(f"📁 输出目录: {output_dir}")
    print(f"🎉 现在可以发布你的排行榜了!")
