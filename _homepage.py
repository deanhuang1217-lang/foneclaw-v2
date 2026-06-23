"""Homepage generation - FoneClaw pre-release redesign with new slogan and 120+ actions positioning."""


ZH_TRANSLATIONS = {
    'tasker-alternative-voice-automation': ('Tasker 替代方案：Android 语音自动化', '无需 root 的 Android 语音自动化方案'),
    'xiaomi-ai-ecosystem-2026': ('小米 HyperOS AI 能力 2026', '小米 HyperOS AI 生态和 MiMo 模型'),
    'voice-control-visually-impaired': ('视障用户语音控制手机指南', '视障用户的语音手机控制完全指南'),
    'gemini-intelligence-supported-devices': ('Gemini Intelligence 支持设备整理 2026', '哪些手机能用 Gemini Intelligence？一文看懂兼容范围'),
    'comp_vs_miclaw': ('小米 MiClaw vs FoneClaw 对比', '小米 MiClaw 和 FoneClaw，到底适合谁？'),
    'wwdc-2026-ai-do-over-phone-agent': ('WWDC 2026 Siri AI 和 Apple Intelligence', '苹果这次想把 Siri 带向真正的手机龙虾'),
    'agentic-ai-phone-explained': ('龙虾式 AI 手机：MiClaw、Gemini、Siri AI', '手机 AI Agent 到底能做什么？这篇讲清楚'),
    'gemini-vs-foneclaw': ('Gemini Intelligence vs FoneClaw', 'Gemini 偏理解，FoneClaw 偏执行：差别在哪？'),
    'android-vs-ios-26-5-voice-control': ('Android vs iOS：语音控制对比 2026', 'Android 和 iOS 的语音控制，到底谁更适合实用场景？'),
    'voice-control-whatsapp': ('WhatsApp 语音控制：免提指南 2026', '用语音发 WhatsApp 消息、打电话、管理聊天'),
    'gemini-intelligence-vs-siri': ('Gemini Intelligence vs Siri AI：2026 对比', 'Gemini 和 Siri AI 的路线差异，普通用户该怎么看？'),
    'foneclaw-vs-apple-intelligence': ('FoneClaw vs Apple Intelligence', '苹果做系统 AI，FoneClaw 做 Android 执行能力'),
}


JA_TRANSLATIONS = {
    'tasker-alternative-voice-automation': ('Tasker代替としてのAndroid音声自動化', 'Root不要で使える、Android向けノーコード音声自動化'),
    'xiaomi-ai-ecosystem-2026': ('小米HyperOS AI機能 2026', 'MiMo、HyperOS、スマホAIエコシステムの見方'),
    'voice-control-visually-impaired': ('視覚障害のあるユーザー向けスマホ音声操作ガイド', 'Voice Access、TalkBack、FoneClawを組み合わせた実用ガイド'),
    'gemini-intelligence-supported-devices': ('Gemini Intelligence対応端末まとめ 2026', 'どのAndroidスマホでGemini Intelligenceを使えるのか'),
    'comp_vs_miclaw': ('小米MiClaw vs FoneClaw 比較', '小米エコシステム向けMiClawと、幅広いAndroid向けFoneClawの違い'),
    'wwdc-2026-ai-do-over-phone-agent': ('WWDC 2026のSiri AIとApple Intelligence', 'AppleのスマホAI戦略をAndroidユーザー目線で読む'),
    'agentic-ai-phone-explained': ('エージェント型AIスマホとは', 'MiClaw、Gemini、Siri AIから見るスマホAIエージェントの実像'),
    'gemini-vs-foneclaw': ('Gemini Intelligence vs FoneClaw', '理解が得意なGeminiと、Android操作に寄せたFoneClawの違い'),
    'android-vs-ios-26-5-voice-control': ('Android vs iOS 音声操作比較 2026', '日常のスマホ操作ではどちらが実用的か'),
    'voice-control-whatsapp': ('WhatsApp音声操作ガイド 2026', '声でメッセージ送信、通話、チャット管理を行う方法'),
    'gemini-intelligence-vs-siri': ('Gemini Intelligence vs Siri AI 2026比較', 'GoogleとAppleのAIアシスタント戦略を比較'),
    'foneclaw-vs-apple-intelligence': ('FoneClaw vs Apple Intelligence', 'AppleのシステムAIとAndroid実行型アシスタントの違い'),
}
KO_TRANSLATIONS = {
    'tasker-alternative-voice-automation': ('Tasker 대안: Android 음성 자동화', '루트 없이 쓰는 Android 코딩 없이 음성 자동화'),
    'xiaomi-ai-ecosystem-2026': ('샤오미 HyperOS AI 기능 2026', 'MiMo, HyperOS, 스마트폰 AI 생태계 읽기'),
    'voice-control-visually-impaired': ('시각장애 사용자를 위한 스마트폰 음성 제어 가이드', 'Voice Access, TalkBack, FoneClaw를 함께 보는 실전 가이드'),
    'gemini-intelligence-supported-devices': ('Gemini Intelligence 지원 기기 정리 2026', '어떤 Android 스마트폰에서 Gemini Intelligence를 쓸 수 있는지 정리'),
    'comp_vs_miclaw': ('샤오미 MiClaw vs FoneClaw 비교', '샤오미 생태계형 MiClaw와 폭넓은 Android용 FoneClaw의 차이'),
    'wwdc-2026-ai-do-over-phone-agent': ('WWDC 2026 Siri AI와 Apple Intelligence', 'Apple의 스마트폰 AI 전략을 Android 사용자 관점에서 보기'),
    'agentic-ai-phone-explained': ('에이전트형 AI 스마트폰이란', 'MiClaw, Gemini, Siri AI로 보는 스마트폰 AI 에이전트의 실제로 달라지는 점'),
    'gemini-vs-foneclaw': ('Gemini Intelligence vs FoneClaw', '이해에 강한 Gemini와 Android 실행에 가까운 FoneClaw의 차이'),
    'android-vs-ios-26-5-voice-control': ('Android vs iOS 음성 제어 비교 2026', '일상적인 스마트폰 조작에서는 어느 쪽이 더 실용적인가'),
    'voice-control-whatsapp': ('WhatsApp 음성 제어 가이드 2026', '음성으로 메시지 전송, 통화, 채팅 관리를 하는 방법'),
    'gemini-intelligence-vs-siri': ('Gemini Intelligence vs Siri AI 2026 비교', 'Google과 Apple의 AI 어시스턴트 전략 비교'),
    'foneclaw-vs-apple-intelligence': ('FoneClaw vs Apple Intelligence', 'Apple의 시스템 AI와 Android 작업 실행형 AI 어시스턴트의 차이'),
}

TW_TRANSLATIONS = {'tasker-alternative-voice-automation': ('Tasker 替代方案：Android 語音自動化', '不用 root，也能做 Android 語音自動化'),
 'xiaomi-ai-ecosystem-2026': ('小米 HyperOS AI 能力 2026', '小米 HyperOS AI 生態與 MiMo 模型'),
 'voice-control-visually-impaired': ('視障使用者手機語音控制指南', '為視障使用者整理的手機語音控制完整指南'),
 'gemini-intelligence-supported-devices': ('Gemini Intelligence 支援裝置整理 2026', '哪些手機可以用 Gemini Intelligence？一篇看懂支援範圍'),
 'comp_vs_miclaw': ('小米 MiClaw vs FoneClaw 比較', '小米 MiClaw 和 FoneClaw，適合哪一類使用者？'),
 'wwdc-2026-ai-do-over-phone-agent': ('WWDC 2026 Siri AI 和 Apple Intelligence', 'Apple 想把 Siri 帶向真正的手機龍蝦'),
 'agentic-ai-phone-explained': ('龍蝦式 AI 手機：MiClaw、Gemini、Siri AI', '手機 AI Agent 到底能做什麼？這篇一次說清楚'),
 'gemini-vs-foneclaw': ('Gemini Intelligence vs FoneClaw', 'Gemini 偏理解，FoneClaw 偏執行：差別在哪？'),
 'android-vs-ios-26-5-voice-control': ('Android vs iOS：語音控制比較 2026', 'Android 和 iOS 的語音控制，誰更適合實用場景？'),
 'voice-control-whatsapp': ('WhatsApp 語音控制：免手動指南 2026', '用語音發 WhatsApp 訊息、打電話、管理聊天'),
 'gemini-intelligence-vs-siri': ('Gemini Intelligence vs Siri AI：2026 比較', 'Gemini 和 Siri AI 的路線差異，一般使用者該怎麼看？'),
 'foneclaw-vs-apple-intelligence': ('FoneClaw vs Apple Intelligence', 'Apple 做系統 AI，FoneClaw 做 Android 執行能力')}


ES_TRANSLATIONS = {
    'tasker-alternative-voice-automation': ('Alternativa a Tasker para automatizar Android por voz', 'Automatización de Android sin root ni scripts complejos'),
    'xiaomi-ai-ecosystem-2026': ('Ecosistema de IA de Xiaomi y HyperOS en 2026', 'MiMo, HyperOS y MiClaw vistos desde tareas reales del teléfono'),
    'voice-control-visually-impaired': ('Control por voz de Android para usuarios con discapacidad visual', 'Voice Access, TalkBack y FoneClaw con criterios de seguridad'),
    'gemini-intelligence-supported-devices': ('Dispositivos compatibles con Gemini Intelligence en 2026', 'Compatibilidad de IA frente a acciones reales en Android'),
    'comp_vs_miclaw': ('Xiaomi MiClaw vs FoneClaw: comparación para Android', 'Ecosistema Xiaomi frente a acciones Android más amplias'),
    'wwdc-2026-ai-do-over-phone-agent': ('WWDC 2026, Siri AI y Apple Intelligence vistos desde Android', 'Qué significan los cambios de Apple para agentes de teléfono'),
    'agentic-ai-phone-explained': ('Qué es un teléfono con IA agentiva', 'De responder preguntas a ejecutar acciones del teléfono'),
    'gemini-vs-foneclaw': ('Gemini Intelligence vs FoneClaw: entender o ejecutar', 'Comprensión de información frente a acciones Android'),
    'android-vs-ios-26-5-voice-control': ('Android vs iOS: control por voz en 2026', 'Comparativa práctica de voz, accesibilidad y automatización'),
    'voice-control-whatsapp': ('Control por voz de WhatsApp en Android', 'Mensajes, llamadas y confirmación con límites claros'),
    'gemini-intelligence-vs-siri': ('Gemini Intelligence vs Siri AI en 2026', 'Estrategias de Google y Apple para asistentes de IA'),
    'foneclaw-vs-apple-intelligence': ('FoneClaw vs Apple Intelligence', 'Integración de iOS frente a ejecución práctica en Android'),
}

PT_TRANSLATIONS = {
    'tasker-alternative-voice-automation': ('Alternativa ao Tasker para automatizar Android por voz', 'Automação Android sem root nem scripts complexos'),
    'xiaomi-ai-ecosystem-2026': ('Ecossistema de IA da Xiaomi e HyperOS em 2026', 'MiMo, HyperOS e MiClaw vistos por tarefas reais do telefone'),
    'voice-control-visually-impaired': ('Controle por voz do Android para usuários com deficiência visual', 'Voice Access, TalkBack e FoneClaw com critérios de segurança'),
    'gemini-intelligence-supported-devices': ('Dispositivos compatíveis com Gemini Intelligence em 2026', 'Compatibilidade de IA frente a ações reais no Android'),
    'comp_vs_miclaw': ('Xiaomi MiClaw vs FoneClaw: comparação para Android', 'Ecossistema Xiaomi frente a ações Android mais amplas'),
    'wwdc-2026-ai-do-over-phone-agent': ('WWDC 2026, Siri AI e Apple Intelligence vistos do Android', 'O que as mudanças da Apple significam para agentes de telefone'),
    'agentic-ai-phone-explained': ('O que é um telefone com IA agentiva', 'De responder perguntas a executar ações do telefone'),
    'gemini-vs-foneclaw': ('Gemini Intelligence vs FoneClaw: entender ou executar', 'Compreensão de informação frente a ações Android'),
    'android-vs-ios-26-5-voice-control': ('Android vs iOS: controle por voz em 2026', 'Comparativo prático de voz, acessibilidade e automação'),
    'voice-control-whatsapp': ('Controle por voz do WhatsApp no Android', 'Mensagens, chamadas e confirmação com limites claros'),
    'gemini-intelligence-vs-siri': ('Gemini Intelligence vs Siri AI em 2026', 'Estratégias de Google e Apple para assistentes de IA'),
    'foneclaw-vs-apple-intelligence': ('FoneClaw vs Apple Intelligence', 'Integração do iOS frente à execução prática no Android'),
}

FR_TRANSLATIONS = {
    'tasker-alternative-voice-automation': ('Alternative à Tasker pour l\'automatisation vocale', 'Automatisation Android sans root ni scripts complexes'),
    'xiaomi-ai-ecosystem-2026': ('L\'écosystème IA Xiaomi et HyperOS en 2026', 'MiMo, HyperOS et MiClaw du point de vue des tâches réelles'),
    'voice-control-visually-impaired': ('Commande vocale Android pour les malvoyants', 'Voice Access, TalkBack et FoneClaw avec critères de sécurité'),
    'gemini-intelligence-supported-devices': ('Appareils compatibles Gemini Intelligence en 2026', 'Compatibilité IA vs actions réelles sur Android'),
    'comp_vs_miclaw': ('Xiaomi MiClaw vs FoneClaw : comparaison', 'Écosystème Xiaomi vs actions Android plus larges'),
    'wwdc-2026-ai-do-over-phone-agent': ('WWDC 2026, Siri AI et Apple Intelligence', 'Ce que les changements d\'Apple signifient pour les agents téléphoniques'),
    'agentic-ai-phone-explained': ('Qu\'est-ce qu\'un téléphone avec agent IA', 'Des réponses aux questions à l\'exécution d\'actions sur le téléphone'),
    'gemini-vs-foneclaw': ('Gemini Intelligence vs FoneClaw', 'Comprendre l\'information vs actions réelles sur Android'),
    'android-vs-ios-26-5-voice-control': ('Android vs iOS : commande vocale en 2026', 'Comparaison pratique de la voix, de l\'accessibilité et de l\'automatisation'),
    'voice-control-whatsapp': ('Commande vocale WhatsApp sur Android', 'Messages, appels et confirmation avec des limites claires'),
    'gemini-intelligence-vs-siri': ('Gemini Intelligence vs Siri AI en 2026', 'Stratégies Google et Apple pour les assistants IA'),
    'foneclaw-vs-apple-intelligence': ('FoneClaw vs Apple Intelligence', 'Intégration iOS vs exécution pratique sur Android'),
}

DE_TRANSLATIONS = {
    'tasker-alternative-voice-automation': ('Tasker Alternative: Android-Sprachsteuerung', 'Modernen Ansatz für Sprachsteuerung auf Android ohne komplexe Skripte', 'Vergleich', '9 min'),
    'xiaomi-ai-ecosystem-2026': ('Xiaomi KI-Ökosystem 2026', 'MiMo, HyperOS und MiClaw aus der Praxisperspektive', 'Industrie', '9 min'),
    'voice-control-visually-impaired': ('Sprachsteuerung für Sehbehinderte', 'Voice Access, TalkBack und FoneClaw mit Sicherheitskriterien', 'Barrierefreiheit', '9 min'),
    'gemini-intelligence-supported-devices': ('Gemini Intelligence Geräte 2026', 'KI-Fähigkeiten vs praktische Aktionen auf Android', 'Industrie', '10 min'),
    'comp_vs_miclaw': ('MiClaw vs FoneClaw Vergleich', 'Xiaomi-Ökosystem vs breitere Android-Aktionen', 'Vergleich', '7 min'),
    'wwdc-2026-ai-do-over-phone-agent': ('WWDC 2026: Siri AI & Apple Intelligence', 'Was Apples Änderungen für Smartphone-Agenten bedeuten', 'Industrie', '10 min'),
    'agentic-ai-phone-explained': ('Agentic KI auf dem Smartphone', 'Von der Fragebeantwortung zur Aktionen-Ausführung', 'Leitfaden', '9 min'),
    'gemini-vs-foneclaw': ('Gemini vs FoneClaw', 'Information analysieren vs konkrete Aktionen ausführen', 'Vergleich', '9 min'),
    'android-vs-ios-26-5-voice-control': ('Android vs iOS Sprachsteuerung 2026', 'Praxisvergleich von Sprache, Barrierefreiheit und Automatisierung', 'Vergleich', '8 min'),
    'voice-control-whatsapp': ('WhatsApp Sprachsteuerung Android', 'Nachrichten, Anrufe und Bestätigung mit klaren Grenzen', 'Leitfaden', '7 min'),
    'gemini-intelligence-vs-siri': ('Gemini Intelligence vs Siri AI 2026', 'KI-Strategien von Google und Apple', 'Industrie', '8 min'),
    'foneclaw-vs-apple-intelligence': ('FoneClaw vs Apple Intelligence', 'iOS-Integration vs praktische Android-Ausführung', 'Vergleich', '8 min'),
}

AR_TRANSLATIONS = {
    'tasker-alternative-voice-automation': ('بديل Tasker لأتمتة الصوت على أندرويد', 'هل تبحث عن بديل لـ Tasker للتحكم في هاتفك بالصوت؟ FoneClaw — مساعد ذكاء اصطناعي بأكثر من 120 إجراء على أندرويد بدون سكريبتات معقدة.', 'مقارنة', '9 دقائق'),
    'xiaomi-ai-ecosystem-2026': ('نظام Xiaomi الذكي 2026: نظرة عملية', 'نظرة على نظام Xiaomi الذكي في 2026: HyperOS، المساعد الصوتي، التكامل مع المنزل الذكي. كيف يكمل FoneClaw إمكانيات Xiaomi.', 'صناعة', '9 دقائق'),
    'voice-control-visually-impaired': ('التحكم الصوتي للمكفوفين وضعاف البصر', 'كيف يمكن للمكفوفين وضعاف البصر التحكم في هاتف أندرويد بالصوت باستخدام FoneClaw. دليل شامل لإمكانية الوصول.', 'إمكانية الوصول', '9 دقائق'),
    'gemini-intelligence-supported-devices': ('أجهزة Gemini Intelligence: مراجعة شاملة', 'قائمة كاملة لأجهزة Gemini Intelligence في 2026. ما هي الهواتف التي ستحصل على ميزات Google الذكية وكيف يكملها FoneClaw.', 'صناعة', '10 دقائق'),
    'comp_vs_miclaw': ('MiClaw مقابل FoneClaw: ما الاختيار في 2026', 'مقارنة Xiaomi MiClaw و FoneClaw: النظام البيئي مقابل حرية الاختيار. تحليل الإمكانيات والتوافق والراحة الفعلية للمستخدم.', 'مقارنة', '7 دقائق'),
    'wwdc-2026-ai-do-over-phone-agent': ('WWDC 2026: Siri AI من منظور مستخدم أندرويد', 'قدمت Apple مساعد Siri المحدث في WWDC 2026. نحلل ما تغير، المقارنة مع مساعدي أندرويد، وهل يستحق الأمر الغيرة.', 'صناعة', '10 دقائق'),
    'agentic-ai-phone-explained': ('الذكاء الاصطناعي الوكيل على الهاتف: شرح بسيط', 'ما هو الذكاء الاصطناعي الوكيل وكيف يعمل على الهاتف. نشرح بأمثلة من MiClaw و Gemini و Siri AI و FoneClaw.', 'دليل', '9 دقائق'),
    'gemini-vs-foneclaw': ('Gemini مقابل FoneClaw: تحليل مقابل فعل', 'Gemini Intelligence يحلل ويفهم، FoneClaw ينفذ ويعمل. نحلل نقاط قوة كل مساعد ومتى تستخدم كلًا منهما.', 'مقارنة', '9 دقائق'),
    'android-vs-ios-26-5-voice-control': ('أندرويد مقابل iOS: التحكم الصوتي 2026', 'نقارن التحكم الصوتي في أندرويد و iOS في 2026. اختبارات حقيقية ونصائح عملية ونظرة موضوعية على كلا المنصتين.', 'مقارنة', '8 دقائق'),
    'voice-control-whatsapp': ('التحكم الصوتي في WhatsApp على أندرويد', 'دليل شامل للتحكم الصوتي في WhatsApp على أندرويد. أرسل رسائل واتصل وأدر المحادثات دون لمس الشاشة.', 'دليل', '7 دقائق'),
    'gemini-intelligence-vs-siri': ('Gemini Intelligence مقابل Siri AI 2026', 'نقارن استراتيجيات Google و Apple في مساعدي الذكاء الاصطناعي. Gemini Intelligence و Siri في 2026: من يقود سباق الذكاء الاصطناعي؟', 'صناعة', '8 دقائق'),
    'foneclaw-vs-apple-intelligence': ('FoneClaw مقابل Apple Intelligence', 'نقارن FoneClaw على أندرويد و Apple Intelligence على iOS. الذكاء الاصطناعي المندمج من Apple مقابل حرية عمل FoneClaw — من الأكثر فعالية؟', 'مقارنة', '8 دقائق'),
}

RU_TRANSLATIONS = {
    'tasker-alternative-voice-automation': ('Альтернатива Tasker для голосовой автоматизации', 'Ищете замену Tasker для управления смартфоном голосом? FoneClaw — AI-ассистент с 120+ действиями на Android без сложных скриптов и настроек.', 'Сравнение', '9 мин'),
    'xiaomi-ai-ecosystem-2026': ('Экосистема AI Xiaomi 2026: обзор и перспективы', 'Обзор AI-экосистемы Xiaomi в 2026 году: HyperOS, голосовой ассистент, интеграция с умным домом. Как FoneClaw дополняет возможности Xiaomi.', 'Индустрия', '9 мин'),
    'voice-control-visually-impaired': ('Голосовое управление телефоном для слабовидящих', 'Как незрячие и слабовидящие пользователи могут управлять Android смартфоном голосом с помощью FoneClaw. Полное руководство по доступности.', 'Доступность', '9 мин'),
    'gemini-intelligence-supported-devices': ('Устройства с Gemini Intelligence: полный обзор', 'Полный список устройств с поддержкой Gemini Intelligence в 2026 году. Какие смартфоны и планшеты получат AI-функции Google и чем дополнить их FoneClaw.', 'Руководство', '9 мин'),
    'comp_vs_miclaw': ('MiClaw vs FoneClaw: что выбрать в 2026', 'Сравнение Xiaomi MiClaw и FoneClaw: экосистема против свободы выбора. Анализ возможностей, совместимости и реального удобства для пользователя.', 'Сравнение', '9 мин'),
    'wwdc-2026-ai-do-over-phone-agent': ('WWDC 2026: Siri AI глазами пользователя Android', 'Apple представила обновлённый Siri на WWDC 2026. Разбираем, что изменилось, сравнение с Android-ассистентами и стоит ли завидовать пользователям iPhone.', 'Индустрия', '10 мин'),
    'agentic-ai-phone-explained': ('Агентный AI на телефоне: простое объяснение', 'Что такое агентный AI и как он работает на смартфоне. Объясняем на примерах MiClaw, Gemini, Siri AI и FoneClaw без сложных терминов.', 'Руководство', '9 мин'),
    'gemini-vs-foneclaw': ('Gemini vs FoneClaw: анализ vs действие', 'Gemini Intelligence анализирует и понимает, FoneClaw выполняет и действует. Разбираем сильные стороны каждого ассистента и когда какой использовать.', 'Сравнение', '9 мин'),
    'android-vs-ios-26-5-voice-control': ('Android vs iOS: голосовое управление 2026', 'Сравниваем голосовое управление Android и iOS в 2026 году. Реальные тесты, практичные советы и объективный взгляд на обе платформы.', 'Сравнение', '8 мин'),
    'voice-control-whatsapp': ('Голосовое управление WhatsApp на Android', 'Полный гид по голосовому управлению WhatsApp на Android. Отправляйте сообщения, звоните и управляйте чатами без касания экрана.', 'Руководство', '7 мин'),
    'gemini-intelligence-vs-siri': ('Gemini Intelligence vs Siri: битва ИИ', 'Сравниваем стратегии Google и Apple в области ИИ-ассистентов. Gemini Intelligence и Siri в 2026 году: кто ведёт в гонке искусственного интеллекта?', 'Индустрия', '8 мин'),
    'foneclaw-vs-apple-intelligence': ('FoneClaw vs Apple Intelligence: ИИ бой', 'Сравниваем FoneClaw на Android и Apple Intelligence на iOS. Системный ИИ Apple против свободы действий FoneClaw — кто эффективнее?', 'Сравнение', '8 мин'),
}

VI_TRANSLATIONS = {'tasker-alternative-voice-automation': ('Thay Tasker bằng giọng nói Android', 'Cách chọn phương án thay Tasker cho Android bằng giọng nói, không cần root, có xác nhận trước thao tác nhạy cảm và phù hợp người dùng Việt.', 'Hướng dẫn', '10 phút'), 'xiaomi-ai-ecosystem-2026': ('Hệ sinh thái AI Xiaomi năm 2026', 'Phân tích HyperOS, MiMo, MiClaw và vai trò của FoneClaw cho người dùng Android muốn điều khiển điện thoại bằng giọng nói rõ ràng hơn.', 'Phân tích', '10 phút'), 'voice-control-visually-impaired': ('Điều khiển Android bằng giọng nói cho người khiếm thị', 'Hướng dẫn dùng Voice Access, TalkBack và FoneClaw để người khiếm thị thao tác Android an toàn, có ngữ cảnh và có bước xác nhận.', 'Trợ năng', '11 phút'), 'gemini-intelligence-supported-devices': ('Thiết bị hỗ trợ Gemini Intelligence', 'Danh sách và cách hiểu thiết bị hỗ trợ Gemini Intelligence, khác biệt giữa khả năng AI của Google và thao tác Android thực tế với FoneClaw.', 'Phân tích', '10 phút'), 'comp_vs_miclaw': ('MiClaw và FoneClaw khác gì?', 'So sánh MiClaw trong hệ sinh thái Xiaomi với FoneClaw độc lập cho Android: phạm vi thiết bị, quyền, thao tác giọng nói và cách chọn.', 'So sánh', '9 phút'), 'wwdc-2026-ai-do-over-phone-agent': ('WWDC 2026 và trợ lý điện thoại AI', 'Nhìn WWDC 2026, Siri AI và Apple Intelligence từ góc độ người dùng Android cần trợ lý điện thoại biết thao tác chứ không chỉ trả lời.', 'Phân tích', '10 phút'), 'agentic-ai-phone-explained': ('AI Agent trên điện thoại là gì?', 'Giải thích AI Agent trên điện thoại bằng ví dụ Gemini, Siri, MiClaw và FoneClaw: khác gì chatbot và cần kiểm soát ra sao.', 'Hướng dẫn', '10 phút'), 'gemini-vs-foneclaw': ('Gemini và FoneClaw: hiểu hay làm', 'So sánh Gemini Intelligence và FoneClaw trên Android: một bên mạnh về hiểu thông tin, một bên tập trung vào thao tác điện thoại có kiểm chứng.', 'So sánh', '9 phút'), 'android-vs-ios-26-5-voice-control': ('Android và iOS: điều khiển giọng nói', 'So sánh điều khiển giọng nói trên Android và iOS năm 2026, từ trợ năng, tự động hóa tới khả năng cho trợ lý AI thao tác thật.', 'So sánh', '9 phút'), 'voice-control-whatsapp': ('Điều khiển WhatsApp bằng giọng nói', 'Cách dùng giọng nói để chuẩn bị tin nhắn, gọi điện và quản lý WhatsApp trên Android với giới hạn an toàn và xác nhận rõ ràng.', 'Ứng dụng', '9 phút'), 'gemini-intelligence-vs-siri': ('Gemini Intelligence và Siri AI', 'So sánh chiến lược trợ lý AI của Google và Apple trong năm 2026, và vì sao người dùng Android vẫn cần lớp thao tác như FoneClaw.', 'So sánh', '9 phút'), 'foneclaw-vs-apple-intelligence': ('FoneClaw và Apple Intelligence', 'So sánh FoneClaw trên Android với Apple Intelligence trên iOS: tích hợp hệ điều hành, phạm vi thao tác và quyền kiểm soát người dùng.', 'So sánh', '9 phút')}

TH_TRANSLATIONS = {'tasker-alternative-voice-automation': ('ทางเลือก Tasker สำหรับสั่ง Android ด้วยเสียง', 'อัตโนมัติบน Android โดยไม่ต้อง root หรือเขียนสคริปต์', 'คู่มือ', '9 นาที'), 'xiaomi-ai-ecosystem-2026': ('ระบบ AI ของ Xiaomi และ HyperOS ปี 2026', 'มอง MiMo, HyperOS และ MiClaw ผ่านงานมือถือจริง', 'อุตสาหกรรม', '9 นาที'), 'voice-control-visually-impaired': ('สั่งงาน Android ด้วยเสียงสำหรับผู้พิการทางสายตา', 'คู่มือ Voice Access, TalkBack และ FoneClaw อย่างปลอดภัย', 'การเข้าถึง', '9 นาที'), 'gemini-intelligence-supported-devices': ('อุปกรณ์ที่รองรับ Gemini Intelligence', 'ความเข้ากันได้ของ AI เทียบกับการทำงานจริงบน Android', 'อุตสาหกรรม', '10 นาที'), 'comp_vs_miclaw': ('MiClaw vs FoneClaw สำหรับ Android', 'ระบบ Xiaomi เทียบกับการทำงาน Android ที่กว้างกว่า', 'เปรียบเทียบ', '8 นาที'), 'wwdc-2026-ai-do-over-phone-agent': ('WWDC 2026, Siri AI และ Apple Intelligence', 'สิ่งที่ Apple เปลี่ยนมีความหมายอย่างไรต่อผู้ช่วยมือถือ', 'อุตสาหกรรม', '10 นาที'), 'agentic-ai-phone-explained': ('AI Agent บนมือถือคืออะไร', 'จากการตอบคำถามไปสู่การลงมือทำงานบนมือถือ', 'คู่มือ', '9 นาที'), 'gemini-vs-foneclaw': ('Gemini vs FoneClaw: เข้าใจหรือทำงาน', 'การเข้าใจข้อมูลเทียบกับการสั่งงาน Android จริง', 'เปรียบเทียบ', '9 นาที'), 'android-vs-ios-26-5-voice-control': ('Android vs iOS: สั่งงานด้วยเสียง 2026', 'เปรียบเทียบเสียง การเข้าถึง และอัตโนมัติแบบใช้งานจริง', 'เปรียบเทียบ', '8 นาที'), 'voice-control-whatsapp': ('สั่งงาน WhatsApp ด้วยเสียงบน Android', 'ข้อความ โทร และการยืนยันด้วยขอบเขตที่ชัดเจน', 'คู่มือ', '8 นาที'), 'gemini-intelligence-vs-siri': ('Gemini Intelligence vs Siri AI 2026', 'กลยุทธ์ผู้ช่วย AI ของ Google และ Apple', 'อุตสาหกรรม', '8 นาที'), 'foneclaw-vs-apple-intelligence': ('FoneClaw vs Apple Intelligence', 'การฝังลึกใน iOS เทียบกับการทำงานจริงบน Android', 'เปรียบเทียบ', '8 นาที')}

ID_TRANSLATIONS = {'tasker-alternative-voice-automation': ('Alternatif Tasker untuk Otomatisasi Suara Android', 'Cara memilih pengganti Tasker untuk Android lewat suara, tanpa root, dengan konfirmasi sebelum aksi sensitif dan cocok untuk pengguna Indonesia.', 'Panduan', '10 menit'), 'xiaomi-ai-ecosystem-2026': ('Ekosistem AI Xiaomi Tahun 2026', 'Analisis HyperOS, MiMo, MiClaw dan peran FoneClaw bagi pengguna Android yang ingin mengendalikan ponsel lewat suara dengan lebih jelas.', 'Analisis', '10 menit'), 'voice-control-visually-impaired': ('Kontrol Android Lewat Suara untuk Tunanetra', 'Panduan Voice Access, TalkBack dan FoneClaw agar tunanetra dapat mengoperasikan Android dengan aman, berkonteks dan ada langkah konfirmasi.', 'Aksesibilitas', '11 menit'), 'gemini-intelligence-supported-devices': ('Perangkat yang Mendukung Gemini Intelligence', 'Daftar dan cara memahami perangkat yang mendukung Gemini Intelligence, perbedaan kemampuan AI Google dan pengoperasian Android sesungguhnya dengan FoneClaw.', 'Analisis', '10 menit'), 'comp_vs_miclaw': ('MiClaw dan FoneClaw Apa Bedanya?', 'Perbandingan MiClaw dalam ekosistem Xiaomi dengan FoneClaw independen untuk Android: cakupan perangkat, izin, aksi suara dan cara memilih.', 'Perbandingan', '9 menit'), 'wwdc-2026-ai-do-over-phone-agent': ('WWDC 2026 dan Asisten Ponsel AI', 'Melihat WWDC 2026, Siri AI dan Apple Intelligence dari sudut pandang pengguna Android yang butuh asisten ponsel bisa mengoperasikan bukan hanya menjawab.', 'Analisis', '10 menit'), 'agentic-ai-phone-explained': ('Apa Itu AI Agent di Ponsel?', 'Penjelasan AI Agent di ponsel dengan contoh Gemini, Siri, MiClaw dan FoneClaw: bedanya dengan chatbot dan perlu kontrol seperti apa.', 'Panduan', '10 menit'), 'gemini-vs-foneclaw': ('Gemini dan FoneClaw: Memahami atau Mengerjakan', 'Perbandingan Gemini Intelligence dan FoneClaw di Android: satu sisi kuat memahami informasi, sisi lain fokus mengoperasikan ponsel secara nyata.', 'Perbandingan', '9 menit'), 'android-vs-ios-26-5-voice-control': ('Android dan iOS: Kontrol Suara 2026', 'Perbandingan kontrol suara di Android dan iOS tahun 2026. Uji coba nyata, tips praktis dan pandangan objektif terhadap kedua platform.', 'Perbandingan', '8 menit'), 'voice-control-whatsapp': ('Kontrol Suara WhatsApp di Android', 'Panduan lengkap kontrol suara WhatsApp di Android. Kirim pesan, telepon dan kelola obrolan tanpa menyentuh layar.', 'Panduan', '8 menit'), 'gemini-intelligence-vs-siri': ('Gemini Intelligence vs Siri AI 2026', 'Perbandingan strategi Google dan Apple dalam asisten AI. Gemini Intelligence dan Siri di 2026: siapa yang memimpin?', 'Industri', '8 menit'), 'foneclaw-vs-apple-intelligence': ('FoneClaw vs Apple Intelligence', 'Perbandingan FoneClaw di Android dan Apple Intelligence di iOS. AI tertanam Apple versus kebebasan aksi FoneClaw — mana yang lebih efektif?', 'Perbandingan', '8 menit')}

def _build_article_cards(articles, lang='en'):
    """Build HTML for article cards with hub-style design."""
    # slug → (url, image) overrides for mismatched paths
    overrides = {
        'voice-control-visually-impaired': ('voice-control-visually-impaired', 'uc_visual_impaired'),
        'gemini-vs-foneclaw': ('gemini-vs-foneclaw', 'comp_vs_gemini'),
        'comp_vs_miclaw': ('miclaw-vs-foneclaw', 'comp_vs_miclaw'),
    }
    cards = []
    for slug, title, desc, cat, read_time in articles:
        if lang == 'ru' and slug in RU_TRANSLATIONS:
            title, desc, cat, read_time = RU_TRANSLATIONS[slug]
        elif lang == 'de' and slug in DE_TRANSLATIONS:
            title, desc, cat, read_time = DE_TRANSLATIONS[slug]
        elif lang == 'ar' and slug in AR_TRANSLATIONS:
            title, desc, cat, read_time = AR_TRANSLATIONS[slug]
        elif lang == 'vi' and slug in VI_TRANSLATIONS:
            title, desc, cat, read_time = VI_TRANSLATIONS[slug]
        elif lang == 'th' and slug in TH_TRANSLATIONS:
            title, desc, cat, read_time = TH_TRANSLATIONS[slug]
        elif lang == 'id' and slug in ID_TRANSLATIONS:
            title, desc, cat, read_time = ID_TRANSLATIONS[slug]
        elif lang == 'fr' and slug in FR_TRANSLATIONS:
            title, desc = FR_TRANSLATIONS[slug]
        elif lang == 'pt' and slug in PT_TRANSLATIONS:
            title, desc = PT_TRANSLATIONS[slug]
        elif lang == 'es' and slug in ES_TRANSLATIONS:
            title, desc = ES_TRANSLATIONS[slug]
        elif lang == 'ko' and slug in KO_TRANSLATIONS:
            title, desc = KO_TRANSLATIONS[slug]
        elif lang == 'ja' and slug in JA_TRANSLATIONS:
            title, desc = JA_TRANSLATIONS[slug]
        elif lang == 'tw' and slug in TW_TRANSLATIONS:
            title, desc = TW_TRANSLATIONS[slug]
        elif lang == 'zh' and slug in ZH_TRANSLATIONS:
            title, desc = ZH_TRANSLATIONS[slug]
        read_label = {'ru':'Читать','fr':'Lire','de':'Lesen','vi':'Đọc','th':'อ่าน','ar':'اقرأ','pt':'Ler','es':'Leer','ko':'읽기','ja':'読む','tw':'閱讀','zh':'阅读','id':'Baca'}.get(lang, 'Read')
        prefix = {'ru':'/ru','fr':'/fr','de':'/de','vi':'/vi','th':'/th','ar':'/ar','pt':'/pt','es':'/es','ko':'/ko','ja':'/ja','tw':'/tw','zh':'/zh','id':'/id'}.get(lang, '')
        url_slug, img_slug = overrides.get(slug, (slug, slug))
        if lang in ('zh', 'tw', 'ja', 'ko', 'es', 'pt', 'ru', 'fr', 'de', 'ar', 'th', 'vi', 'id') and slug == 'comp_vs_miclaw':
            url_slug = 'comp_vs_miclaw'
        if lang in ('zh', 'tw', 'ja', 'ko', 'es', 'pt', 'ru', 'fr', 'de', 'ar', 'th', 'vi', 'id'):
            read_time = str(read_time).replace(' min', ' min' if lang in ('es','pt','fr','de','ar','th','vi','id') else ('분' if lang == 'ko' else ('分' if lang == 'ja' else (' 分鐘' if lang == 'tw' else ' 分钟'))))
            ja_cat = {'Setup': '設定','Industry': '業界','Use Cases': '活用例','Comparison': '比較','Apps': 'アプリ','Guide': 'ガイド','Safety': '安全','Accessibility': 'アクセシビリティ'}
            zh_cat = {'Setup': '设置','Industry': '行业','Use Cases': '使用场景','Comparison': '对比','Apps': '应用','Guide': '指南','Safety': '安全','Accessibility': '无障碍'}
            tw_cat = {'Setup': '設定','Industry': '產業','Use Cases': '使用情境','Comparison': '比較','Apps': 'App','Guide': '指南','Safety': '安全','Accessibility': '無障礙'}
            ko_cat = {'Setup': '설정','Industry': '업계','Use Cases': '활용 사례','Comparison': '비교','Apps': '앱','Guide': '가이드','Safety': '안전','Accessibility': '접근성'}
            es_cat = {'Setup': 'Guía','Industry': 'Industria','Use Cases': 'Casos de uso','Comparison': 'Comparativa','Apps': 'Apps','Guide': 'Guía','Safety': 'Seguridad','Accessibility': 'Accesibilidad'}
            pt_cat = {'Setup': 'Guia','Industry': 'Indústria','Use Cases': 'Casos de uso','Comparison': 'Comparativo','Apps': 'Apps','Guide': 'Guia','Safety': 'Segurança','Accessibility': 'Acessibilidade'}
            ru_cat = {'Setup': 'Руководство','Industry': 'Индустрия','Use Cases': 'Сценарии','Comparison': 'Сравнение','Apps': 'Приложения','Guide': 'Руководство','Safety': 'Безопасность','Accessibility': 'Доступность'}
            de_cat = {'Setup': 'Leitfaden','Industrie': 'Industrie','Use Cases': 'Anwendungsfälle','Comparison': 'Vergleich','Apps': 'Apps','Guide': 'Leitfaden','Safety': 'Sicherheit','Accessibility': 'Barrierefreiheit'}
            fr_cat = {'Setup': 'Guide','Industry': 'Industrie','Use Cases': 'Cas d\'usage','Comparison': 'Comparaison','Apps': 'Applications','Guide': 'Guide','Safety': 'Sécurité','Accessibility': 'Accessibilité'}
            ar_cat = {'Setup': 'إعداد','Industry': 'صناعة','Use Cases': 'حالات الاستخدام','Comparison': 'مقارنة','Apps': 'تطبيقات','Guide': 'دليل','Safety': 'أمان','Accessibility': 'إمكانية الوصول'}
            th_cat = {'Setup': 'คู่มือ','Industry': 'อุตสาหกรรม','Use Cases': 'กรณีใช้งาน','Comparison': 'เปรียบเทียบ','Apps': 'แอป','Guide': 'คู่มือ','Safety': 'ความปลอดภัย','Accessibility': 'การเข้าถึง'}
            vi_cat = {'Setup': 'Hướng dẫn','Industry': 'Phân tích','Use Cases': 'Tình huống dùng','Comparison': 'So sánh','Apps': 'Ứng dụng','Guide': 'Hướng dẫn','Safety': 'An toàn','Accessibility': 'Trợ năng'}
            id_cat = {'Setup': 'Panduan','Industry': 'Industri','Use Cases': 'Kasus Penggunaan','Comparison': 'Perbandingan','Apps': 'Aplikasi','Guide': 'Panduan','Safety': 'Keamanan','Accessibility': 'Aksesibilitas'}
            cat = (id_cat if lang == 'id' else (vi_cat if lang == 'vi' else (th_cat if lang == 'th' else (ar_cat if lang == 'ar' else (de_cat if lang == 'de' else (fr_cat if lang == 'fr' else (ru_cat if lang == 'ru' else (pt_cat if lang == 'pt' else (es_cat if lang == 'es' else (ko_cat if lang == 'ko' else (ja_cat if lang == 'ja' else (tw_cat if lang == 'tw' else zh_cat)))))))))))).get(cat, cat)
        img_html = f'<img class="article-card-img" src="/images/articles/{img_slug}.jpg" alt="{title}" loading="lazy" onerror="this.style.display=\'none\'">'
        cards.append(
            f'<a href="{prefix}/{url_slug}.html" class="article-card">'
            f'{img_html}'
            f'<div class="article-card-body">'
            f'<span class="article-card-tag">{cat}</span>'
            f'<h4>{title}</h4>'
            f'<p>{desc[:120]}</p>'
            f'</div>'
            f'<div class="article-card-meta"><span>⏱ {read_time}</span><span class="read-link">{read_label} →</span></div>'
            f'</a>'
        )
    return '\n      '.join(cards)


def generate_homepage(full_page, base, imgs=None, lang='en'):
    """Generate the homepage using full_page()."""
    from _i18n import get_text, generate_hreflang_tags

    t = lambda key: get_text('homepage', key, lang)

    # Featured articles — from Google Sheet optimization tracking
    featured_articles = [
        ('tasker-alternative-voice-automation', 'Tasker Alternative: Android Voice Automation', 'No-code voice automation for Android without root access.', 'Setup', '6 min'),
        ('xiaomi-ai-ecosystem-2026', 'Xiaomi HyperOS AI Capabilities 2026', 'MiMo model, HyperOS integration, and the Xiaomi app ecosystem.', 'Industry', '9 min'),
        ('voice-control-visually-impaired', 'Voice Activated Phone for Blind Users', '100% voice control for accessibility — Voice Access, TalkBack, and more.', 'Use Cases', '9 min'),
        ('gemini-intelligence-supported-devices', 'Gemini Intelligence Supported Devices List 2026', 'Which phones support Gemini Intelligence and what you need.', 'Industry', '10 min'),
        ('comp_vs_miclaw', 'Xiaomi MiClaw vs FoneClaw Phone Agent', 'Closed beta vs open Android — MiClaw, MiMo, and HyperOS lock-in.', 'Comparison', '7 min'),
        ('wwdc-2026-ai-do-over-phone-agent', 'WWDC 2026 Siri AI and Apple Intelligence', 'What Apple announced and what it means for phone agents.', 'Industry', '7 min'),
        ('agentic-ai-phone-explained', 'Agentic AI Phone: MiClaw, Gemini, Siri AI', 'What agentic AI means for your phone in 2026.', 'Industry', '8 min'),
        ('gemini-vs-foneclaw', 'Gemini Intelligence vs FoneClaw', 'Can Gemini Intelligence control Android apps like FoneClaw?', 'Comparison', '6 min'),
        ('android-vs-ios-26-5-voice-control', 'Android vs iOS: Voice Control Compared 2026', 'Voice assistant integration across platforms — who wins?', 'Comparison', '6 min'),
        ('voice-control-whatsapp', 'WhatsApp Voice Control: Hands-Free Guide 2026', 'Send messages, make calls, and manage chats with voice.', 'Apps', '7 min'),
        ('gemini-intelligence-vs-siri', 'Gemini Intelligence vs Siri AI: 2026 Comparison', 'WWDC 2026, Gemini-powered Siri, and what it means for Android.', 'Comparison', '20 min'),
        ('foneclaw-vs-apple-intelligence', 'FoneClaw vs Apple Intelligence', 'Siri AI vs Android agent — App Intents vs cross-app control.', 'Comparison', '12 min'),
    ]
    article_cards_html = _build_article_cards(featured_articles, lang=lang)

    _free_label = {'ru':'Бесплатно','fr':'Gratuit','de':'Kostenlos','vi':'Miễn phí','th':'ฟรี','ar':'مجاني','pt':'Grátis','es':'Gratis','ko':'무료','ja':'無料','tw':'免費','zh':'免费','id':'Gratis'}.get(lang, 'Free')

    extra_css = '''<style>
:root{--bg:#070914;--bg2:#0b1020;--panel:#101624;--panel2:#151c2d;--line:rgba(255,255,255,.09);--line2:rgba(0,212,255,.18);--text:#f7f8fb;--muted:#9aa4b2;--soft:#cbd5e1;--cyan:#00d4ff;--green:#3fb950;--violet:#7c7cff;--amber:#f7b955;--danger:#ff6b8a;--radius:24px}
body:before{content:"";position:fixed;inset:0;pointer-events:none;background:radial-gradient(circle at 20% 0%,rgba(0,212,255,.16),transparent 32%),radial-gradient(circle at 84% 8%,rgba(124,124,255,.15),transparent 34%),radial-gradient(circle at 50% 100%,rgba(63,185,80,.08),transparent 36%);z-index:-2}
body:after{content:"";position:fixed;inset:0;background-image:linear-gradient(rgba(255,255,255,.025) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.025) 1px,transparent 1px);background-size:56px 56px;mask-image:linear-gradient(to bottom,rgba(0,0,0,.72),transparent 72%);pointer-events:none;z-index:-1}
/* Hero */
.hero{padding:120px 0 80px;text-align:center}
.hero h1{font-size:clamp(48px,8vw,72px);font-weight:800;line-height:1.05;letter-spacing:-.04em;margin-bottom:20px}
.hero .grad{background:linear-gradient(135deg,var(--cyan),var(--green));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero .lead{font-size:18px;color:var(--soft);line-height:1.7;max-width:580px;margin:0 auto 32px}
.hero .btns{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-bottom:48px}
.bp{padding:14px 32px;background:linear-gradient(135deg,var(--cyan),var(--green));color:#080c18;border:none;border-radius:12px;font-size:16px;font-weight:700;cursor:pointer;text-decoration:none;font-family:'Space Grotesk',sans-serif;display:inline-block;transition:.2s}
.bp:hover{box-shadow:0 4px 20px rgba(0,212,255,.3);transform:translateY(-1px)}
.bo{padding:14px 32px;background:0;color:var(--soft);border:1px solid var(--line2);border-radius:12px;font-size:16px;cursor:pointer;font-family:'Space Grotesk',sans-serif;display:inline-block;text-decoration:none;transition:.2s}
.bo:hover{border-color:var(--cyan);color:var(--text)}
.hero-screenshots{display:flex;gap:20px;justify-content:center;align-items:center}
.phone-frame{display:inline-block;padding:10px 8px;background:#1a1d24;border-radius:24px;border:2px solid #2a2d35;box-shadow:0 8px 32px rgba(0,0,0,.4);flex-shrink:0;height:420px}.phone-frame img{display:block;border-radius:14px;width:100%;height:100%;object-fit:cover}.hero-gif{width:auto;height:420px;max-width:240px}
@media(max-width:980px){.hero-gif{width:180px}}
@media(max-width:540px){.hero-screenshots{flex-direction:column;align-items:center}.hero-gif{width:220px}}
/* Scenarios */
.scenarios{padding:80px 0;background:var(--bg2)}
.section-title{text-align:center;margin-bottom:48px}
.section-title h2{font-size:clamp(28px,4vw,40px);font-weight:700;margin-bottom:10px}
.section-title p{color:var(--muted);font-size:16px;max-width:560px;margin:0 auto;line-height:1.6}
.scenario-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
@media(max-width:768px){.scenario-grid{grid-template-columns:1fr}}
.scenario{background:var(--panel);border:1px solid var(--line);border-radius:20px;padding:28px 24px;text-align:center;transition:.25s}
.scenario:hover{border-color:var(--line2);transform:translateY(-3px)}
.scenario .emoji{font-size:36px;margin-bottom:14px;display:block}
.scenario h3{font-size:18px;font-weight:700;margin-bottom:8px;color:var(--text)}
.scenario p{font-size:14px;color:var(--muted);line-height:1.65}
/* Stats bar */
.stats{padding:60px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.stats-grid{display:flex;justify-content:center;gap:60px;flex-wrap:wrap}
.stat{text-align:center}
.stat strong{display:block;font-size:36px;font-weight:800;color:var(--text);font-family:'Space Grotesk',sans-serif}
.stat span{font-size:13px;color:var(--muted)}
/* Feature overview */
.features-overview{padding:80px 0;background:var(--bg2)}
.feat-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
@media(max-width:768px){.feat-grid{grid-template-columns:1fr 1fr}}
@media(max-width:480px){.feat-grid{grid-template-columns:1fr}}
.feat{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:22px;transition:.25s}
.feat:hover{border-color:var(--line2);transform:translateY(-2px)}
.feat .emoji{font-size:24px;margin-bottom:10px;display:block}
.feat h4{font-size:15px;font-weight:700;margin-bottom:4px;color:var(--text)}
.feat p{font-size:13px;color:var(--muted);line-height:1.5}
.feat-link{display:inline-block;margin-top:24px;font-size:15px;color:var(--cyan);font-weight:600;text-decoration:none}
.feat-link:hover{text-decoration:underline}
/* Trust */
.trust{padding:80px 0}
.trust-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
@media(max-width:768px){.trust-grid{grid-template-columns:1fr}}
.trust-card{background:var(--panel);border:1px solid var(--line);border-radius:16px;padding:28px 24px;border-left:3px solid var(--cyan)}
.trust-card h3{font-size:17px;font-weight:700;margin-bottom:10px;color:var(--text)}
.trust-card p{font-size:14px;color:var(--muted);line-height:1.7}
/* FAQ */
.faq{max-width:720px;margin:0 auto}
.fq{background:var(--panel);border:1px solid var(--line);border-radius:12px;margin-bottom:8px;overflow:hidden;cursor:pointer}
.fq-q{padding:16px 20px;font-size:15px;font-weight:600;color:var(--text);display:flex;justify-content:space-between;align-items:center}
.fq-q::after{content:"+";color:var(--cyan);font-size:18px;transition:.2s}
.fq.on .fq-q::after{transform:rotate(45deg)}
.fq-a{max-height:0;overflow:hidden;transition:.3s;padding:0 20px;color:var(--muted);font-size:14px;line-height:1.7}
.fq.on .fq-a{max-height:300px;padding:0 20px 16px}
/* Bottom CTA */
.bottom-cta{padding:80px 0;text-align:center;background:var(--bg2);border-top:1px solid var(--line)}
.bottom-cta h2{font-size:clamp(24px,3.5vw,36px);margin-bottom:12px}
.bottom-cta p{color:var(--muted);max-width:480px;margin:0 auto 28px;line-height:1.6}
/* Featured articles */
.articles-section{padding:80px 0;background:var(--bg2)}
.articles-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
@media(max-width:980px){.articles-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:540px){.articles-grid{grid-template-columns:1fr}}
.article-card{background:var(--panel);border:1px solid var(--line);border-radius:14px;overflow:hidden;text-decoration:none;display:block;transition:.25s}
.article-card:hover{border-color:var(--line2);transform:translateY(-3px)}
.article-card-img{width:100%;aspect-ratio:16/9;object-fit:cover;display:block}
.article-card-body{padding:18px}
.article-card-tag{display:inline-block;background:rgba(0,212,255,.1);color:var(--cyan);padding:3px 10px;border-radius:8px;font-size:11px;font-weight:700;margin-bottom:8px}
.article-card h4{font-size:15px;font-weight:700;color:var(--text);margin-bottom:6px;line-height:1.35}
.article-card p{font-size:13px;color:var(--muted);line-height:1.5;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.article-card-meta{display:flex;justify-content:space-between;align-items:center;padding:0 18px 14px}
.article-card-meta span{font-size:12px;color:var(--muted)}
.article-card-meta .read-link{color:var(--cyan);font-weight:600;font-size:13px}
/* Filter tabs */
.filter-tabs{display:flex;gap:10px;justify-content:center;margin-bottom:32px;flex-wrap:wrap}
.filter-tab{padding:8px 18px;background:var(--panel);border:1px solid var(--line);border-radius:20px;color:var(--muted);font-size:13px;font-weight:600;cursor:pointer;transition:.2s;text-decoration:none;font-family:'Space Grotesk',sans-serif}
.filter-tab:hover,.filter-tab.on{border-color:var(--cyan);color:var(--cyan);background:rgba(0,212,255,.06)}
</style>'''

    _features_href = '/pt/features.html' if lang == 'pt' else ('/es/features.html' if lang == 'es' else ('/ko/features.html' if lang == 'ko' else ('/ja/features.html' if lang == 'ja' else ('/tw/features.html' if lang == 'tw' else ('/zh/features.html' if lang == 'zh' else '/features.html')))))
    body = '''
<header class="hero">
  <div class="wrap">
    <h1><span class="grad">''' + t('hero_slogan') + '''</span></h1>
    <p class="lead">''' + t('hero_lead') + '''</p>
    <div data-foneclaw-apk-cta data-title="''' + t('cta_download') + '''" data-copy="''' + t('cta_copy') + '''"></div>
    <div style="text-align:center;margin-top:16px;margin-bottom:40px"><a class="bo" href="''' + _features_href + '''">''' + t('cta_see_features') + '''</a></div>
    <div class="hero-screenshots" aria-label="Product screenshots">
      <div class="phone-frame"><img src="/images/features/gif-phone-health-poster.jpg" data-gif="/images/features/gif-phone-health.gif" alt="FoneClaw phone health" class="hero-gif lazy-gif"></div>
      <div class="phone-frame"><img src="/images/features/gif-daily-brief-poster.jpg" data-gif="/images/features/gif-daily-brief.gif" alt="FoneClaw daily brief" class="hero-gif lazy-gif"></div>
      <div class="phone-frame"><img src="/images/features/gif-passive-triggers-poster.jpg" data-gif="/images/features/gif-passive-triggers.gif" alt="FoneClaw passive triggers" class="hero-gif lazy-gif"></div>
    </div>
  </div>
</header>

<section class="scenarios">
  <div class="wrap">
    <div class="section-title"><h2>''' + t('scenario_title') + '''</h2><p>''' + t('scenario_desc') + '''</p></div>
    <div class="scenario-grid">
      <div class="scenario"><span class="emoji">\U0001f4e2</span><h3>''' + t('scenario_1_title') + '''</h3><p>''' + t('scenario_1_desc') + '''</p></div>
      <div class="scenario"><span class="emoji">\U0001f4f1</span><h3>''' + t('scenario_2_title') + '''</h3><p>''' + t('scenario_2_desc') + '''</p></div>
      <div class="scenario"><span class="emoji">\U0001f4f8</span><h3>''' + t('scenario_3_title') + '''</h3><p>''' + t('scenario_3_desc') + '''</p></div>
    </div>
  </div>
</section>

<section class="stats">
  <div class="wrap">
    <div class="stats-grid">
      <div class="stat"><strong>16</strong><span>''' + t('stat_categories') + '''</span></div>
      <div class="stat"><strong>120+</strong><span>''' + t('stat_actions') + '''</span></div>
      <div class="stat"><strong>''' + _free_label + '''</strong><span>''' + t('stat_free') + '''</span></div>
      <div class="stat"><strong>Android 9+</strong><span>''' + t('stat_android') + '''</span></div>
    </div>
  </div>
</section>



<section class="articles-section">
  <div class="wrap">
    <div class="section-title"><h2>''' + t('articles_title') + '''</h2><p>''' + t('articles_desc') + '''</p></div>
    <div class="articles-grid">
      {article_cards_html}
    </div>
  </div>
</section>

<section class="bottom-cta">
  <div class="wrap">
    <h2>''' + t('bottom_cta_title') + '''</h2>
    <p>''' + t('bottom_cta_desc') + '''</p>
    <div data-foneclaw-apk-cta data-title="''' + t('cta_download') + '''" data-copy="''' + t('cta_copy') + '''"></div>
  </div>
</section>
<script>
document.querySelectorAll('.lazy-gif').forEach(function(img){{
  var poster=img.src;
  var gif=img.getAttribute('data-gif');
  if(!gif)return;
  img.addEventListener('mouseenter',function(){{img.src=gif;}});
  img.addEventListener('mouseleave',function(){{img.src=poster;}});
}});
</script>
'''

    body = body.format(article_cards_html=article_cards_html)

    hreflang = generate_hreflang_tags('/', lang)

    return full_page(
        t('meta_title'),
        t('meta_desc'),
        '/' if lang == 'en' else f'/{lang}/',
        0,
        body,
        extra_css=extra_css,
        og_image='https://www.foneclaw.ai/images/og-index.jpg',
        lang=lang,
        hreflang_tags=hreflang)
