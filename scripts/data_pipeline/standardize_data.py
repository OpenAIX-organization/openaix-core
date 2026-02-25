#!/usr/bin/env python3
"""
OpenAIX 数据标准化脚本 v2.0
- 统一等级计算标准
- 修复历史数据中的不一致
- 生成标准化的前端数据
"""

import json
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Any, Optional

# 配置
DATA_DIR = Path('/Users/wesley/Desktop/repo/openaix-core/data')
EVALUATIONS_DIR = DATA_DIR / 'evaluations'
CLEANED_DIR = DATA_DIR / 'cleaned'
EXPORTS_DIR = DATA_DIR / 'exports'

# 评分标准配置
GRADING_STANDARD = {
    "version": "v2.0_fixed",
    "name": "Fixed Threshold",
    "description": "固定阈值等级划分",
    "thresholds": {
        "S": {"min": 80, "max": 100, "label": "硅基原生"},
        "A": {"min": 65, "max": 79, "label": "Agent友好"},
        "B": {"min": 50, "max": 64, "label": "人类优化"},
        "C": {"min": 0, "max": 49, "label": "需要改进"}
    }
}

def calculate_grade(score: int) -> str:
    """使用固定阈值计算等级"""
    if score >= 80:
        return "S"
    elif score >= 65:
        return "A"
    elif score >= 50:
        return "B"
    else:
        return "C"

def parse_evaluation_file(filepath: Path) -> Optional[Dict[str, Any]]:
    """解析单个评测报告文件"""
    try:
        content = filepath.read_text(encoding='utf-8')
        data = {
            "filename": filepath.name,
            "filepath": str(filepath.relative_to(DATA_DIR)),
            "evaluated_at": extract_timestamp(filepath.name)
        }
        
        # 提取URL
        url_match = re.search(r'\*\*Target\*\*: (https?://[^\s]+)', content)
        if url_match:
            data['url'] = url_match.group(1)
            data['domain'] = extract_domain(url_match.group(1))
        
        # 提取分数
        score_match = re.search(r'\*\*Score\*\*: (\d+)/100', content)
        if score_match:
            data['score'] = int(score_match.group(1))
        
        # 提取原始等级（用于对比）
        grade_match = re.search(r'\*\*Grade\*\*: Class ([SABC])', content)
        if grade_match:
            data['original_grade'] = grade_match.group(1)
        
        # 提取类型
        site_type_match = re.search(r'\*\*Site Type\*\*: (\w+)', content)
        if site_type_match:
            data['site_type'] = site_type_match.group(1)
        
        # 提取维度分数
        for dim in ['snr', 'semantic', 'token', 'permissions', 'api']:
            pattern = rf'### {dim.capitalize()}.*?- Score: (\d+)'
            match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
            if match:
                data[f'{dim}_score'] = int(match.group(1))
        
        # 提取元数据
        snr_percent = re.search(r'snr_percent: ([\d.]+)', content)
        if snr_percent:
            data['snr_percent'] = float(snr_percent.group(1))
        
        raw_tokens = re.search(r'raw_tokens: (\d+)', content)
        if raw_tokens:
            data['raw_tokens'] = int(raw_tokens.group(1))
        
        clean_tokens = re.search(r'clean_tokens: (\d+)', content)
        if clean_tokens:
            data['clean_tokens'] = int(clean_tokens.group(1))
        
        # 提取特性标志
        data['json_ld'] = bool(re.search(r'json_ld_present: True', content))
        data['llms_txt'] = bool(re.search(r'llms_txt_present: True', content))
        data['has_api'] = bool(re.search(r'has_api: True', content))
        
        # 计算新的标准化等级
        if 'score' in data:
            data['grade'] = calculate_grade(data['score'])
            data['grade_standard'] = GRADING_STANDARD['version']
        
        return data
    except Exception as e:
        print(f"  ⚠️  解析失败 {filepath}: {e}")
        return None

def extract_timestamp(filename: str) -> str:
    """从文件名提取时间戳"""
    # 格式: HHMMSS_domain.md
    match = re.match(r'(\d{6})_', filename)
    if match:
        ts = match.group(1)
        return f"2026-02-23T{ts[:2]}:{ts[2:4]}:{ts[4:6]}Z"
    return datetime.now().isoformat()

def extract_domain(url: str) -> str:
    """从URL提取域名"""
    domain = url.replace('https://', '').replace('http://', '').replace('/', '')
    return domain

def load_all_evaluations() -> List[Dict[str, Any]]:
    """加载所有评测记录"""
    print("🔍 正在扫描所有评测文件...")
    evaluations = []
    
    for date_dir in EVALUATIONS_DIR.iterdir():
        if not date_dir.is_dir():
            continue
        
        for md_file in date_dir.glob('*.md'):
            if 'summary' in md_file.name or 'report' in md_file.name:
                continue
            
            eval_data = parse_evaluation_file(md_file)
            if eval_data and 'score' in eval_data:
                evaluations.append(eval_data)
    
    print(f"✅ 加载了 {len(evaluations)} 条评测记录")
    return evaluations

def aggregate_by_site(evaluations: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    """按网站聚合评测记录"""
    print("\n📊 正在聚合网站数据...")
    
    sites = defaultdict(lambda: {
        "domain": "",
        "url": "",
        "evaluations": [],
        "first_seen": None,
        "last_evaluated": None
    })
    
    for eval_data in evaluations:
        domain = eval_data.get('domain')
        if not domain:
            continue
        
        site = sites[domain]
        site['domain'] = domain
        site['url'] = eval_data.get('url', site['url'])
        site['evaluations'].append(eval_data)
        
        # 更新首次/最后评测时间
        eval_time = eval_data.get('evaluated_at')
        if eval_time:
            if not site['first_seen'] or eval_time < site['first_seen']:
                site['first_seen'] = eval_time
            if not site['last_evaluated'] or eval_time > site['last_evaluated']:
                site['last_evaluated'] = eval_time
    
    print(f"✅ 聚合了 {len(sites)} 个唯一网站")
    return dict(sites)

def calculate_site_summary(site: Dict[str, Any]) -> Dict[str, Any]:
    """计算网站汇总信息"""
    evaluations = site['evaluations']
    
    if not evaluations:
        return None
    
    # 按时间排序
    sorted_evals = sorted(evaluations, key=lambda x: x.get('evaluated_at', ''), reverse=True)
    
    # 最新评测
    latest = sorted_evals[0]
    
    # 最佳评测（按分数）
    best = max(evaluations, key=lambda x: x.get('score', 0))
    
    # 分数趋势
    scores = [e.get('score', 0) for e in sorted_evals[:5]]  # 最近5次
    avg_score = sum(scores) / len(scores) if scores else 0
    
    if len(scores) >= 2:
        if scores[0] > scores[-1]:
            trend = "improving"
        elif scores[0] < scores[-1]:
            trend = "declining"
        else:
            trend = "stable"
    else:
        trend = "stable"
    
    return {
        "domain": site['domain'],
        "url": site['url'],
        "first_seen": site['first_seen'],
        "last_evaluated": site['last_evaluated'],
        
        "current": {
            "score": latest.get('score', 0),
            "grade": latest.get('grade', 'C'),
            "site_type": latest.get('site_type', 'unknown'),
            "evaluated_at": latest.get('evaluated_at'),
            "features": {
                "llms_txt": latest.get('llms_txt', False),
                "json_ld": latest.get('json_ld', False),
                "has_api": latest.get('has_api', False)
            }
        },
        
        "best": {
            "score": best.get('score', 0),
            "grade": best.get('grade', 'C'),
            "evaluated_at": best.get('evaluated_at')
        },
        
        "history": {
            "evaluation_count": len(evaluations),
            "score_trend": trend,
            "average_score": round(avg_score, 1)
        },
        
        "all_evaluations": [e['filename'] for e in evaluations]
    }

def generate_exports(sites_data: Dict[str, Dict[str, Any]]) -> None:
    """生成前端导出数据"""
    print("\n📦 正在生成导出数据...")
    
    EXPORTS_DIR.mkdir(exist_ok=True)
    
    # 准备当前分数排行数据
    current_rankings = []
    for domain, site in sites_data.items():
        summary = calculate_site_summary(site)
        if summary:
            current_rankings.append({
                "domain": summary['domain'],
                "url": summary['url'],
                "score": summary['current']['score'],
                "grade": summary['current']['grade'],
                "site_type": summary['current']['site_type'],
                "evaluated_at": summary['current']['evaluated_at'],
                "features": summary['current']['features'],
                "history_count": summary['history']['evaluation_count']
            })
    
    # 排序并添加排名
    current_rankings.sort(key=lambda x: x['score'], reverse=True)
    for i, site in enumerate(current_rankings, 1):
        site['rank'] = i
    
    # 导出当前排行
    export_current = {
        "meta": {
            "generated_at": datetime.now().isoformat(),
            "standard_version": GRADING_STANDARD['version'],
            "standard_name": GRADING_STANDARD['name'],
            "total_sites": len(current_rankings),
            "data_source": "current"
        },
        "sites": current_rankings
    }
    
    with open(EXPORTS_DIR / 'rankings_current.json', 'w', encoding='utf-8') as f:
        json.dump(export_current, f, ensure_ascii=False, indent=2)
    
    print(f"  ✓ rankings_current.json ({len(current_rankings)} sites)")
    
    # 导出网站索引（包含历史）
    sites_index = {
        "meta": {
            "generated_at": datetime.now().isoformat(),
            "standard_version": GRADING_STANDARD['version'],
            "total_sites": len(sites_data)
        },
        "sites": {domain: calculate_site_summary(site) for domain, site in sites_data.items()}
    }
    
    with open(EXPORTS_DIR / 'sites_index.json', 'w', encoding='utf-8') as f:
        json.dump(sites_index, f, ensure_ascii=False, indent=2)
    
    print(f"  ✓ sites_index.json ({len(sites_data)} sites with history)")
    
    # 导出标准定义
    with open(EXPORTS_DIR / 'grading_standard.json', 'w', encoding='utf-8') as f:
        json.dump(GRADING_STANDARD, f, ensure_ascii=False, indent=2)
    
    print(f"  ✓ grading_standard.json")

def generate_consistency_report(evaluations: List[Dict[str, Any]]) -> None:
    """生成一致性检查报告"""
    print("\n🔍 正在检查数据一致性...")
    
    inconsistencies = []
    
    for eval_data in evaluations:
        if 'original_grade' in eval_data and 'grade' in eval_data:
            if eval_data['original_grade'] != eval_data['grade']:
                inconsistencies.append({
                    "domain": eval_data.get('domain'),
                    "score": eval_data.get('score'),
                    "original_grade": eval_data['original_grade'],
                    "new_grade": eval_data['grade'],
                    "filename": eval_data.get('filename')
                })
    
    if inconsistencies:
        print(f"  ⚠️  发现 {len(inconsistencies)} 条等级不一致记录:")
        for item in inconsistencies[:10]:  # 只显示前10条
            print(f"    - {item['domain']}: {item['score']}分 "
                  f"({item['original_grade']} → {item['new_grade']})")
        if len(inconsistencies) > 10:
            print(f"    ... 还有 {len(inconsistencies) - 10} 条")
    else:
        print("  ✓ 所有数据等级一致")
    
    # 保存详细报告
    report = {
        "generated_at": datetime.now().isoformat(),
        "standard_version": GRADING_STANDARD['version'],
        "total_evaluations": len(evaluations),
        "inconsistencies_found": len(inconsistencies),
        "inconsistencies": inconsistencies
    }
    
    with open(EXPORTS_DIR / 'consistency_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

def generate_statistics(sites_data: Dict[str, Dict[str, Any]]) -> None:
    """生成统计报告"""
    print("\n📈 统计数据:")
    
    total_sites = len(sites_data)
    total_evaluations = sum(len(s['evaluations']) for s in sites_data.values())
    
    # 等级分布
    grade_counts = defaultdict(int)
    type_counts = defaultdict(int)
    scores = []
    
    for site in sites_data.values():
        for eval_data in site['evaluations']:
            grade = eval_data.get('grade', 'C')
            grade_counts[grade] += 1
            
            site_type = eval_data.get('site_type', 'unknown')
            type_counts[site_type] += 1
            
            if 'score' in eval_data:
                scores.append(eval_data['score'])
    
    print(f"  总网站数: {total_sites}")
    print(f"  总评测数: {total_evaluations}")
    print(f"  平均评测次数: {total_evaluations / total_sites:.1f}")
    
    if scores:
        print(f"  平均分数: {sum(scores) / len(scores):.1f}")
    
    print(f"\n  等级分布 (标准化后):")
    for grade in ['S', 'A', 'B', 'C']:
        count = grade_counts.get(grade, 0)
        pct = (count / len(scores) * 100) if scores else 0
        print(f"    {grade}级: {count:4d} ({pct:5.1f}%)")
    
    print(f"\n  网站类型分布:")
    for site_type, count in sorted(type_counts.items(), key=lambda x: -x[1])[:5]:
        print(f"    {site_type}: {count}")

def main():
    """主函数"""
    print("="*60)
    print("🚀 OpenAIX 数据标准化 v2.0")
    print("="*60)
    print(f"\n评分标准: {GRADING_STANDARD['name']}")
    print(f"  S级: {GRADING_STANDARD['thresholds']['S']['min']}+ 分")
    print(f"  A级: {GRADING_STANDARD['thresholds']['A']['min']}-{GRADING_STANDARD['thresholds']['A']['max']} 分")
    print(f"  B级: {GRADING_STANDARD['thresholds']['B']['min']}-{GRADING_STANDARD['thresholds']['B']['max']} 分")
    print(f"  C级: 0-{GRADING_STANDARD['thresholds']['C']['max']} 分")
    
    # 1. 加载所有评测数据
    evaluations = load_all_evaluations()
    
    # 2. 按网站聚合
    sites_data = aggregate_by_site(evaluations)
    
    # 3. 检查一致性
    generate_consistency_report(evaluations)
    
    # 4. 生成统计
    generate_statistics(sites_data)
    
    # 5. 生成导出数据
    generate_exports(sites_data)
    
    print("\n" + "="*60)
    print("✅ 数据标准化完成!")
    print("="*60)
    print(f"\n导出文件:")
    print(f"  📄 {EXPORTS_DIR}/rankings_current.json")
    print(f"  📄 {EXPORTS_DIR}/sites_index.json")
    print(f"  📄 {EXPORTS_DIR}/grading_standard.json")
    print(f"  📄 {EXPORTS_DIR}/consistency_report.json")

if __name__ == '__main__':
    main()
