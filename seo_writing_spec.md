# FoneClaw SEO Article Writing Specification v3.1

## 写作模型（2026-05-22更新）

**写文章用 Gemini 3.5 Flash**

| 配置项 | 值 |
|--------|-----|
| 模型名 | `gemini-3.5-flash` |
| 端点 | `generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent` |
| maxOutputTokens | **16384**（8192会导致文章被截断） |
| temperature | 0.7 |
| API Key | `/home/administrator/video-workflow/.env` |

### 写作质量（2026-05-22 Batch9测试）

| 指标 | Gemini 3.5 Flash |
|------|------------------|
| 平均字数 | 3008词 |
| 禁用词 | 0个 |
| E-E-A-T | 平均8.4处 |
| FAQ | 全部8个 |
| 段落结构 | 平均60词/段 |

### 写作流程

1. **梳理prompt** - 为每篇文章生成完整prompt（slug/title/meta/section outline）
2. **逐篇生成** - 调用Gemini 3.5 Flash API，maxOutputTokens=16384
3. **验证质量** - 检查字数/禁用词/E-E-A-T/FAQ
4. **合并为batch** - 保存为JSON格式，创建加载脚本



## Product Context
FoneClaw = AI Agent for voice-controlled Android phones (US market)
- Target: US users, English only
- Key features: 50+ voice operations, multi-step automation, remote control, memory learning
- Website: www.foneclaw.ai

## Article Format (MUST follow exactly)
Output a Python tuple: (article_id, title, description, category, read_time, sections)
- sections = list of (subtitle, body_text) tuples
- Each body_text MUST be 250-400 words
- 7-8 sections per article (6 content + 1 intro + 1 FAQ)
- Total article length: 质量优先，不强制字数
  - 推荐1500-3000词（根据文章类型）：教程/指南2000-3000词，对比/评测1500-2500词，行业分析2000-3000词，功能介绍1500-2500词
  - 禁止为凑字数而堆砌内容
  - 每个章节250-400词，确保信息密度

## E-E-A-T引用位置（必须遵守）
- 第1个section开头（最重要的位置）
- 至少1个数据引用（数字+来源）
- 至少1个测试引用（"Based on our testing"）

## KEYWORD TARGETING (MANDATORY)

Every article MUST include its assigned keywords naturally throughout the text.

### Keyword Placement Rules:
1. **H1 (title)**: MUST contain the primary keyword
2. **First 100 words**: MUST contain the primary keyword naturally
3. **At least 1 H2**: MUST contain the primary keyword or close variant
4. **Each H2**: Should contain 1 secondary keyword
5. **FAQ section**: At least 1 Q&A must mention the primary keyword
6. **Final paragraph**: Re-mention the primary keyword
7. **Density target**: 1.0-1.8% (for a 2000-word article = 20-36 occurrences)

### How to naturally integrate keywords:
- Use them in real scenarios: "When you need voice control while driving..."
- Use them in questions: "How does hands-free texting work?"
- Use them in comparisons: "Unlike basic voice commands, FoneClaw..."
- Use them in conclusions: "Voice control on Android has evolved..."
- DON'T force keywords into every sentence
- DO use variations: "voice control" / "voice commands" / "voice-controlled"

## 内链规范（必须遵守）

### 内链数量
- 2000-3000词：8-12条
- 3000-5000词：12-15条
- 上限：15条

### 内链规则
- 同一关键词只链接一次（首次出现）
- 同一目标文章只链接一次
- 均匀分布（不要集中在一段）
- Anchor Text：2-4词，包含关键词
- 不链接已有<a>标签内的文字
- 不链接<h2>标题内的文字

## SEO Writing Framework

### Opening (Section 1 - Intro)
Use PAS framework:
- Problem: Start with a relatable pain point (use keyword in context)
- Agitate: Expand on consequences
- Solution: Introduce FoneClaw as the answer
Include primary keyword in first 100 words.

### Body Sections (Sections 2-6)
Each section:
- H2 subtitle containing a secondary keyword variation
- 250-400 words of substantive content
- Include 1-2 Bucket Brigades per article (NOT per section), rotating:
  * "The real difference?" / "What matters most?" / "The key insight?"
  * "The reality is:" / "The honest truth?" / "What actually happens?"
  * "Here's how" / "In practice:" / "Concretely:"
  * "Consider this:" / "Put differently:" / "To illustrate:"
- Include real-world scenarios, specific numbers
- Naturally weave in keywords and semantic related terms
- Use bullet points where appropriate

### FAQ质量标准（必须遵守）
- 问题必须是真实搜索查询
- 答案40-60词，具体有信息量
- 至少1个问题包含主关键词
- 避免泛泛而谈的问答

### FAQ Section (Last section)
Title: "Frequently Asked Questions"
Body: 4-5 Q&A pairs, each 40-60 words
- At least 1 question must contain the primary keyword
- Questions should target actual search queries
Format: "Q: ... A: ..."

## 格式元素使用（建议）
- 每200-300词使用一个小标题
- 适当使用列表（但不要过度）
- 使用引用块突出重要信息
- 使用表格对比信息

## BANNED PHRASES (AI-taste detection)
DO NOT use these phrases:
- incredibly, seamlessly, absolutely, fundamentally, revolutionary
- "Here's the thing:", "But there's a catch", "Let me explain"
- "Now, you might be wondering", "The bottom line?", "Think about it this way"
- "game-changer", "empower", "leverage", "cutting-edge", "unparalleled"
- "changes this dynamic entirely", "in this article"
- "We have all been there/experienced", "Imagine your/this/that"
- Avoid repeating the same Bucket Brigade more than once per article

## 图片Alt文本（必须遵守）
- 每张图片必须有描述性alt文本
- 包含关键词
- 描述图片内容

## Tone
- Conversational but authoritative
- Second person ("you")
- Short sentences mixed with longer ones
- Real scenarios, not abstract claims
- Vary sentence openings (don't start every paragraph the same way)
- Limit "FoneClaw" mentions: max 1 per paragraph, use "the app/agent/tool" alternately

---

## 移动端优化（必须遵守）
- 移动端和桌面端内容完全一致
- 通过CSS和结构优化体验
- 使用小标题、列表、表格分隔内容
- 重要信息前置

## 2026 SEO Updates (Post Google March 2026 Core Update)

### Information Gain Signal (Critical)
Google now explicitly measures "Information Gain" — how much genuinely new knowledge a piece of content adds relative to what already ranks for the same query. Content that merely rephrases or aggregates top-ranking pages will lose rank.

**Actionable rules:**
- Every article MUST contain at least ONE unique element: original data, proprietary insights, first-hand testing results, real user scenarios, or a novel comparison framework
- Before writing, check the current top 5 results for the target keyword — your article must add something NONE of them cover
- Do NOT simply rephrase competitor content with better keyword optimization
- Prefer: real FoneClaw usage data, specific benchmarks, unique user scenarios, comparison tests
- Avoid: generic "top 10 benefits" lists that could apply to any voice assistant

### E-E-A-T Author Authority
Google now cross-references author expertise with content complexity (Experience-Authority Gap Analysis). Anonymous or generic "Editorial Team" bylines lose ranking power.

**Actionable rules:**
- Articles should reference specific expertise: "In our testing of 50+ voice commands..." or "Based on FoneClaw user data..."
- Include credible attribution where possible (link to official docs, cite real product capabilities)
- Avoid publishing content on topics where the site has no demonstrable authority (stay in the voice control / Android automation lane)

### User Interaction Pattern Scoring
Google now analyzes post-click behavior: scroll-back rate, comparison bounces, snippet satisfaction. Content must genuinely satisfy user intent, not just technically answer a query.

**Actionable rules:**
- Answer the primary query in the first 200 words (satisfy snippet scanners)
- Use clear structure so users can find answers without bouncing (H2s as signposts)
- Include actionable takeaways, not just information dumps
- Make FAQ answers genuinely useful (40-60 words, specific, not vague)

### AI Search Optimization (GEO — Generative Engine Optimization)
LLMs (ChatGPT, Perplexity, Google AI Overviews) pull from 16-36 diverse sources per answer. Being cited in AI answers is now a primary SEO goal alongside traditional rankings.

**Actionable rules:**
- Structure content with clear, quotable statements that LLMs can extract
- Use definitive phrasing: "FoneClaw supports 50+ voice commands" not "There are many voice commands available"
- Include specific numbers, facts, and structured data that LLMs prefer to cite
- Ensure content appears on third-party sites (reviews, comparisons, forums) for broader AI visibility
- FAQ sections should directly answer questions in a format LLMs can extract

### Topical Coherence
Google rewards domains with consistent authority in a defined subject area over time. Publishing across many topics at shallow depth hurts domain authority.

**Actionable rules:**
- Keep all articles within FoneClaw's core domain: voice control, Android automation, hands-free productivity, accessibility
- Do NOT write tangential content just for search volume (e.g., generic "best Android apps" unless directly tied to voice control)
- Build content clusters: interlink related articles to demonstrate depth in the topic area

### Schema Markup Strategy (Post March 2026 Update)
Google's March 2026 update fundamentally shifted structured data's role: from SERP display trigger → AI trust and entity verification signal.

**Key changes:**
- FAQ schema now restricted to pages where FAQ is the PRIMARY content (blog post FAQs no longer qualify for rich results)
- How-To rich results removed entirely from desktop; mobile limited to primary content pages
- Editorial Review schema (self-reviews, "best of" roundup ratings) now triggers manual action risk
- Organization + Person schema with `SameAs` identifiers is the highest-leverage implementation
- `Speakable` schema flags citable passages for AI synthesis (no SERP display, pure AI signal)

**Actionable rules for FoneClaw articles:**
- Use `Article` + `Author` (Person) schema with `SameAs` links to verify author identity across platforms
- Add `Speakable` markup to the most quotable/definitive paragraph in each article
- Do NOT add FAQ schema to articles where FAQ is just a supplementary section
- Do NOT use editorial Review schema on comparison or "best of" articles
- Ensure all schema passes Google Rich Results Test validation

### AI Traffic Quality Data (Ahrefs, May 2026)
AI-driven traffic converts at significantly higher rates than traditional search traffic (Ahrefs reports 23x higher conversion). Prioritize quality over volume.

**Content types earning disproportionate AI traffic:**
- "Best" articles: 7.06% of AI traffic share
- "How-to" guides: 6.35%
- "Top" lists: 5.5%
- "Vs" comparisons: 4.88%

**Third-party brand mentions matter most for AI citations.** Backlinko/Ahrefs data shows most AI citations reference third-party sites, not the brand's own domain. Unlinked mentions are picked up equally by AI engines.

**Actionable rules:**
- Prioritize "how-to" and "comparison" content formats for FoneClaw (highest AI traffic potential)
- Include definitive, quotable statements in every article (e.g., "FoneClaw supports 50+ voice commands")
- Ensure FoneClaw is mentioned on third-party review/comparison sites for broader AI visibility

---

## 2026年6月最新SEO知识更新 ⭐ NEW

### 1. GEO（生成式引擎优化）深化

**Google AI Overview扩展**：已覆盖美国、英国、印度等市场的大部分搜索查询，展示在搜索结果顶部。

**GEO核心策略：**
- **结构化、可引用的内容**：使用列表、表格、定义、步骤格式
- **成为AI的引用来源**：直接回答问题，使用统计数据和具体数字
- **技术实现**：确保页面可被AI爬虫访问（不要屏蔽GPTBot、CCBot等）

**GEO写法示例：**
```
传统写法：
"SEO是一个复杂的领域，需要考虑很多因素..."

GEO优化写法：
"2026年SEO的三大核心因素是：(1) 内容质量与E-E-A-T信号（占排名因素约35%），
(2) 技术SEO与用户体验（约30%），(3) 链接与品牌信号（约25%）。"
```

### 2. E-E-A-T框架演进

**2026年新变化：**
- **作者实体化**：Google Knowledge Graph对作者实体的识别能力增强
- **内容新鲜度信号**：Google能识别"有意义的更新"vs"仅改日期"
- **原创性验证**：纯粹的AI改写内容排名持续下降

**行动建议：**
- 为每个内容创作者建立详细的作者页面
- 在AI辅助创作的内容中加入原创数据、案例和见解
- 避免大规模AI批量生产内容（AI content farms）

### 3. 技术SEO更新

**Core Web Vitals 2026指标：**
| 指标 | 全称 | 良好阈值 | 需改进 | 差 |
|------|------|---------|--------|-----|
| **LCP** | Largest Contentful Paint | ≤2.5秒 | 2.5-4秒 | >4秒 |
| **INP** | Interaction to Next Paint | ≤200毫秒 | 200-500毫秒 | >500毫秒 |
| **CLS** | Cumulative Layout Shift | ≤0.1 | 0.1-0.25 | >0.25 |

**INP（2024年3月替代FID）**：测量用户交互到页面视觉响应的完整延迟。

**其他技术趋势：**
- 动态渲染（Dynamic Rendering）已被Google标记为临时方案，建议迁移到SSR
- Google完全切换到移动端优先索引（Mobile-first Indexing）
- HTTPS已成为绝对基线要求

### 4. Schema标记更新

**2026年新增Schema类型：**
- `Speakable`：针对语音搜索优化，标记适合朗读的内容片段
- `ClaimReview`：事实核查标记，在YMYL领域越来越重要
- `LearningResource`：教育内容标记

**Schema实施策略：**
- 使用JSON-LD格式（Google推荐）
- 嵌套标记：将相关Schema类型组合（如Article + Person + Organization）
- 使用`sameAs`属性帮助建立知识图谱关联

### 5. 链接建设策略更新

**2026年链接价值变化：**
- 质量 >> 数量：低质量链接不仅无效，还可能有害
- 品牌提及（Brand Mentions）：无链接的品牌提及越来越被重视为排名信号
- 实体关联（Entity Association）：链接的语义相关性比域名权重更重要

**有效策略：**
| 策略 | 效果 | 推荐度 |
|------|------|--------|
| 原创研究/数据发布 | ⭐⭐⭐⭐⭐ | 强烈推荐 |
| 专家访谈/圆桌讨论 | ⭐⭐⭐⭐ | 推荐 |
| 数字PR | ⭐⭐⭐⭐⭐ | 强烈推荐 |
| 目录提交 | ⭐ | 不推荐 |
| 购买链接 | ❌ | 禁止 |

### 6. 需要避免的过时做法

**❌ 内容层面：**
- 关键词堆砌 → 自然写作，关注话题覆盖
- 大量AI批量生成内容 → AI辅助+人工编辑+原创价值
- 仅改日期不改内容 → 有实质性内容更新
- 抄袭/改写竞争对手内容 → 提供独特视角和原创数据

**❌ 技术层面：**
- 动态渲染 → SSR或SSG
- 过度依赖客户端渲染 → Next.js/Nuxt等SSR框架
- 忽视移动端体验 → 移动端优先设计

**❌ 链接层面：**
- PBN（私有博客网络） → 内容驱动的自然链接
- 购买链接 → 创造值得链接的内容
- 大量评论链接 → 仅在相关社区有意义参与

### 7. AI搜索时代的反模式

1. **不要屏蔽所有AI爬虫**：除非有明确的商业原因，否则允许AI爬虫访问可以增加品牌在AI回答中的曝光
2. **不要忽视AI来源的流量**：AI搜索正在改变流量分布，需要监控和优化
3. **不要只关注传统排名**：AI Overview中的引用位置可能比传统排名更有价值
4. **不要忽略品牌建设**：在AI搜索时代，品牌认知度是被引用的关键因素

---

## 2026年SEO优先级清单

### 高优先级（立即行动）
1. ✅ 优化Core Web Vitals，特别是INP
2. ✅ 审计并提升内容质量（E-E-A-T）
3. ✅ 实施完整的Schema标记
4. ✅ 分析AI Overview对核心关键词的影响
5. ✅ 建立内容创作者的实体化展示

### 中优先级（本季度）
6. 🔄 开发GEO优化策略
7. 🔄 建立数据驱动的链接建设流程
8. 🔄 优化移动端体验
9. 🔄 实施内容更新审计流程

### 长期规划（本年度）
10. 📋 建立品牌提及监控系统
11. 📋 开发原创研究/数据内容资产
12. 📋 探索多模态搜索优化（图像、视频）
13. 📋 建立AI搜索流量监控体系

---

## 2026年5月最新SEO知识更新 ⭐ NEW (2026-05-18)

### 8. Relevance Engineering（相关性工程）— AI搜索新范式

**核心变化**：Google AI Mode逐步取代传统SERP，搜索行为从线性变为个性化。每个用户看到独特的、基于历史和意图生成的结果。传统关键词追踪正在变得过时。

**Query Fan-Out（查询扇出）机制**：一个主题会触发多个相关问题、变体和格式。SEO需要从"关键词追踪"转向"查询扇出映射"。

**行动建议：**
- 围绕用户意图（而非关键词密度）重建内容策略
- 识别核心主题触发的所有相关查询变体和格式
- 构建跨格式、跨平台的内容生态系统（视频、社交、论坛、工具）
- 将内容设计为AI可提取的训练数据：语义丰富、机器可读、结构化
- 优化目标：从"关键词密度"转向"受众共鸣"

### 9. 后端SEO与代理AI（Agentic AI）可访问性

**新趋势**：2026年，后端SEO（API、数据库、内容结构）与前端优化同等重要。AI助手需要通过智能设备（Google Nest、智能电视等）访问内容并执行操作。

**新兴协议：**
- **Agentic Commerce Protocol (ACP)**：电商AI优化产品Feed
- **Media Control Protocol (MCP)**：媒体/订阅内容的AI助手可访问性

**行动建议：**
- 确保后端系统有干净的API和结构化数据库
- 为AI助手的直接操作（预约、下单等）预留接口
- 产品Feed需要针对AI优化（不仅是Google Shopping）

### 10. 品牌情感作为AI可见性信号

**新维度**：LLM优先展示来自可信、权威来源的内容。品牌在全网的持续提及（社会评论、评测、高质量反链）直接影响AI如何呈现你的品牌。**提及的情感倾向**（正面/负面）直接影响AI排名和展示方式。

**行动建议：**
- 将品牌搜索量视为关键漏斗顶部指标
- 与出版商、KOL、评测平台建立关系
- 使用AI可见性工具追踪品牌在AI回答中的呈现
- 将正面评价和批评转化为互动机会
- 跨平台保持一致的品牌信息和语调

### 11. 内容格式多元化提升AI引用稳定性

**新发现**：AI平台（Perplexity等）现在从更广泛的渠道拉取数据，包括Instagram、Facebook等社交平台。**实用性工具内容**（计算器、模板、清单、交互工具）更容易获得AI引用。多格式内容品牌在各搜索场景中获得更稳定的引用。

**行动建议：**
- 不要仅依赖文字内容，将文章转换为多模态格式
- 投资创建实用工具内容：计算器、模板、清单、Checklist
- 在AI工具经常拉取的平台分享内容：Reddit、YouTube、主要社交网络
- 品牌提及出现在论坛和社区讨论中可以增加AI引用概率

### 12. 产品导向内容（Product-Led Content）为AI搜索设计

**新策略**：买家越来越期望AI工具推荐最适合其特定场景的产品。内容应聚焦于产品如何解决具体用例，而非泛泛解释问题。买家会用高度具体的查询提示AI。

**行动建议：**
- 优先创作底部漏斗内容：假设受众已理解问题，展示产品如何更好地解决
- 具体化优势：突出产品表现出色的用例和理想客户画像（ICP）
- 使用真实证据：照片、截图、定制演示视频、客户案例——不用AI生成内容
- 监控Reddit、Quora、Facebook群组等社区中受众使用的语言和问题

### 13. 三种SEO策略路径（State of SEO 2026调查）

**行业格局**（基于371名SEO专业人士调查）：
- **AI-Heavy Adopters (22%)**：全面押注自动化规模化
- **Authority Builders (49%)**：加倍投入E-E-A-T和人类专业知识
- **Hybrid Strategists (58%)**：AI辅助+人类创作的中间路线

**关键数据**：
- 66%认为原创内容创作对SEO影响最大
- 49%计划在2026年投资E-E-A-T建设
- 77%担忧AI回答会减少网站点击量
- 42.3%已使用AI写作助手（与技术SEO工具并列第四）

**行动建议：**
- 选择适合自身的策略路径，但原创内容+人工审核是核心
- 将E-E-A-T作为对抗AI冲击的防御策略
- 追踪业务影响指标（品牌搜索量趋势、LLM中的声量份额、客户终身价值）

---

## 2026年5月25日新增：AI Overview引用排名因素研究 ⭐ NEW

基于Wellows对15,847个AI Overview结果的系统性研究（2026年5月），7个核心排名因素按影响力排序：

### 1. 语义完整性（Semantic Completeness）— r=0.87
**最核心因素**。内容评分≥8.5/10时被AI引用概率提升4.2倍。
- **最优语义单元长度**：134-167词（AI提取效率最高的段落长度）
- 62%的AI引用内容落在100-300词区间
- 每个语义单元必须**自包含**：定义+证据+结论，无需上下文即可理解
- 关键答案放在板块前100词内

### 2. 多模态内容整合 — r=0.92（最高相关性）
文本+图片+视频+结构化数据的页面，AI选择率比纯文本高**156%**。
完整多模态+Schema集成可提升**317%**的AI引用率。
- 每篇文章2-3张带Alt文本的图片
- 教程类内容优先嵌入视频
- 关键数据以文本+表格+列表三种形式呈现

### 3. 实时事实验证 — r=0.89
Google AI实时交叉验证事实声明。引用率提升**89%**。
- 每篇至少2个可验证数据源
- 数字+来源格式：「FoneClaw支持50+语音命令（2026年4月版本统计）」
- 引用来源需可被AI验证（官方文档、研究论文、行业报告）

### 4. E-E-A-T + 实体密度 — r=0.81
96%的AI引用来自强E-E-A-T来源。15+被识别实体 → 引用概率提升**4.8倍**。
- 自然包含15+个Knowledge Graph可识别实体
- 实体类型：品牌名、专业术语、产品名、人物/组织

### 5. 传统SEO指标衰退
- Domain Authority相关性降至r=0.18
- **47%**的AI引用来自排名低于第5位的页面
- LLM引荐流量转化率**30-40%**（VentureBeat）

### FoneClaw文章写作新规则
1. 每个H2板块设计134-167词的自包含语义单元
2. 每篇包含15+个可被Google识别的实体
3. 每篇至少2个带来源的可验证数据
4. 关键观点以文本+表格+列表三种形式呈现
5. 答案前置：每个板块前100词内回答核心问题

---

## 2026年6月1日新增：Agentic RAG与AI搜索架构演进 ⭐ NEW

### 14. Agentic RAG — AI搜索的核心架构变革

**核心变化**：AI搜索已从单次检索（single-shot RAG）演进为Agentic RAG。Google AI Mode、ChatGPT Search、Perplexity Pro Search等所有主流平台现在都运行多阶段、多循环的检索架构。

**Agentic RAG的四个核心属性：**
1. **Planning（规划）**：系统在检索前将用户查询分解为研究计划，生成子查询，预选工具，确定检索顺序
2. **Tool Use（工具调用）**：检索只是众多工具之一，Agent可以选择向量索引、BM25索引、结构化数据API、代码执行、实时网页浏览等
3. **Multi-hop Iteration（多跳迭代）**：Agent检索→阅读→再检索，基于新发现不断深化
4. **Reflection（反思）**：Agent对生成的答案进行自我评分（充分性、矛盾性、新鲜度、来源多样性），不满意则重新检索

**对内容写作的影响：**
- 传统SEO优化为一个判断时刻（SERP），Agentic RAG需要在五个不同时刻获胜：planner、router、retrieval、pairwise、critic
- 单次检索的"top-k"逻辑已过时，内容需要在多阶段管道中生存
- 引用计数可能低估实际影响力3-10倍（如果你出现在4/12个子检索中但只被引用1次，传统追踪漏掉75%的影响）

**行动建议：**
- 内容设计为"自包含语义单元"（定义+证据+结论），无需上下文即可被理解
- 每个H2板块的前100词内回答核心问题（满足planner的提取需求）
- 使用明确、可引用的陈述（满足critic的验证需求）
- 结构化数据+多模态内容提升在多个检索阶段的可见性

**来源**: Search Engine Land, "Beyond RAG: Why every AI search platform is now agentic and what that means for your content" (2026-05-29)
https://searchengineland.com/beyond-rag-ai-search-agentic-content-478996

### 15. Google AI Guide明确 debunked 的5个做法

**Google官方立场**（2026年5月）：以下做法对AI Overview引用无效：

| 做法 | Google态度 | 正确理解 |
|------|-----------|---------|
| llms.txt | ❌ 无效 | Googlebot不读取此文件，不影响AI引用 |
| AI-specific内容重写 | ❌ 无效 | 被Google质量系统视为低质量内容 |
| 内容切片（chunking） | ❌ 无效 | Google系统原生处理多主题页面 |
| 虚假品牌提及 | ❌ 无效 | 无论任何范围都是违规 |
| 过度Schema优化 | ⚠️ 误解 | Schema是身份基础设施，不是引用杠杆 |

**正确理解：**
- "Wrong for Google Search" ≠ "Wrong for AI agents"
- llms.txt概念对自主Agent可能有用，但不是引用策略
- 内容应为"清晰写作"而非"为AI写作"——Machine-First Architecture
- Schema是table-stakes身份基础设施，不是月度引用提升工具

**来源**: Search Engine Journal, "What Google's New AI Guide Actually Debunks. And What It Doesn't" (2026-06-01)
https://www.searchenginejournal.com/what-googles-new-ai-guide-actually-debunks-and-what-it-doesnt/575497

### 16. AI Overview在商业查询中的超高触发率

**关键数据**（Peec研究，2026年4月）：
- 商业/购买意图查询：AI Overview触发率 **88.5%**
- 决策阶段提示（产品比较）：**88.5%**
- 11-15词长查询：触发率接近 **89%**
- 2词短查询：触发率 **64.6%**
- EU地区：**76%**（法国0%，因未上线）
- 非EU地区：**90.3%**

**重要区分：**
- 87%的数字测量的是"购买意图提示"的AI Overview出现率，不是所有Google搜索
- Ahrefs分析1.46亿结果发现AI Overview覆盖20.5%的关键词
- 差异在于：高意图、完整句子提示更容易触发AI Overview

**对内容写作的启示：**
- 底部漏斗内容（比较、"best X for Y"）比信息类内容更容易获得AI Overview展示
- 如果优化只针对信息类搜索，会错过导致购买的搜索
- AI Mode已突破10亿月活，与AI Overview深度整合

**来源**: Search Engine Journal, "Google AI Overview Data Looks Different For Commercial Queries" (2026-05-29)
https://www.searchenginejournal.com/google-ai-overview-data-looks-different-for-commercial-queries/577350

### 17. AI内容不等于SEO成功 — 长尾查询崛起

**核心发现**：
- 长尾查询（10+词）大幅增长，查询复杂性上升
- 驱动真实意图的查询现在更像自然语言，而非SEO优化的关键词短语
- AI在开放网络上训练的内容仍在为旧模式写作
- 结果：内容产出更快，但匹配的实际转化查询更少

**4层AI Ops框架**（CallRail的Darrell Tyler）：
1. **Knowledge层**：训练AI使用自然语言输入（匹配实际搜索方式）
2. **Workflow层**：将AI从个人工具扩展到团队系统
3. **Governance层**：建立质量控制和品牌一致性
4. **Application层**：将AI应用于内容优化、排名报告、技术审计

**行动建议：**
- AI需要使用已经以自然语言编写的训练材料
- 第一方数据源（客服对话、销售反馈、用户评价）是自然语言输入的最佳来源
- AI工作流不能只存在于一个人的保存提示中

**来源**: Search Engine Journal, "AI Content Alone Won't Fix Your SEO Rankings (Here's What Will)" (2026-05-29)
https://www.searchenginejournal.com/ai-content-alone-wont-fix-your-seo-rankings-heres-what-will/577380

### 18. AI的6种使用模式 — 判断层才是价值所在

**Gorichanaz研究**（2025 ASIS&T，205个ChatGPT使用案例）：

| 模式 | 占比 | 价值层级 |
|------|------|---------|
| Writing（写作） | 47% | 执行层 |
| Identifying（识别） | 10% | 执行层 |
| **Deciding（决策）** | **21%** | **判断层** |
| **Ideating（构思）** | **9%** | **判断层** |
| **Talking（对话）** | **8%** | **判断层** |
| **Critiquing（批评）** | **6%** | **判断层** |

**关键发现**：
- 88%的组织使用AI，但只有6%产生有意义的企业级影响
- 高绩效者比普通者更可能从根本上重组工作流程（3.6倍）
- Writing+Identifying占77%的使用，但不是杠杆所在
- Deciding+Ideating+Talking+Critiquing是不可替代的

**对SEO从业者的启示：**
- **Deciding模式**：用AI压力测试假设（不是draft，是decision input）
- **Ideating模式**：映射品牌未识别的实体和权威缺口
- **Critiquing模式**：在策略周期前用AI发现内部审查遗漏的问题
- **Talking模式**：为高风险对话排练（客户汇报、内部简报）

**来源**: Search Engine Journal, "You're Using AI At The Execution Layer. The Value Is In The Judgment Layer" (2026-05-28)
https://www.searchenginejournal.com/youre-using-ai-at-the-execution-layer-the-value-is-in-the-judgment-layer/575747

---

*本规范基于截至2026年6月1日的最新SEO行业趋势、Google官方动态及行业专家观点综合整理。*
## 2026年6月15日新增 ⭐ NEW

### 19. 搜索景观结构性变化：信息类vs决策类查询CTR分化

**核心发现**（DigitalDiscoverist, 2026-06）：
- 信息类查询（定义、简单how-to、日期查询）：CTR大幅下降，AI Overview无需点击即解决
- 决策类查询（产品对比、深度推荐、本地信息）：CTR基本不受影响
- Google AI Overview覆盖约15-20%的美国查询（2025年中），持续扩展
- 多模态搜索（Google Lens数十亿次/月）和语音查询（Gemini驱动）成为主流
- SEO不再是独立渠道，必须与品牌建设整合：品牌搜索→更高CTR+排名提升，社交分发→链接+新受众，邮件/社区→回访用户+互动信号

**对FoneClaw的启示：**
- 信息类内容（"what is voice control"）需要额外价值层来保持CTR
- 决策类内容（"best voice control app for Android 2026"）是更安全的投资方向
- 品牌建设不是可选项，是SEO的必要组成部分

### 20. 情感写作框架（GEO优化写法新维度）

**新写作技术**（TextWordCount, 2026-06）：
大多数SEO文章失败的原因：听起来为电子表格而写，不是为赶工期的人写的。

**每个section的4步循环：**
1. **命名痛点**：用具体场景引发共鸣
2. **承诺具体结果**：给出明确预期输出
3. **展示你如何知道**：过程、数据或经验（E-E-A-T自然跟随）
4. **提供下一步**：内链、模板或工具

**Before vs After示例：**
```
Before（机器人）："SEO content writing requires keyword optimization and meta tag best practices."
→ 准确但无用，没人知道周一早上该做什么

After（解决问题）："If your article answers 'how to write SEO content,' open with the exact mistake you see in drafts—keyword lists pasted into intros, or FAQs that repeat the H1. Then show your outline: intent label, working title, three H2 questions pulled from People Also Ask."
→ 同一主题，读者看到路径。AI Overviews和GEO更喜欢这个版本，因为声明具体、结构化、可引用。
```

**关键原则：** 读者先于算法。长度没有情感进展就是填充物——对人类和AI摘要都是如此。

### 21. 发布前竞争对标检查

**新流程步骤**（TextWordCount, 2026-06）：
在发布前，将文章字数和结构与排名前3的竞争对手对标：
- 检查竞争对手平均字数（用word counter工具）
- 对比阅读时间
- 确保每个section在竞争对手基础上有所增量
- 一轮诚实度检查：删除无法用证据或经验支持的声明

---

*本规范基于截至2026年6月15日的最新SEO行业趋势、Google官方动态及行业专家观点综合整理。*
*最后更新：2026-06-15*
