#!/usr/bin/env python3
"""
OpenAIX Website List Generator
Combines Majestic Million Top 5000 + Industry Websites + Community Slots
Target: 10,000 websites total
"""

import re
from collections import defaultdict

def extract_domains_from_file(filepath):
    """Extract domain names from a file, one per line"""
    domains = set()
    try:
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                # Skip empty lines, comments, and section headers
                if not line or line.startswith('#') or line.startswith('##'):
                    continue
                # Skip category count markers like "(500个)"
                if '个' in line or '(' in line:
                    continue
                # Extract domain from URL or plain domain
                if line.startswith('http://') or line.startswith('https://'):
                    # Extract domain from URL
                    domain = line.split('//')[1].split('/')[0].strip()
                else:
                    domain = line.strip()
                
                # Clean up domain
                domain = domain.lower().strip()
                # Remove www. prefix
                if domain.startswith('www.'):
                    domain = domain[4:]
                
                if domain and '.' in domain:
                    domains.add(domain)
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    return domains

def parse_industry_websites(filepath):
    """Parse industry websites organized by category"""
    categories = defaultdict(set)
    current_category = None
    
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            
            # Category header
            if line.startswith('# ') and ' - ' in line:
                current_category = line.replace('# ', '').split(' - ')[0].strip()
                continue
            
            # Subcategory header
            if line.startswith('## '):
                continue
            
            # Skip empty lines
            if not line:
                continue
            
            # Extract domain
            if line.startswith('http://') or line.startswith('https://'):
                domain = line.split('//')[1].split('/')[0].strip()
            else:
                domain = line.strip()
            
            # Clean up
            domain = domain.lower().strip()
            if domain.startswith('www.'):
                domain = domain[4:]
            
            if domain and '.' in domain and current_category:
                categories[current_category].add(domain)
    
    return categories

def is_valid_domain(domain):
    """Basic domain validation"""
    if not domain or len(domain) > 253:
        return False
    # Basic pattern: contains at least one dot, alphanumeric and hyphens only
    pattern = r'^[a-z0-9]([a-z0-9\-]{0,61}[a-z0-9])?(\.[a-z0-9]([a-z0-9\-]{0,61}[a-z0-9])?)+$'
    return bool(re.match(pattern, domain.lower()))

def main():
    print("=" * 60)
    print("OpenAIX Website List Generator")
    print("=" * 60)
    
    # 1. Read existing websites (to check for duplicates)
    print("\n[1] Reading existing websites.txt...")
    existing_domains = extract_domains_from_file('websites.txt')
    print(f"    Found {len(existing_domains)} existing domains")
    
    # 2. Read Majestic Million Top 5000
    print("\n[2] Reading Majestic Million Top 5000...")
    majestic_domains = extract_domains_from_file('majestic_top5000.txt')
    print(f"    Found {len(majestic_domains)} domains from Majestic")
    
    # 3. Parse industry websites
    print("\n[3] Parsing industry websites...")
    industry_categories = parse_industry_websites('industry_websites_raw.txt')
    industry_domains = set()
    category_counts = {}
    for category, domains in industry_categories.items():
        category_counts[category] = len(domains)
        industry_domains.update(domains)
    print(f"    Found {len(industry_domains)} industry domains")
    for cat, count in sorted(category_counts.items()):
        print(f"      - {cat}: {count}")
    
    # 4. Combine all sources
    print("\n[4] Combining and deduplicating...")
    all_domains = majestic_domains.union(industry_domains)
    
    # Filter valid domains
    valid_domains = {d for d in all_domains if is_valid_domain(d)}
    invalid_count = len(all_domains) - len(valid_domains)
    if invalid_count > 0:
        print(f"    Filtered out {invalid_count} invalid domains")
    
    # 5. Calculate statistics
    print("\n[5] Statistics:")
    print(f"    Majestic domains: {len(majestic_domains)}")
    print(f"    Industry domains: {len(industry_domains)}")
    print(f"    Combined (before dedup): {len(majestic_domains) + len(industry_domains)}")
    print(f"    Combined (after dedup): {len(valid_domains)}")
    
    # Overlap analysis
    overlap_majestic_industry = majestic_domains.intersection(industry_domains)
    print(f"    Overlap (Majestic ∩ Industry): {len(overlap_majestic_industry)}")
    
    overlap_existing = valid_domains.intersection(existing_domains)
    print(f"    Overlap with existing list: {len(overlap_existing)}")
    
    # New domains added
    new_domains = valid_domains - existing_domains
    print(f"    New domains to add: {len(new_domains)}")
    
    # 6. Sort and format domains
    print("\n[6] Sorting domains...")
    sorted_domains = sorted(valid_domains, key=lambda x: (x.split('.')[-1], x))
    
    # 7. Generate final list
    print("\n[7] Generating websites.txt...")
    
    header = f"""# OpenAIX 评测网站列表
# 数据来源: Majestic Million Top 5000 + 行业精选网站 + 社区提交位
# 更新时间: 2026-02-25
# 总计: {len(sorted_domains) + 1000} 个网站 (含1000个社区预留位)
# 
# 分类统计:
# - Majestic Million Top 5000: {len(majestic_domains)} 个
# - 行业网站: {len(industry_domains)} 个  
# - 去重后总计: {len(sorted_domains)} 个
# - 社区预留位: 1000 个
#
"""
    
    with open('websites_expanded.txt', 'w') as f:
        f.write(header)
        f.write("\n")
        
        # Write sorted domains
        for domain in sorted_domains:
            f.write(f"https://{domain}\n")
        
        # Add community submission markers
        f.write("\n# === 社区提交位 (Community Submissions) - 1000 slots reserved ===\n")
        f.write("# 请通过 GitHub Issues 或 Discord 提交网站建议\n")
        for i in range(1, 1001):
            f.write(f"# COMMUNITY_SLOT_{i:04d}\n")
    
    print(f"    Written to websites_expanded.txt")
    
    # 8. Generate detailed report
    print("\n[8] Generating report...")
    
    report = f"""
{'='*60}
OpenAIX Website Expansion Report
{'='*60}

一、数据源统计
--------------
• Majestic Million Top 5000: {len(majestic_domains):,} 个
• 行业精选网站: {len(industry_domains):,} 个
  - 金融/银行: {category_counts.get('金融/银行 - Finance/Banking', 0):,} 个
  - 教育/学术: {category_counts.get('教育/学术 - Education/Academic', 0):,} 个
  - 电商/零售: {category_counts.get('电商/零售 - E-commerce/Retail', 0):,} 个
  - 科技/SaaS: {category_counts.get('科技/SaaS - Technology/SaaS', 0):,} 个
  - 政府/公共: {category_counts.get('政府/公共 - Government/Public', 0):,} 个
  - 媒体/新闻: {category_counts.get('媒体/新闻 - Media/News', 0):,} 个
  - 社交媒体: {category_counts.get('社交媒体 - Social Media', 0):,} 个
  - 其他补充: {category_counts.get('其他补充 - Others', 0):,} 个

二、合并统计
------------
• 合并前总计: {len(majestic_domains) + len(industry_domains):,} 个
• Majestic 与行业网站重叠: {len(overlap_majestic_industry):,} 个
• 去重后总数: {len(valid_domains):,} 个

三、与现有列表对比
------------------
• 现有列表: {len(existing_domains):,} 个
• 新列表去重后: {len(valid_domains):,} 个
• 重叠网站: {len(overlap_existing):,} 个
• 新增网站: {len(new_domains):,} 个

四、最终构成
------------
• 现有评测网站: {len(existing_domains):,} 个
• 本次新增网站: {len(new_domains):,} 个
• 去重后总网站: {len(valid_domains):,} 个
• 社区预留位: 1,000 个
• 总计: {len(valid_domains) + 1000:,} 个

五、评测完成时间估算
--------------------
按每小时评测速度计算:
• 保守速度 (5个/小时): {(len(valid_domains) + 1000) / 5:,.0f} 小时 ≈ {(len(valid_domains) + 1000) / 5 / 24:.1f} 天
• 中等速度 (10个/小时): {(len(valid_domains) + 1000) / 10:,.0f} 小时 ≈ {(len(valid_domains) + 1000) / 10 / 24:.1f} 天
• 快速 (15个/小时): {(len(valid_domains) + 1000) / 15:,.0f} 小时 ≈ {(len(valid_domains) + 1000) / 15 / 24:.1f} 天

六、建议
--------
1. 优先评测 Majestic Top 1000（流量大、影响广）
2. 分行业批次进行，确保各行业均衡覆盖
3. 预留的1000个社区位可根据用户反馈动态添加
4. 建议设置自动化评测流水线以提高效率

{'='*60}
"""
    
    with open('website_expansion_report.txt', 'w') as f:
        f.write(report)
    
    print(report)
    print("\n✅ 扩展完成！")
    print("   - websites_expanded.txt: 最终网站列表")
    print("   - website_expansion_report.txt: 详细报告")

if __name__ == '__main__':
    main()
