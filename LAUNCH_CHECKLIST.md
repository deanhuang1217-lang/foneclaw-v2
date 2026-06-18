# FoneClaw Website — 上线检查清单 v2.0

*基于 2026年3月 Google 核心更新 最佳实践*

---

## 一、公共组件一致性

- [ ] **导航栏**：所有页面使用同一组件，链接数量、顺序、文案一致
- [ ] **导航高亮**：当前页面对应的导航项高亮，其他不高亮
- [ ] **Hamburger 按钮**：所有页面移动端都有汉堡菜单
- [ ] **Footer**：所有页面使用同一组件，列数、链接、文案一致
- [ ] **Footer 链接**：无 href="#" 死链，所有链接指向正确页面
- [ ] **回到顶部按钮**：所有页面都有，样式和行为一致
- [ ] **新增页面**：必须通过公共组件生成，禁止独立手写 HTML

## 二、分析工具覆盖

- [ ] **Google Analytics**：所有页面安装 GA 代码（G-0PHX8QGTBF）
- [ ] **GA 代码位置**：在 <head> 内，页面加载即触发
- [ ] **Google Search Console**：已验证域名所有权
- [ ] **Sitemap 已提交**：Search Console 中显示已提交的 sitemap

## 三、资源优化

- [ ] **图片压缩**：所有图片经过无损压缩
- [ ] **图片格式**：优先 WebP，其次 JPEG，避免 PNG（除非需要透明）
- [ ] **图片尺寸**：og-image 1200x630 < 1MB
- [ ] **base64 内嵌**：仅用于 favicon 和小图标，大图必须外部引用
- [ ] **页面体积**：首页 < 500KB，文章页 < 300KB
- [ ] **字体加载**：使用 preconnect + display=swap

## 四、SEO 规范（每个页面）

### 4.1 Meta 标签
- [ ] **title**：唯一，含品牌名，60 字符内
- [ ] **meta description**：唯一，120-160 字符，含关键词，有行动号召
- [ ] **meta robots**：index, follow
- [ ] **canonical URL**：带 .html 后缀，与 og:url 一致
- [ ] **viewport**：width=device-width, initial-scale=1.0

### 4.2 Open Graph & Twitter Card
- [ ] og:type, og:title, og:description, og:url, og:image, og:site_name
- [ ] twitter:card = summary_large_image

### 4.3 结构化数据
- [ ] JSON-LD 存在（SoftwareApplication / TechArticle / FAQPage / CollectionPage）
- [ ] BreadcrumbList 正确（层级、URL 带 .html）

### 4.4 内容结构
- [ ] H1 唯一
- [ ] 标题层级正确（H1→H2→H3，不跳级）
- [ ] 图片有 alt 属性
- [ ] 内部链接带 .html 后缀
- [ ] 无 href="#" 死链接

### 4.5 Sitemap & Robots
- [ ] sitemap.xml 包含所有页面 URL
- [ ] 无重复 URL
- [ ] robots.txt 允许爬取

## 五、2026 核心更新新规 ⭐

### 5.1 信息增益（Information Gain）
Google 显式衡量内容相对于已有排名结果提供了多少**真正的新知识**。

- [ ] 每篇文章至少包含1个独特元素：原创数据、第一手测试、真实用户场景
- [ ] 写作前检查 TOP5 结果，文章必须包含它们都没有的内容
- [ ] 不要仅仅重新表述竞争对手内容
- [ ] 优先：真实产品使用数据、具体基准测试、独特用户场景
- [ ] 避免：通用的"10大好处"列表，换个产品名也能用的内容

### 5.2 用户交互模式评分（User Interaction Pattern Scoring）
Google 分析三种点击后行为：回滚率、对比跳出、摘要满意度。

- [ ] 前200字内直接回答主要查询（满足摘要扫描者）
- [ ] 使用清晰 H2 结构，让用户无需跳出就能找到答案
- [ ] 包含可操作的要点，不仅仅是信息堆砌
- [ ] FAQ 答案真正有用（40-60字，具体，不模糊）

### 5.3 E-E-A-T 作者权威性
Google 交叉验证作者专业度与内容复杂度。

- [ ] 文章引用具体专业经验（"在我们的测试中..."）
- [ ] 包含可信归因（链接到官方文档，引用真实产品能力）
- [ ] 避免在网站没有明显权威的领域发布内容
- [ ] 不使用"编辑团队"等匿名署名

### 5.4 GEO（生成式引擎优化）
LLM 从 16-36 个不同来源提取信息。被 AI 答案引用是新的 SEO 目标。

- [ ] 内容结构清晰，有可引用的陈述句
- [ ] 使用确定性措辞："FoneClaw 支持 50+ 语音命令"（不是"有很多语音命令可用"）
- [ ] 包含具体数字、事实、结构化数据
- [ ] FAQ 用 "Q: A:" 格式便于 LLM 提取
- [ ] 确保内容出现在第三方网站上

### 5.5 主题一致性（Topical Coherence）
域名级主题权威 > 页面级关键词优化。

- [ ] 所有内容在核心领域内：语音控制、Android 自动化、免手操作、无障碍
- [ ] 不为搜索量写无关的广覆盖内容
- [ ] 构建内容集群：互链相关文章
- [ ] 深度优先于广度

## 六、文案质量

### 6.1 逻辑性
- [ ] 每段文字有明确的信息增量
- [ ] 说服逻辑：痛点 → 方案 → 证据 → 行动
- [ ] 数据具体：用数字代替模糊描述

### 6.2 去 AI 味
- [ ] 禁用词检查：
  - 中文：赋能、引领、助力、携手、打造、一站式、全方位
  - 英文：delve, leverage, utilize, cutting-edge, seamless, revolutionize, harness, unlock, embark, robust, innovative, game-changer, absolutely, furthermore, moreover, additionally, incredibly, fundamentally, unparalleled, empower
  - 句式："Here's the thing:", "But there's a catch", "Let me explain", "Now you might be wondering", "The bottom line?", "Think about it this way", "We have all been there", "Imagine your/this/that", "in this article", "changes this dynamic entirely"
- [ ] 句式自然：短句为主，避免长复合句
- [ ] 人称统一：第二人称"你"
- [ ] 有观点、有态度
- [ ] Bucket Brigades 每篇最多1-2处，不重复

### 6.3 CTA（行动号召）
- [ ] 每个页面有明确的 CTA
- [ ] CTA 文案具体
- [ ] CTA 按钮颜色醒目，位置合理

## 七、安全性

- [ ] HTTPS 有效
- [ ] 无敏感信息暴露在前端代码
- [ ] 外部链接加 rel="noopener"

## 八、性能

- [ ] 首屏加载 < 3 秒
- [ ] Core Web Vitals 达标（LCP < 2.5s, FID < 100ms, CLS < 0.1）

## 九、404 页面

- [ ] 自定义 404 页面存在
- [ ] 不存在的 URL 返回 404 状态码

---

## 快速检查流程

```
1. build_multi.py 构建 → 检查无报错
2. 本地预览 → 检查 nav/footer/back-to-top 一致性
3. grep 检查：
   grep -r 'href="#"' *.html                    → 不应有死链
   grep -r 'G-0PHX8QGTBF' *.html                → 全部有 GA
   grep -ri 'delve\|leverage\|utilize\|robust\|absolutely\|furthermore' *.html → 不应有 AI 味
   grep -r 'canonical' *.html                    → 全部带 .html
4. 复制到 upload 文件夹
5. FileZilla 上传
6. 线上测试
```

---

*v2.0 — 2026-05-12 — 新增 2026 核心更新5条新规*
*v1.0 — 2026-05-11 — 初始版本*
