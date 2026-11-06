# 🤖 AI 热点 5 日播报（11.01 - 11.06）

## 🔥 GitHub 热门 AI 项目

1. **Balanov/uncut** (⭐609, Go) — 无头编码 Agent 框架，单个 7MB 静态二进制、四个工具、纯 stdin/stdout 交互，主打"无损、不静默截断"，为轻量级 Agent 部署提供了极简范式。[链接](https://github.com/Balanov/uncut)

2. **Sandflow-ai/sand3d** (⭐394, HTML) — 用 Python 做 3D 建模，专为 LLM 设计，让大模型能直接生成和操作 3D 场景，是"代码即建模"方向的有趣探索。[链接](https://github.com/Sandflow-ai/sand3d)

3. **SAOS-3624/dsh-see-now** (⭐393, JavaScript) — 让 AI 实时"看见"你的屏幕，按变化量筛选帧、多帧拼图输入，静止画面几乎不消耗 token，直击视觉 Agent 的 token 成本痛点。[链接](https://github.com/SAOS-3624/dsh-see-now)

4. **bytedance/axion1_0** (⭐58, Python) — 字节开源的前沿 Agent 训练配方：仅靠高质量数据 + 简单 SFT+RL 两步，无需 mid-training/DPO，完整 recipe 公开，对自研 Agent 团队参考价值高。[链接](https://github.com/bytedance/axion1_0)

5. **MarkIvor/predictorlab** (⭐67, Python) — 自托管表格 ML 工具，内置 Leakage Guard、共形区间、利润优化阈值与反事实分析，主打"不说谎的 ML"，适合业务侧落地。[链接](https://github.com/MarkIvor/predictorlab)

6. **xingjunm/autoppt** (⭐53, CSS) — AI 备课神器，一键生成整周精美可交互课件，教育场景的 Agent 化落地样本。[链接](https://github.com/xingjunm/autoppt)

7. **prabeakarve/microgpt** (⭐51, Python) — 纯 NumPy 从零实现 GPT，含字节级分词、多头注意力、Adam 训练与 top-k 采样，零依赖，是理解 LLM 内部机制的优质教学代码。[链接](https://github.com/prabeakarve/microgpt)

8. **vixhal-baraiya/qwenFS** (⭐91, Python) — 将文件系统直接编译进 Qwen3.5-2B 权重，探索"模型即系统"的极端集成思路，颇具实验性。[链接](https://github.com/vixhal-baraiya/qwenFS)

> ⚠️ 提示：列表中 `cs2-resp-wallhack-2026` 等为游戏作弊工具，`agentic-hacking-skills` 涉及攻击性技能，均不建议关注或使用。

## 🧠 国际 Agent 更新

- **OpenAI / ChatGPT** — 发布 **GPT‑6 Cyber**，专攻网络安全场景的模型，可发现可利用漏洞并开发修复方案，且被训练为"仅在授权范围内行动"，标志安全 Agent 进入专用模型阶段。同期 Codex 在 Cult.fit 等企业落地，OpenAI 还宣布收购 Pierre Computer Company，并披露 Git 大规模扩展实践。
- **Google / Gemini** — 推出 **Gemini Omni 1.2 Flash**，主打快速、低成本与更长视频片段生成，多模态性价比进一步下探。
- **Claude Code (Anthropic)** — 社区曝出隐私问题：Claude Code 会将用户邮箱地址发送给访问的网站（GitHub issue #107757 高热讨论），提醒开发者关注 Agent 工具的隐私边界。
- **GitHub Copilot (Microsoft)** — 微软提交专利，涉及可在直播中实时修改说话内容的 AI 技术，引发内容真实性与伦理讨论。
- **Cursor IDE** — 本周采集数据中无实质性更新披露。

## 🇨🇳 国内 Agent 更新

- **文心一言（百度）** — 11 月 5 日正式开源 **文心 5.5 Flash Base** 基座模型，多项基准刷新同尺寸 SOTA，延续"开源基座 + 生态"策略，对中小团队自建 Agent 是利好。
- **DeepSeek（深度求索）** — 生态侧活跃：第三方开发者推出 DSH 金融研究插件（Skills、证据库、个股图表与模拟基金），显示 DeepSeek 周边 Agent 工具链正在自发成长（官方未背书）。
- **字节跳动（豆包/扣子）** — 开源 **axion1_0** Agent 训练配方，以极简 SFT+RL 达到前沿 Agent 能力，体现其在 Agent 工程化上的开放姿态。
- 其余厂商（通义千问、Kimi、智谱、腾讯元宝、讯飞星火）本周采集数据中无实质性更新披露。

## 📰 AI 行业动态

1. **Agent 工具隐私与数据安全问题集中爆发** — Postman 被曝静默自动安装 AI 插件并试图共享全部 API 数据（HN 1515 赞、489 评论），叠加 Claude Code 泄露邮箱、OpenAI 疑似悄悄对 Codex 对话重新启用训练，开发者对"Agent 默认行为"的信任危机正在加剧。

2. **AI 倒逼四十年技术债清算** — IEEE Spectrum 一篇关于 AI 与 php2shell 漏洞的文章引发 742 条热议，核心观点是 AI 放大攻击面，迫使企业偿还长期积累的安全与架构欠账。

3. **AI Agent 的"现实检验"** — 50 个 Agent 团队在 Minecraft 中建文明，结果陷入官僚主义泥潭；DoorDash 透露外部 AI Agent 至今仅带来数百单。两则新闻共同说明：多 Agent 协作与消费级 Agent 落地仍远未成熟。

4. **存储与算力基建持续承压** — 富士康旗下富士胶片宣布磁带产量提升 5 倍以应对 AI 归档需求，冷存储正成为 AI 时代被低估的瓶颈环节。

5. **开源权重模型持续追赶** — Ripple-65B Preview 宣称在 Agentic Coding 上达到美国开源权重 SOTA，叠加百度文心 5.5 Flash 开源，开源阵营在 Agent 编码赛道加速逼近闭源前沿。

## 💡 本周洞察

本周最鲜明的信号是 **Agent 从"能力竞赛"转向"信任与工程化竞赛"**：模型侧 GPT‑6 Cyber、Ripple-65B、文心 5.5 Flash 不断刷新能力上限，但真正占据舆论中心的是 Postman 静默装插件、Claude Code 泄露邮箱这类"默认行为"争议——Agent 的权限边界、数据流向和可审计性正成为比 benchmark 更关键的选型标准。与此同时，Minecraft 官僚化实验与 DoorDash 数百单的数据给多 Agent 叙事泼了冷水，提示行业需要从 demo 走向可验证的真实工作流；而字节开源极简 Agent 训练配方、百度开源基座，则意味着"高质量数据 + 简单配方"的开放路线正在压缩自研门槛。对开发者而言，下一阶段的竞争点或许不在模型多强，而在 **谁能把 Agent 的权限、成本与可靠性做成可交付的产品**。

---
*🤖 由 AI Radar 自动生成 · 下期播报预计 11.06 后约5天推送*