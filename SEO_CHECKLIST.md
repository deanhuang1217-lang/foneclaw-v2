# FoneClaw SEO 文章质量检查清单

## 一、SEO基础检查

| # | 检查项 | 要求 |
|---|--------|------|
| 1 | Title 标题 | ≤ 60字符，包含主关键词 |
| 2 | Meta Description | 120-160字符，包含关键词 |
| 3 | URL Slug | 简洁，包含关键词，用连字符 |
| 4 | Canonical URL | 指向正确URL |
| 5 | OG图片 | 已配置，尺寸1200x630 |

## 二、内容质量检查

| # | 检查项 | 要求 |
|---|--------|------|
| 6 | 字数 | 1500-3000词（按类型） |
| 7 | 段落结构 | 每section 3-4段，每段60-100词 |
| 8 | Section结构 | 每200-300词一个小标题 |
| 9 | 禁用词 | 24个禁用词=0 |
| 10 | 可读性 | 短句为主，第二人称"you" |

## 三、E-E-A-T 检查

| # | 检查项 | 要求 |
|---|--------|------|
| 11 | E-E-A-T数量 | ≥ 3处，第1section开头必须有 |
| 12 | E-E-A-T类型 | 数据/测试/经验/分析引用 |
| 13 | 具体数据 | ≥ 3个具体数字 |

## 四、内链检查

| # | 检查项 | 要求 |
|---|--------|------|
| 14 | 内链数量 | 8-15条（按字数） |
| 15 | 内链质量 | 同关键词/目标只链一次 |
| 16 | 内链实现 | article_keywords_data.py自动注入 |

## 五、FAQ 检查

| # | 检查项 | 要求 |
|---|--------|------|
| 17 | FAQ格式 | "Frequently Asked Questions" + Q:/A: |
| 18 | FAQ质量 | 4-5问题，40-60词答案 |

## 六、图片检查

| # | 检查项 | 要求 |
|---|--------|------|
| 19 | Hero图片 | 1376x768，JPG quality=95 |
| 20 | Alt文本 | 描述性，包含关键词 |
| 21 | 图片加载 | 可正常加载，<500KB |

## 七、社交分享检查

| # | 检查项 | 要求 |
|---|--------|------|
| 22 | OG标签 | title/description/image/url |
| 23 | Twitter Card | card/title/description/image |
| 24 | 分享文案 | ≤280字符，吸引点击 |

## 八、移动端检查

| # | 检查项 | 要求 |
|---|--------|------|
| 25 | 移动端适配 | 响应式设计 |
| 26 | 移动端内容 | 与桌面端一致 |

## 九、技术SEO检查

| # | 检查项 | 要求 |
|---|--------|------|
| 27 | 页面加载 | 200状态码 |
| 28 | Sitemap | URL在sitemap.xml中 |
| 29 | Robots.txt | 未被阻止 |
| 30 | 结构化数据 | JSON-LD Article类型 |

## 十、作者页检查

| # | 检查项 | 要求 |
|---|--------|------|
| 31 | 作者页显示 | 有标题和摘要，按日期倒序 |
| 32 | 作者信息 | X账号@huangda_huang |

## 十一、Resources页检查

| # | 检查项 | 要求 |
|---|--------|------|
| 33 | 分类正确 | cat_map有映射 |
| 34 | 文章显示 | 有标题和摘要 |

## 十二、部署检查

| # | 检查项 | 要求 |
|---|--------|------|
| 35 | 文件完整性 | HTML+resources+author+sitemap+图片 |
| 36 | 线上验证 | 可访问/内链/图片/FAQ |

---

## 十三、Google Analytics 代码检查

| # | 检查项 | 要求 |
|---|--------|------|
| 37 | GA4 代码 | 已配置 Google Analytics 4 |
| 38 | GA Measurement ID | 正确的 G-XXXXXXXXXX ID |
| 39 | GA 代码位置 | 在 <head> 中，所有页面一致 |
| 40 | GA 事件跟踪 | 页面浏览、滚动、点击等事件 |
| 41 | GTM 代码 | 如使用 GTM，代码已配置 |
| 42 | GA 数据验证 | GA 后台可收到数据 |

### GA 代码检查命令

```bash
# 检查GA4代码是否存在
grep -o 'G-[A-Z0-9]*' article.html

# 检查gtag.js
grep 'gtag.js' article.html

# 检查GA Measurement ID
grep -o 'G-[A-Z0-9]\{7,\}' article.html

# 检查所有页面GA代码一致性
for f in *.html; do echo "$f:"; grep -o 'G-[A-Z0-9]*' $f | head -1; done
```

---

## 十四、页面性能检查

| # | 检查项 | 要求 |
|---|--------|------|
| 43 | 页面加载速度 | < 3秒 (移动端) |
| 44 | Core Web Vitals | LCP < 2.5s, FID < 100ms, CLS < 0.1 |
| 45 | 图片优化 | WebP格式，懒加载 |
| 46 | CSS/JS 压缩 | 已压缩，无冗余代码 |
| 47 | 缓存策略 | 静态资源有缓存头 |
| 48 | HTTPS | 全站HTTPS |

### 性能检查工具

```bash
# 使用PageSpeed Insights
curl "https://pagespeed.web.dev/analysis?url=https://www.foneclaw.ai/article.html"

# 检查HTTPS
curl -sI "https://www.foneclaw.ai/article.html" | grep -i "strict-transport"
```

---

## 十五、结构化数据检查

| # | 检查项 | 要求 |
|---|--------|------|
| 49 | JSON-LD 类型 | Article / BlogPosting |
| 50 | headline | 与Title一致 |
| 51 | datePublished | 正确的发布日期 |
| 52 | dateModified | 正确的修改日期 |
| 53 | author | 作者信息正确 |
| 54 | image | 文章图片URL |
| 55 | publisher | FoneClaw信息 |

### 结构化数据检查命令

```bash
# 提取JSON-LD
grep -o '<script type="application/ld+json">[^<]*</script>' article.html

# 验证结构化数据
curl "https://search.google.com/test/rich-results?url=https://www.foneclaw.ai/article.html"
```

---

## 十六、日期和时间检查

| # | 检查项 | 要求 |
|---|--------|------|
| 56 | datePublished | 存储在 article_publish_dates.py |
| 57 | dateModified | 使用 datetime.date.today() |
| 58 | 展示日期 | 使用 dateModified（用户可见） |
| 59 | 日期格式 | ISO 8601 (YYYY-MM-DD) |

---

## 十七、CTA 和转化检查

| # | 检查项 | 要求 |
|---|--------|------|
| 60 | CTA 按钮 | 有明确的行动号召 |
| 61 | CTA 位置 | 文章开头和结尾 |
| 62 | CTA 文案 | 吸引点击，与内容相关 |
| 63 | 下载链接 | 如有，链接正常 |

---

## 十八、外部链接检查

| # | 检查项 | 要求 |
|---|--------|------|
| 64 | 外部链接数量 | 2-5个权威来源 |
| 65 | 外部链接质量 | 高权重网站 |
| 66 | 外部链接属性 | target="_blank" rel="noopener" |
| 67 | 链接有效性 | 无死链 |

### 外部链接检查命令

```bash
# 提取外部链接
grep -o 'href="https://[^"]*"' article.html | grep -v "foneclaw.ai"

# 检查死链
curl -s -o /dev/null -w "%{http_code}" "https://external-link.com"
```

---

## 十九、无障碍访问检查

| # | 检查项 | 要求 |
|---|--------|------|
| 68 | 图片 Alt | 所有图片有描述性alt |
| 69 | 标题层级 | H1-H6 正确嵌套 |
| 70 | 颜色对比度 | 符合 WCAG AA 标准 |
| 71 | 键盘导航 | 可用键盘访问所有元素 |
| 72 | ARIA 标签 | 交互元素有 ARIA 标签 |

---

## 二十、安全性检查

| # | 检查项 | 要求 |
|---|--------|------|
| 73 | SSL 证书 | 有效，未过期 |
| 74 | 混合内容 | 无 HTTP 资源 |
| 75 | CSP 头 | 已配置 Content-Security-Policy |
| 76 | XSS 防护 | 已配置 X-XSS-Protection |

---

## 二十一、监控和备份

| # | 检查项 | 要求 |
|---|--------|------|
| 77 | 网站监控 | 已配置 Uptime 监控 |
| 78 | 错误监控 | 已配置 404/500 错误监控 |
| 79 | 备份策略 | 定期备份，可恢复 |
| 80 | 日志记录 | 访问日志和错误日志 |

---

## 快速检查命令

### SEO 基础检查

```bash
# 检查Title长度
grep -o '<title>[^<]*</title>' article.html

# 检查Meta长度
grep -o '<meta name="description" content="[^"]*"' article.html

# 检查禁用词
grep -i 'utilize\|furthermore\|robust\|seamlessly\|navigate' article.html

# 检查E-E-A-T
grep -ci 'based on our\|our testing\|our experience' article.html

# 检查段落数
grep -c '<p>' article.html

# 检查内链数
grep -o 'href="/[^"]*\.html"' article.html | wc -l

# 检查FAQ格式
grep -c 'faq-q' article.html
```

### GA 代码检查

```bash
# 检查GA4代码
grep -o 'G-[A-Z0-9]*' article.html

# 检查gtag.js
grep 'gtag.js' article.html

# 检查所有页面GA代码
for f in *.html; do echo "$f:"; grep -o 'G-[A-Z0-9]*' $f | head -1; done
```

### 结构化数据检查

```bash
# 提取JSON-LD
grep -o '<script type="application/ld+json">[^<]*</script>' article.html

# 检查日期
grep -o '"datePublished":"[^"]*"' article.html
grep -o '"dateModified":"[^"]*"' article.html
```

### 性能检查

```bash
# 检查HTTPS
curl -sI "https://www.foneclaw.ai/article.html" | grep -i "strict-transport"

# 检查页面大小
curl -s "https://www.foneclaw.ai/article.html" | wc -c

# 检查图片数量
grep -c '<img' article.html
```

---

## Checklist 更新记录

- 2026-05-22: 初始版本，36项
- 2026-05-22: 添加 GA 代码检查（第13节）
- 2026-05-22: 添加页面性能检查（第14节）
- 2026-05-22: 添加结构化数据检查（第15节）
- 2026-05-22: 添加日期和时间检查（第16节）
- 2026-05-22: 添加 CTA 和转化检查（第17节）
- 2026-05-22: 添加外部链接检查（第18节）
- 2026-05-22: 添加无障碍访问检查（第19节）
- 2026-05-22: 添加安全性检查（第20节）
- 2026-05-22: 添加监控和备份检查（第21节）
