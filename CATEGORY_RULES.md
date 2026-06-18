# FoneClaw Resources 分类规则

## 当前7个分类

| ID | 名称 | Icon | 包含内容 |
|---|------|------|---------|
| getting-started | Getting Started | 🚀 | Setup, Tutorial, Guide, How-To |
| voice-control | Voice Control Apps | 🎤 | 社媒APP控制（WhatsApp/YouTube/TikTok等） |
| use-cases | Use Cases | 📱 | 场景类（通勤/做饭/健身/带娃/脏手） |
| comparisons | Comparisons | ⚖️ | FoneClaw vs 其他工具（Siri/Google/Alexa等） |
| accessibility | Accessibility | ♿ | 老年人/视障/残障用户 |
| safety | Safety & Emergency | 🛡️ | 驾驶安全/紧急情况/隐私/智能家居 |
| industry | Industry & Trends | 📊 | AI行业分析/市场趋势/技术洞察 |

## 分配规则

新文章写完后，按以下规则分配分类：

1. **看标题和内容** → 最匹配的分类
2. **如果有疑问** → 问我确认
3. **如果没有合适分类** → 建议创建新分类

## 新分类创建条件

- 该场景有3篇以上文章潜力
- 与现有分类有明显区别
- 代表独立的用户需求

## 待扩展分类（文章≥3篇时自动显示）

| ID | 名称 | 触发条件 |
|---|------|---------|
| gaming | Gaming Automation | 挂机/自动游戏操作文章≥3篇 |
| shopping | Shopping Automation | 自动购物/比价文章≥3篇 |
| smart-home | Smart Home | 智能家居控制文章≥3篇 |

## cat_map映射表

见build_multi.py中的cat_map字典，新增分类时同步更新。
