#!/usr/bin/env python3
"""Automated quality check for all FoneClaw articles."""
import os
import re
import sys

os.chdir('/home/administrator/clawfone-v2')

# Check all batch files
batch_files = sorted([f for f in os.listdir('.') if f.startswith('articles_batch') and f.endswith('.py')])

print("=" * 70)
print("  FoneClaw 文章自动化质量检查")
print("=" * 70)
print()

total_articles = 0
issues = []

for batch_file in batch_files:
    try:
        ns = {}
        exec(open(batch_file).read(), ns)
        batch = ns.get('BATCH', [])
    except Exception as e:
        issues.append(f"❌ {batch_file}: 语法错误 - {e}")
        continue
    
    for item in batch:
        if len(item) < 6:
            issues.append(f"❌ {batch_file}: {item[0]} - 字段不足6个")
            continue
        
        slug = item[0]
        title = item[1]
        meta = item[2]
        sections = item[5]
        total_articles += 1
        
        full_text = ' '.join(b for _, b in sections)
        
        # 1. Title length
        if len(title) > 60:
            issues.append(f"⚠️ {slug}: Title超60字符 ({len(title)})")
        
        # 2. Meta length
        if len(meta) < 120 or len(meta) > 160:
            issues.append(f"⚠️ {slug}: Meta长度异常 ({len(meta)}字符)")
        
        # 3. Banned words
        banned = ['utilize', 'furthermore', 'robust', 'seamlessly', 'incredibly', 
                  'empower', 'leverage', 'cutting-edge', 'unparalleled', 'revolutionary']
        found_banned = [w for w in banned if w in full_text.lower()]
        if found_banned:
            issues.append(f"❌ {slug}: 禁用词 {found_banned}")
        
        # 4. E-E-A-T
        eeat_patterns = ['based on', 'our testing', 'our experience', 'our benchmark',
                        'we tested', 'foneclaw data', 'our analysis']
        has_eeat = any(p in full_text.lower() for p in eeat_patterns)
        if not has_eeat:
            issues.append(f"⚠️ {slug}: 缺少E-E-A-T")
        
        # 5. MiMo attribution (首次标注Xiaomi即可)
        mimo_sentences = [s for s in re.split(r'\.', full_text) if 'mimo' in s.lower()]
        if mimo_sentences:
            first_mention = mimo_sentences[0].strip()
            if 'xiaomi' not in first_mention.lower():
                issues.append(f"⚠️ {slug}: MiMo首次提及未标注Xiaomi")
            # 检查是否有错误归属
            for s in mimo_sentences:
                if 'foneclaw' in s.lower() and ('own' in s.lower() or 'our' in s.lower()):
                    issues.append(f"❌ {slug}: MiMo错误归属FoneClaw - {s[:50]}...")
        
        # 6. FoneClaw independence
        if 'foneclaw' in full_text.lower():
            if 'independent' not in full_text.lower():
                issues.append(f"⚠️ {slug}: FoneClaw未标注independent")
        
        # 7. FAQ format (必须使用Q:/A:格式)
        faq_sections = [(sub, body) for sub, body in sections if 'FAQ' in sub or 'faq' in sub.lower()]
        for sub, body in faq_sections:
            if '**' in body:
                issues.append(f"❌ {slug}: FAQ使用**加粗**格式（应使用Q:/A:）")
            elif 'Q:' in body and 'A:' in body:
                # 验证Q:A:格式是否正确
                q_count = body.count('Q:')
                a_count = body.count('A:')
                if q_count != a_count:
                    issues.append(f"⚠️ {slug}: FAQ的Q:A:数量不匹配 (Q:{q_count} A:{a_count})")
            elif '1.' in body or '2.' in body:
                issues.append(f"❌ {slug}: FAQ使用数字编号格式（应使用Q:/A:）")
            else:
                issues.append(f"⚠️ {slug}: FAQ格式不明")
        
        # 8. Section count
        if len(sections) < 5:
            issues.append(f"⚠️ {slug}: 章节太少 ({len(sections)}个)")
        
        # 9. Word count
        total_words = sum(len(b.split()) for _, b in sections)
        if total_words < 500:
            issues.append(f"⚠️ {slug}: 字数太少 ({total_words}词)")
        
        # 10. Keyword index for auto-linking
        # 内链通过article_keywords_data.py + _auto_link_keywords()自动注入
        # 不需要在batch源码中写href
        pass  # 内链由build系统自动处理

# Summary
print(f"检查完成: {total_articles}篇文章")
print()

if issues:
    print(f"发现 {len(issues)} 个问题:")
    print("-" * 70)
    for issue in issues:
        print(f"  {issue}")
    print("-" * 70)
    
    errors = [i for i in issues if i.startswith("❌")]
    warnings = [i for i in issues if i.startswith("⚠️")]
    
    print(f"\n  ❌ 错误: {len(errors)}")
    print(f"  ⚠️ 警告: {len(warnings)}")
else:
    print("✅ 全部通过，无问题！")

print()
print("=" * 70)
