#!/usr/bin/env python3
"""
article_keywords_data.py 格式验证和修复脚本
确保所有关键词都在字典里面
"""
import os
import re

def validate_and_fix():
    filepath = '/home/administrator/clawfone-v2/article_keywords_data.py'
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # 检查是否有关键词在字典外面
    # 匹配 } 后面还有 'slug': [...] 的情况
    pattern = r'\}\s*\n\s*#.*\n\s*\'[^\']+\':\s*\[[^\]]+\]'
    matches = re.findall(pattern, content)
    
    if matches:
        print(f"⚠️ 发现 {len(matches)} 个关键词在字典外面，正在修复...")
        
        # 修复：将外面的关键词移到字典里面
        for match in matches:
            # 提取关键词行
            kw_line = re.search(r'#.*\n\s*(\'[^\']+\':\s*\[[^\]]+\])', match)
            if kw_line:
                kw_text = kw_line.group(1)
                # 移除外面的关键词
                content = content.replace(match, '}')
                # 添加到字典里面
                content = content.replace('}\n', f'    {kw_text},\n}}\n')
        
        with open(filepath, 'w') as f:
            f.write(content)
        
        print("✅ 修复完成")
    else:
        print("✅ 格式正确，所有关键词都在字典里面")

if __name__ == '__main__':
    validate_and_fix()
