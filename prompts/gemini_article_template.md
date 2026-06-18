# Gemini 3.5 Flash Article Writing Prompt Template
# 用于FoneClaw SEO文章生成（2026-05-22更新 - Gemini 3.5 Flash）


## API配置

| 配置项 | 值 |
|--------|-----|
| 模型名 | `gemini-3.5-flash` |
| 端点 | `generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent` |
| maxOutputTokens | **16384**（8192会导致文章被截断） |
| temperature | 0.7 |
| API Key | `/home/administrator/video-workflow/.env` |

## 写作流程

1. **梳理prompt** - 为每篇文章生成完整prompt（slug/title/meta/section outline）
2. **逐篇生成** - 调用Gemini 3.5 Flash API，maxOutputTokens=16384
3. **验证质量** - 检查字数/禁用词/E-E-A-T/FAQ
4. **合并为batch** - 保存为JSON格式，创建加载脚本

## 标准Prompt模板

```
Write an SEO article for foneclaw.ai.

Slug: [slug]
Title: [title] (≤60 characters)
Meta: [meta] (120-160 characters)
Category: [Comparison/Use Case/How-To/Industry & Trends]
Topic: [topic description]

Structure (7-8 sections):
- S0: Intro (PAS framework, 200-300 words)
- S1-S6: Content sections (each 250-400 words)
- S7: FAQ (4-5 Q&A pairs, each 40-60 words)

CRITICAL RULES:
1. FoneClaw is INDEPENDENT startup, NOT owned by Xiaomi
2. MiMo is Xiaomi's model - FoneClaw supports but does NOT own it
3. First mention of MiMo must include "Xiaomi" (e.g., "Xiaomi MiMo-V2.5-Pro")
4. Subsequent mentions can just say "MiMo"

E-E-A-T PLACEMENT (REQUIRED):
- First section must start with "Based on our testing/experience/data"
- At least 1 data reference (number + source)
- At least 1 test reference ("Based on our testing")

FAQ FORMAT (MUST follow):
Q: Question here?
A: Answer here (40-60 words, specific and informative).

Q: Another question?
A: Another answer.

- At least 1 question must contain the main keyword
- Questions should be real search queries
- DO NOT use **bold** or numbered lists for FAQ

STYLE:
- Conversational tone, use "you" frequently
- Short sentences mixed with longer ones

PARAGRAPH STRUCTURE (CRITICAL - MUST follow):
- Each section MUST have 3-4 paragraphs (NOT 1 big block)
- Each paragraph: 3-5 sentences (60-100 words)
- Separate paragraphs with \\n\\n (double backslash-n) in Python string
- Structure per section (250-400 words total):
  * Paragraph 1: Hook/Problem (70-80 words)
  * Paragraph 2: Solution/Details (70-80 words)
  * Paragraph 3: Examples/Data (70-80 words)
  * Paragraph 4: Summary/Transition (15-20 words, optional)

Example of CORRECT section format:
```python
("Section Title", "First paragraph with hook and problem statement. This engages the reader. It sets up the context. You should feel the pain point here. This paragraph ends with a question.\\n\\nSecond paragraph provides the solution. It explains the main concept. You learn how it works. The details are specific. This builds on the first paragraph.\\n\\nThird paragraph gives examples. You see real-world applications. The data supports the claims. Based on our testing, this approach works. Users report positive results.\\n\\nFinal short summary sentence that transitions to next section.")
```

Example of WRONG section format (DO NOT do this):
```python
("Section Title", "One giant block of text with 250+ words and no paragraph breaks. This is hard to read on mobile. Users will bounce. The content feels overwhelming. Nobody wants to read a wall of text...")
```

Note: Use \\n\\n (literal string) not actual newlines in Python code
- In Python string: "para1\\n\\npara2\\n\\npara3"
- This becomes: para1[blank line]para2[blank line]para3

- Use H2 subtitles every 200-300 words
- Include lists, tables, blockquotes where appropriate

BANNED WORDS (NEVER use):
utilize, furthermore, robust, seamlessly, incredibly, empower, leverage, cutting-edge, unparalleled, revolutionary, delve, landscape, tapestry, multifaceted, nuanced, intricate, navigate, foster, harness, realm

BANNED SENTENCES:
"Here's the thing:", "But there's a catch", "Let me explain"
"Now you might be wondering", "The bottom line?", "Think about it this way"
"In conclusion", "To summarize"

INTERNAL LINK KEYWORDS (embed naturally in text):
- Same keyword only link once (first occurrence)
- Same target article only link once
- Anchor text: 2-4 words, contains keyword
- Distribute evenly (don't concentrate in one paragraph)

IMAGE ALT TEXT:
- Every image must have descriptive alt text
- Include keywords
- Describe image content

MOBILE OPTIMIZATION:
- Content identical on mobile and desktop
- Use H2, lists, tables to break up content
- Important information first

OUTPUT FORMAT (Python BATCH code only, no explanation):
```python
BATCH = [
    (
        "slug-here",
        "Title Here",
        "Meta description 120-160 characters.",
        "Category",
        "X min",
        [
            ("Section Title 1", "Paragraph 1 hook and problem. 3-4 sentences here. Engage the reader. Set up the context.\n\nParagraph 2 solution and details. 3-4 sentences here. Explain the concept. Provide specifics.\n\nParagraph 3 examples and data. 3-4 sentences here. Real-world cases. Based on our testing.\n\nParagraph 4 short summary. Transition sentence."),
            ("Section Title 2", "Paragraph 1...\n\nParagraph 2...\n\nParagraph 3..."),
            # ... 6-7 sections, each with 3-4 paragraphs separated by \n\n
            ("Frequently Asked Questions", "Q: Question?\nA: Answer 40-60 words.\n\nQ: Question?\nA: Answer 40-60 words."),
        ]
    ),
]
```

IMPORTANT: Separate paragraphs with \n\n (double newline), NOT \n (single newline)
- \n\n = paragraph break (correct)
- \n = line break within paragraph (wrong for section body)

## 使用方法

1. 复制上面的模板
2. 替换 [slug], [title], [meta], [category], [topic] 为实际值
3. 添加内链关键词（从article_keywords_data.py获取）
4. 发送给Gemini 3 Flash Preview
5. 验证输出格式是否正确
6. 保存到articles_batchX.py

## 注意事项

- Gemini可能输出markdown格式，需要手动转换
- Gemini可能输出Python函数，需要提取BATCH部分
- FAQ标题必须是"Frequently Asked Questions"（不是"FAQ"）
- 检查禁用词（包括新增的delve/landscape/tapestry等）
- 每个section必须250-400词（不是50-100词）
- 总字数推荐1500-3000词（根据文章类型）
