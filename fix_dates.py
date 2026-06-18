#!/usr/bin/env python3
"""修复article_publish_dates.py格式错误"""
import re

filepath = 'article_publish_dates.py'

with open(filepath, 'r') as f:
    content = f.read()

# 找到字典结束位置
lines = content.split('\n')
dict_end = None
for i, line in enumerate(lines):
    if line.strip() == '}':
        dict_end = i
        break

if dict_end is None:
    print("❌ 未找到字典结束符}")
    exit(1)

# 检查字典外面是否有日期
outside_dates = []
for i, line in enumerate(lines[dict_end + 1:], start=dict_end + 1):
    stripped = line.strip()
    if stripped and "'" in stripped and ':' in stripped and '2026' in stripped:
        outside_dates.append((i + 1, stripped))

if outside_dates:
    print(f"⚠️ 发现 {len(outside_dates)} 个日期在字典外面:")
    for line_num, date_line in outside_dates:
        print(f"  行{line_num}: {date_line}")
    
    # 移除字典外面的日期
    new_lines = lines[:dict_end + 1]
    
    # 在}之前添加日期
    for _, date_line in outside_dates:
        kw = date_line.rstrip(',')
        new_lines.append(f"    {kw},")
    
    # 添加}
    new_lines.append("}")
    
    # 添加后续内容
    for i, line in enumerate(lines[dict_end + 1:], start=dict_end + 1):
        stripped = line.strip()
        if not (stripped and "'" in stripped and ':' in stripped and '2026' in stripped):
            new_lines.append(line)
    
    with open(filepath, 'w') as f:
        f.write('\n'.join(new_lines))
    
    print("✅ 已修复日期格式")
else:
    print("✅ 日期格式正确")
