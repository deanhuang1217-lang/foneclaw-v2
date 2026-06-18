# FoneClaw Website Development Rules

> 铁律：所有规则必须遵守，违反会导致功能丢失或返工。
> 最后更新：2026-05-14

---

## 一、铁律（违反会直接丢功能）

| # | 规则 | 原因 |
|---|------|------|
| 1 | **所有功能必须写在源码里**（build_multi.py / _components.py / _social_share.py / _style.css / articles_batch*.py），不能只改输出HTML | build会覆盖一切，改HTML白改 |
| 2 | **修改前必须先读最新版本** | 已因违反丢失功能多次（社区Facebook+SVG、首页链接、SEO优化） |
| 3 | **SEO修复必须在batch源数据做**（articles_batch*.py / batch6_data.json），不能改HTML输出 | build会覆盖 |
| 4 | **build_multi.py中URL_MAP值不能加.html后缀** | 既用于文件名（自动加.html）又用于canonical URL，加了会变xxx.html.html |
| 5 | **修改源码前必须先备份，项目结束后创建基线** | 修改前：cp file file.bak。项目结束后：将所有源码文件打包到batch_backups/YYYY-MM-DD_基线/，包括build_multi.py/_components.py/_social_share.py/_article_template.py/_style.css/articles_batch*.py/batch6_data.json/share_text_data.py/rebuild_cache.py/compress_images.py/seo_writing_spec.md |

---

## 二、产品/品牌规范

| # | 规则 | 说明 |
|---|------|------|
| 5 | **ClawFone = 硬件（龙虾手机），FoneClaw = 软件（Agent OS）** | 不要搞反 |
| 6 | **默认语言：英语** | language switcher已移除 |
| 7 | **所有app用美国案例** | iMessage, Amazon, DoorDash, Google Maps, Spotify, Uber |
| 8 | **紧急号码：911** | 不是110 |
| 9 | **单位：°F, miles** | 不是°C, km |
| 10 | **产品定价** | Free core forever + Pro $9.99/mo |
| 11 | **域名** | www.foneclaw.ai |

---

## 三、设计规范

| # | 规则 | 说明 |
|---|------|------|
| 12 | **暗色主题 + 青色强调色** | 背景#080c18，强调#00d4ff |
| 13 | **禁止红色字体** | 用户明确说红色让人不舒服 |
| 14 | **每个页面必须图文结合** | 不能只有文字 |
| 15 | **字体** | Space Grotesk（标题）+ Inter（正文），Google Fonts |
| 16 | **导航顺序** | Home → Features → Download → Resources → Community |
| 17 | **导航字体** | 14px / weight:500，hover和选中状态不变粗 |
| 18 | **内部链接必须带.html后缀** | 如 /features.html，不能写 /features |
| 19 | **Trust卡片对齐** | 标题顶部对齐 + 固定52px高度 |
| 20 | **Back-to-top箭头** | SVG箭头 + inline style（CSS class切换不可靠） |

### 配色方案

| 用途 | 颜色 |
|------|------|
| 标题H1/H2 | #f0f4f8 |
| 副标题H3 | #c9d1d9 |
| 正文 | #8b949e |
| 辅助文字 | #6e7681 |
| 强调色 | #00d4ff |
| 解决方案 | #3fb950 |
| 卡片背景 | #0d1117 |
| 主背景 | #080c18 |

---

## 四、SEO规范

| # | 规则 | 标准 |
|---|------|------|
| 21 | **SEO文章质量阈值** | 80分（满分100） |
| 22 | **禁用词** | utilize, furthermore, robust, additionally, fundamentally, seamlessly, incredibly, empower, leverage, cutting-edge, unparalleled, revolutionary |
| 23 | **关键词密度** | 1.0% - 1.8% |
| 24 | **Title长度** | ≤ 60字符（不含" - FoneClaw"后缀） |
| 25 | **Meta描述长度** | 120 - 160字符 |
| 26 | **E-E-A-T** | 每篇文章至少1处专业经验引用 |
| 27 | **写作规范文件** | seo_writing_spec.md（v3.0） |
| 28 | **sitemap.xml** | 必须包含所有页面URL（build_multi.py自动生成） |
| 29 | **robots.txt** | 必须白名单：facebookexternalhit / Googlebot / Twitterbot |
| 30 | **canonical标签** | 每个页面必须有，指向自身完整URL |
| 31 | **JSON-LD** | 文章页必须有Article类型的结构化数据 |

---

## 五、图片规范

| # | 规则 | 说明 |
|---|------|------|
| 28 | **图片压缩必须无损** | quality=100 |
| 29 | **页面图片标准** | 800×446（来自2026-05-12_1900） |
| 30 | **文章图片标准** | 1376×768（来自resources/） |
| 31 | **图片资源基准** | 以2026-05-12_1900为标准，不能用更模糊的版本 |
| 32 | **favicon** | 256×256用于网站icon，16×16用于base64嵌入HTML（1KB vs 160KB） |
| 33 | **Facebook OG图片** | og-image.png，256×256 |

### 图片lazy loading陷阱

首页/Features的img标签有 `loading="lazy"`，浏览器自动化工具初次检查时会报broken（naturalWidth=0），需要滚动到可视区域后才加载。**测试图片是否真的broken前，必须先滚动到底部再检查。**

---

## 六、部署规范

| # | 规则 | 说明 |
|---|------|------|
| 34 | **部署方式** | FTP（FileZilla手动上传） |
| 35 | **FTP服务器** | 44.224.204.0:2121, user: www_foneclaw_ai |
| 36 | **待发布文件** | 放 uploads/YYYY-MM-DD_HHMM/ |
| 37 | **发布后** | 建新文件夹，旧文件夹保留不删 |
| 38 | **Build命令** | `cd /home/administrator/clawfone-v2 && python3 build_multi.py` |
| 39 | **Cache重建** | `cd /home/administrator/clawfone-v2 && python3 rebuild_cache.py` |

---

## 七、社交/分享规范

| # | 规则 | 说明 |
|---|------|------|
| 40 | **Facebook分享只依赖OG标签** | quote参数无效，已移除 |
| 41 | **社媒平台** | Telegram, Discord, X, Facebook, 微信 |
| 42 | **Facebook页面** | facebook.com/foneclaw |
| 43 | **robots.txt白名单** | facebookexternalhit / Googlebot / Twitterbot |
| 44 | **Facebook OG缓存** | 文件大小变更后需在Debugger中Scrape Again，缓存24-48小时过期 |

---

## 八、工作流程规范

| # | 规则 | 说明 |
|---|------|------|
| 45 | **用户确认后才动手** | 问"能不能做"时先回答，确认后再动手 |
| 46 | **交付前自测** | 所有功能必须验证通过 |
| 47 | **改完必须全面测试** | 桌面端 + 移动端，不能只测改的部分 |
| 48 | **长任务主动汇报进度** | 每完成一步要汇报（✅/⏳），不能等全部做完才说 |
| 49 | **不要多轮确认** | 发现问题直接修，连续问"要我改吗？"会让人不耐烦 |
| 50 | **CSS问题** | 社媒分享/back-to-top CSS不能放在</style>外面 |

---

## 九、技术架构

### 文件结构

```
clawfone-v2/
├── build_multi.py          # 主构建脚本（生成32个HTML）
├── _components.py          # 公共组件（nav/footer/back_to_top/js/head/full_page）
├── _social_share.py        # 社媒分享组件（Facebook只用URL+OG标签）
├── _article_template.py    # 文章模板
├── _style.css              # 全局CSS
├── compress_images.py      # 图片压缩（quality=100）
├── rebuild_cache.py        # 缓存重建
├── seo_writing_spec.md     # SEO写作规范v3.0
├── articles_batch{1-5}.py  # 25篇文章源数据
├── batch6_data.json        # 额外文章数据
├── _build_cache.pkl        # 图片缓存（76张+16×16 favicon）
├── images/                 # 27张页面图片（800×446）
├── images/articles/        # 25张文章图片（1376×768）
├── favicon.png             # 256×256 网站icon
├── favicon_transparent.png # 256×256 RGBA透明背景版
├── favicon_small.png       # 16×16 用于base64嵌入
├── og-image.png            # Facebook OG图片
├── robots.txt              # 搜索引擎白名单
├── WEBSITE_RULES.md        # 本文件
└── *.html                  # 32个HTML文件
```

### 页面生成方式

| 页面类型 | 生成方式 | 函数 |
|----------|----------|------|
| index / features / community | html.append() + head() | 直接构建 |
| download / early-access / privacy / resources | full_page() | _components.py |
| 文章页（25篇） | _article_template.py | batch数据 + 模板 |

### OG标签

所有页面通过 `head()` 函数统一生成OG标签：
- og:type, og:title, og:description, og:url, og:image, og:site_name
- twitter:card, twitter:title, twitter:description, twitter:image

---

## 十、历史教训

| 事件 | 原因 | 教训 |
|------|------|------|
| 社区Facebook+SVG丢失 | build重建覆盖了手动改的HTML | 规则#1 |
| SEO优化全部丢失 | 改了HTML输出而非batch源数据 | 规则#3 |
| 首页链接丢失 | 用了旧版本的缓存 | 规则#2 |
| Facebook分享不显示 | quote参数无效，只依赖OG标签 | 规则#40 |
| Facebook返回403 | 缓存了旧的大文件响应 | 规则#44 |
| Back-to-top箭头消失 | CSS class切换不可靠 | 规则#20 |
| favicon太大（160KB） | 256×256 base64嵌入HTML | 规则#32 |
| 图片太糊 | quality=80有损压缩 | 规则#28 |
| Facebook JS函数换行符 | Python三引号中\n被解释为换行符 | 用\\\\n |

---

## 十一、社交账号

| 平台 | 链接 |
|------|------|
| Telegram | t.me/foneclaw |
| Discord | discord.gg/vQ65DUHucj |
| X/Twitter | x.com/FoneClaw001 |
| Facebook | facebook.com/foneclaw |
| Email | Feedback@foneclaw.ai |

---

## 十二、Google集成

| 项目 | 值 |
|------|-----|
| Google Analytics | G-0PHX8QGTBF |
| Google Apps Script | 表单提交endpoint（early-access页面用） |
| Google Search Console | 待验证域名所有权（需DNS TXT record） |

---

## 十三、内链管理规则（自动关键词链接）

### 原则
- 内链在**写作时规划**，不是事后注入
- 每篇文章选择3-5篇相关文章，将它们的索引关键词自然融入正文
- build时 `_auto_link_keywords()` 自动将关键词转为锚文本链接

### 工作流程

```
写新文章前：
1. python3 find_related_articles.py "文章主题"
2. 选择3-5篇相关文章
3. 查看它们的索引关键词（article_keywords_data.py）
4. 将关键词自然融入新文章正文

写完后：
1. python3 build_multi.py
2. 自动链接已生成
3. 验证：无自链接、无无效链接、每篇≥3条内链
```

### 关键词索引维护
- 文件：`article_keywords_data.py`
- 格式：`slug -> [关键词1, 关键词2, ...]`
- 新增文章时，添加对应的关键词条目
- 关键词应为2-3词的自然短语，不要太长

### 验证命令
```bash
# 检查内链质量
python3 -c "
import re, os
for fname in os.listdir('.'):
    if not fname.endswith('.html'): continue
    # ... 检查自链接和无效链接
"
```

### 注意事项
- 关键词不要太长（2-3词最佳），否则不会精确匹配
- 不要使用会匹配到HTML标签的关键词
- 同一关键词在一篇文章中只链接一次
- 不链接当前文章自己的关键词（防止自链接）
