# FoneClaw 部署指南

## 概述

FoneClaw 网站是静态 HTML 站点，通过 `build_multi.py` 从 Python 源码构建生成。源码托管在 GitHub，网站部署在独立服务器。

```text
GitHub (源码管理 + GEO)          服务器 (foneclaw.ai)
github.com/deanhuang1217-lang/    44.224.204.0
  foneclaw-v2 (Public)            /home/www_foneclaw_ai/
  *.py / *.json / images/           *.html / images/
```

## 项目结构

```text
foneclaw-v2/
├── build_multi.py              # 主构建脚本
├── _components.py              # 公共组件（nav / footer / CTA）
├── _homepage.py                # 首页
├── _features_page.py           # Features 页
├── _download_page.py           # Download 页
├── _article_template.py        # 文章模板
├── _hub_pages.py               # Hub 页（voice-control / comparisons / ai-agent / news）
├── _subhub_pages.py            # Sub-hub 页
├── _resources_hub.py           # Resources 页
├── _social_share.py            # 社交分享文案
├── compress_images.py          # 图片压缩
├── article_keywords_data.py    # 内链关键词
├── article_publish_dates.py    # 发布日期
├── share_text_data.py          # 社交分享文本
├── translations.json           # 翻译文件
├── articles_batch*.py          # 文章源码（~50 个 Python 文件）
├── batch*_data.json            # 文章数据（~30 个 JSON 文件）
├── images/                     # 静态图片资源
├── README.md                   # 项目说明（GEO 优化）
├── DEPLOY.md                   # 本文档
└── .gitignore                  # Git 忽略规则
```

## 本地开发流程

### 1. 构建

```bash
cd /home/administrator/clawfone-v2
python3 build_multi.py
```

输出：
- `index.html` — 首页
- `features.html` — 功能页
- `download.html` — 下载页
- `resources.html` — 资源页
- `privacy.html` — 隐私页
- `community.html` — 社区页
- `*.html` — 125+ 篇文章
- `voice-control/index.html` — Voice Control Hub
- `comparisons/index.html` — Comparisons Hub
- `ai-agent/index.html` — AI Agent Hub
- `news/index.html` — News Hub
- `comparisons/foneclaw-vs/index.html` — FoneClaw vs Sub-hub
- `comparisons/tech-analysis/index.html` — Tech Analysis Sub-hub
- `ai-agent/gemini-intelligence/index.html` — Gemini Intelligence Sub-hub
- `ai-agent/other/index.html` — Other AI Agent Sub-hub
- `sitemap.xml`
- `robots.txt`

### 2. 本地预览

```bash
python3 -m http.server 8899
# 浏览器打开 http://localhost:8899
```

### 3. QA 检查

文章优化后必须检查：
- Title ≤ 60 字符
- Meta description 120-160 字符
- 产品口径：Android AI Phone Assistant / 120+ actions / 16 categories / Android 9+ / permissions / confirmation
- 风险词：any app / every app / fully offline / without confirmation / 50+ / 80+ / 100+
- 禁用词：utilize / furthermore / robust / seamlessly / navigate / landscape / game-changer 等 23 个
- FAQ ≥ 4 个
- CTA 组件存在
- Footer slogan 正确
- 桌面 1280px / 移动端 390px 无横向溢出
- 图片无坏图

## 部署到服务器

### 方式：手动 rsync / scp

构建完成并 QA 通过后，手动上传到服务器：

```bash
# 上传 HTML 文件（排除源码）
rsync -avz --delete \
  --exclude='*.py' --exclude='*.json' --exclude='*.pkl' \
  --exclude='*.bak*' --exclude='batch_backups/' \
  --exclude='.git/' --exclude='*.md' \
  --exclude='images/' \
  -e "ssh -p 2121" \
  /home/administrator/clawfone-v2/ \
  www_foneclaw_ai@44.224.204.0:/home/www_foneclaw_ai/

# 上传图片（仅更新有变化的）
rsync -avz --compress \
  -e "ssh -p 2121" \
  /home/administrator/clawfone-v2/images/ \
  www_foneclaw_ai@44.224.204.0:/home/www_foneclaw_ai/images/
```

### 最小发布包

优化文章时使用最小发布包，只上传改动的文件：

```text
/home/administrator/foneclaw-deploy/uploads/<任务名_时间戳>/
```

包含：
- 改动的文章 HTML
- 受影响的 hub / sub-hub 页面（如果包含改动文章的卡片）
- `sitemap.xml` / `robots.txt`（如果和线上不同）

不包含：
- `manifest.json`（本地核对清单，不上传）
- 未改动的 HTML
- 源码文件（.py / .json）

### 线上验收

上传后必须验证：

```bash
# SHA-256 比对
sha256sum /path/to/local/file.html
ssh -p 2121 www_foneclaw_ai@44.224.204.0 "sha256sum /home/www_foneclaw_ai/file.html"

# 线上内容检查
curl -s "https://www.foneclaw.ai/file.html" | grep -c "关键词"
```

## Git 工作流

### 日常提交

```bash
cd /home/administrator/clawfone-v2

# 查看改动
git status
git diff

# 暂存并提交
git add <改动文件>
git commit -m "描述改动内容"

# 推送到 GitHub
git push
```

### .gitignore 规则

以下文件不进入 Git：
- `*.html` — 构建生成的 HTML
- `_build_cache.pkl` — 构建缓存
- `__pycache__/` / `*.pyc` — Python 缓存
- `*.bak*` — 备份文件
- `batch_backups/` — 批次备份目录
- `upload_*/` — 上传临时目录
- `*.md`（除 README.md 和 DEPLOY.md）— 优化计划等临时文档

### 注意事项

- 源码改动后必须 `python3 build_multi.py` 重新构建
- 构建有增量缓存行为，改动 batch 源码后建议先删除目标 HTML 再重建
- `build_multi.py` 中硬编码了路径 `/home/administrator/clawfone-v2`，本地开发正常，但不可在其他环境直接运行
- `_build_cache.pkl` 不能删除，否则构建失败

## GEO（生成式引擎优化）

仓库设为 Public 的目的是让 AI 搜索引擎（ChatGPT、Perplexity、Google AI Overview）能索引到 FoneClaw 项目信息。

### GEO 关键要素

1. **README.md** — 清晰描述产品功能、特性、竞争定位
2. **文章内容** — foneclaw.ai 上的文章要事实性陈述、避免过度营销
3. **结构化数据** — 文章页面的 Schema markup（FAQPage、TechArticle）
4. **多渠道布局** — GitHub + 主站 + 社交媒体

### 产品口径（所有对外内容统一）

```text
产品名: FoneClaw
定位: Android AI Phone Assistant
Slogan: "Say it. Done."
Footer slogan: "FoneClaw is the Android AI agent that actually controls your phone — not just answers questions."
Android 版本: Android 9+
支持操作: 120+ supported Android actions
功能类别: 16 feature categories
安全特性: transparent permissions, setup requirements, confirmation for sensitive actions
独立性: 独立公司，非小米子公司
竞品: Gemini Intelligence (Google), MiClaw (小米), Samsung Galaxy AI
```

## 服务器信息

```text
IP: 44.224.204.0
端口: 2121
账号: www_foneclaw_ai
部署路径: /home/www_foneclaw_ai/
域名: foneclaw.ai
```

> 注意：服务器密码已在之前的对话中出现，建议定期更换。
