# 🤖 AI 热点 5 日播报（07.29 - 08.03）

## 🔥 GitHub 热门 AI 项目

1. **[FareedKhan-dev/kimi-k3-in-c](https://github.com/FareedKhan-dev/kimi-k3-in-c)** — 2.78万亿参数的 Kimi K3 在纯 C99 实现下，仅用 8.24GB 内存即可在单 CPU 上跑推理，无 BLAS、无框架、无 GPU。开源社区对"小内存跑大模型"的极致追求，令人震撼。

2. **[melonmath/microkimi](https://github.com/melonmath/microkimi)** — 用纯 Rust（零依赖）从零重写 Kimi K3 和 DeepSeek-V4-Flash-0731 架构，并逐行验证与官方实现 1:1 一致。架构逆向工程的典范，对理解前沿模型内部机制极有价值。

3. **[Anionex/codex-vision-proxy](https://github.com/Anionex/codex-vision-proxy)** — 让纯文本 LLM 在 Codex 中调用内置看图工具（view_image）的方案，附带为纯文本模型设计的视觉工具包。巧妙解决文本模型的视觉短板，实用性极强。

4. **[0xwilliamortiz/ratchet](https://github.com/0xwilliamortiz/ratchet)** — 让 Agent 读取规则并检查自身是否遵守。Agent 行为合规性验证是当前行业痛点，这个轻量级方案（JavaScript，⭐411）直击要害。

5. **[aigclink/geolook](https://github.com/aigclink/geolook)** — 开源端到端 GEO（生成式引擎优化）实现：状态分析、诊断、策略、工单、执行、验证全链路。GEO 正成为 SEO 之后的下一波流量红利，值得提前布局。

6. **[simonlin1212/vibe-astock](https://github.com/simonlin1212/vibe-astock)** — A 股短线复盘看板：涨停池、连板梯队、龙虎榜、板块资金一屏看完。情绪指标纯本地计算，AI 只负责把数据串成盘面研判——"数据本地算，AI 只写稿"的设计思路很务实。

7. **[juxhinr/bindwidth](https://github.com/juxhinr/bindwidth)** — 基于证据的本地 LLM 推理规模与 TCO（总拥有成本）计算器。企业部署本地模型前的算力/成本评估工具，实用价值高。

8. **[harrrshall/barunlm-35m](https://github.com/harrrshall/barunlm-35m)** — 仅 3500 万参数的 Base LM，在 57 亿 token 上训练。小参数模型的效率探索，对端侧和资源受限场景有意义。

9. **[artbyjazi/autoclip](https://github.com/artbyjazi/autoclip)** — 本地优先的开源 AI 视频剪辑器：长视频进，字幕烧录+说话人追踪的 9:16 竖屏剪辑出。完全离线可用（Whisper + Ollama），内容创作者的效率神器。

10. **[AFan4724/clone-chat](https://github.com/AFan4724/clone-chat)** — 用 LLM 复刻聊天对象的本地对话 Agent：导入真实聊天记录，学习 TA 的语气、表情和回复节奏，支持语音、主动联系和长期记忆，数据全在本地。数字分身/情感陪伴赛道的代表性开源项目。

## 🧠 国际 Agent 更新

- **Claude (Anthropic)** — 本周经历了一次"跨所有模型的高错误率"事件（已解决），引发社区对 Claude 服务稳定性的讨论。同时，Claude Code 生态持续活跃，社区出现 **Agent-Manager**（Tmux TUI 统一管理 Claude Code/Codex/OpenCode）和 **qm**（多人 Agent 协作工作台，HN 获 665 赞）等周边工具，显示 Claude Code 已成为 Agent 开发的事实标准之一。

- **OpenAI / ChatGPT** — 发布多项数学和理论计算机科学进展（几何、密码学、复杂性理论），并宣布"构建富足智能"的全栈战略：让先进 AI 更强大、更便宜、更普及。此外，Sora 幕后故事曝光——奥特曼也逃不过刷 TikTok 上瘾，侧面反映团队对短视频数据的重视。

- **GitHub Copilot (Microsoft)** — Google 借助 AI 修复 Chrome 漏洞的效率大幅提升（6 月修复量超过过去两年总和），微软正在将类似 AI 辅助安全能力整合进 Copilot 与 Azure 安全体系中。

- **Google Gemini** — Gemini 驱动的 Chrome 漏洞修复效率引发行业关注（HN 热帖 572 赞），AI 辅助代码审计与漏洞修复正在成为安全领域的新范式。

- **Llama (Meta)** — 虽然本周无重大版本更新，但社区围绕 Llama 的微调与部署工具持续涌现，Llama 仍是开源模型生态的核心底座。

## 🇨🇳 国内 Agent 更新

- **Kimi (月之暗面)** — 本周 GitHub 社区出现两个重量级项目：**kimi-k3-in-c** 用纯 C 在单 CPU 上跑通 2.78 万亿参数推理（8.24GB 内存），**microkimi** 用 Rust 从零重写 Kimi K3 架构并验证 1:1 一致。这两个项目侧面印证 Kimi K3 架构的开源影响力，也说明国内模型在端侧/低成本推理方向的领先探索。

- **DeepSeek (深度求索)** — DeepSeek-V4-Flash-0731 架构被开源社区用 Rust 逆向重写（microkimi 项目），显示 DeepSeek 最新模型的架构设计受到国际开发者高度关注。

- **通义千问 (阿里)** — 本周未观测到重大版本更新，但阿里在 AI 基础设施和企业级 Agent 落地方面持续投入。

## 📰 AI 行业动态

1. **EU AI Act 第 50 条正式生效（8 月 2 日）**：未披露 AI 生成内容（尤其是幻觉内容）将面临违法和高额罚款。这标志着全球 AI 内容合规进入强监管时代，对内容平台和 Agent 开发者的影响深远。

2. **前沿实验室 Agent 入侵事件时间线公开**：Hugging Face 发布"2026 年 7 月前沿实验室 Agent 入侵事件"技术时间线，揭示 Agent 安全攻防的严峻现实。Agent 安全问题已从理论讨论进入真实攻防阶段。

3. **AI 初创公司正在减少论文发表**：Science 杂志报道 AI 头部初创公司几乎不再发表研究成果，引发对 AI 研究透明度和学术生态的担忧。

4. **LLM 路由器被证伪**：Manifest 团队宣布弃用自研 LLM 路由器，称"每个人都在构建 LLM 路由器，但我们废弃了它"。模型路由的 ROI 受到质疑，简单方案可能更优。

5. **AI 美学成为讨论热点**："The AI Aesthetic" 一文在 HN 引发热议（376 赞），AI 生成内容的视觉风格正在形成独特的审美范式，设计界面临新课题。

## 💡 本周洞察

**本周最值得关注的是"让大模型跑在普通硬件上"的集体努力**——Kimi K3 在 8GB 内存的 CPU 上跑推理、35M 参数的 BarunLM、纯 Rust 的架构重写，都在指向同一个方向：模型能力的释放不再依赖云端巨量算力，端侧/本地化部署正在成为现实。与此同时，**Agent 的安全与合规问题（EU AI Act 生效、Agent 入侵事件、ratchet 规则检查工具）正从边缘话题变成行业刚需**——当 Agent 开始真正执行任务，规则遵循、内容披露和边界控制就不再是锦上添花，而是决定 Agent 能否大规模商用的生死线。

---
*🤖 由 AI Radar 自动生成 · 下期播报预计 08.03 后约5天推送*