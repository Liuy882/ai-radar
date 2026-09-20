# 🤖 AI 热点 5 日播报（09.15 - 09.20）

## 🔥 GitHub 热门 AI 项目

1. **[liyupi/ai-model-world](https://github.com/liyupi/ai-model-world)** (⭐123, TypeScript): 把 556 个大模型拟人化成像素小人的可视化站点，聚合 Epoch AI、LiveBench、Hugging Face 等数据源每小时同步，零后端纯静态导出，是观察模型竞争格局的有趣窗口。

2. **[ruc-datalab/EvoOntology](https://github.com/ruc-datalab/EvoOntology)** (⭐191, Python): 为 Claude Code / Codex 建立并进化本体层的自演化插件，代表"数据 Agent + 知识结构化"这一新方向，值得关注其对 Agent 长期记忆的解决思路。

3. **[wfzyx/von](https://github.com/wfzyx/von)** (⭐47, Python): 开源 System One 决策模型，亚 15ms 非自回归推理，可作为 TypeSafe Jev 的本地替代方案，标志着"轻量决策模型"开始从闭源走向开源。

4. **[Heman10x-NGU/openJev-verdict-2.0](https://github.com/Heman10x-NGU/openJev-verdict-2.0)** (⭐48, Python): 151M 参数的非自回归决策引擎，在 typed-decisions 基准上以 77.10% 准确率、0.0636 Brier 分数击败 TypeSafe Jev 与 Laya，小模型在特定任务上反超大模型的典型案例。

5. **[mizorewww/laya-mlx](https://github.com/mizorewww/laya-mlx)** (⭐34, Python): Laya 类型化决策模型的 MLX 原生运行时，M3 Max 上 7-14ms 完成短决策，无需 PyTorch 或云 API，端侧决策模型工程化的重要一步。

6. **[0xNatoshi/jev-codex-router](https://github.com/0xNatoshi/jev-codex-router)** (⭐73, Python): 为 Codex 提供逐轮模型与推理深度路由，由 Jev 驱动自动选择模型、思考深度和速度模式，是"推理成本优化"这一痛点的直接回应。

7. **[ekzhang/openjev-sglang](https://github.com/ekzhang/openjev-sglang)** (⭐196, Python): 基于开源模型的 Jev 兼容 API 端点（prefill-only），为 Jev 生态补齐了推理侧基础设施。

8. **[pallavi-shekhar/ai-engineering-interview-questions-company-wise](https://github.com/pallavi-shekhar/ai-engineering-interview-questions-company-wise)** (⭐66, Markdown): 按公司分类的 AI 工程面试题库，反映 AI 工程岗位招聘需求持续升温，对求职者有直接参考价值。

> 📌 本周 GitHub 最显著的趋势是 **Jev / TypeSafe System One 生态的爆发**——awesome 列表、路由、运行时、开源替代模型在同一周密集涌现，围绕"类型化决策"这一细分方向已形成小型生态圈。

## 🧠 国际 Agent 更新

- **Claude Code (Anthropic)**: 开始支持在没有 Claude.md 的情况下读取 AGENTS.md，进一步兼容社区 Agent 配置标准，降低多工具协作的迁移成本。（HN 714 赞）
- **Claude (Anthropic)**: Claude Cowork 与聊天合并为统一的 Claude 体验，协作与对话场景的边界被打破，指向"一个 Claude 处理所有工作流"的产品方向。
- **ChatGPT (OpenAI)**: 推出 **Astra for Law**，面向法律行业的前沿智能 + 定制工作流 + 法律级数据管控；同时 Cooley 律所基于 ChatGPT Work 构建 GO Public 加速 IPO 流程，垂直行业落地明显提速。
- **Mistral AI**: 与 Mozilla 合作推出隐私优先、多语言 AI 浏览体验，将模型能力嵌入浏览器层，是欧洲 AI 主权叙事的又一落子。
- **GitHub Copilot (Microsoft)**: 本周无直接产品更新，但微软高管在未删减法庭文件中称 AI 抓取是"人类历史上最大的劳动力盗窃"，这一表态对 Copilot 的数据合规叙事构成潜在压力。

## 🇨🇳 国内 Agent 更新

- **通义千问 (阿里)**: Qwen 3.8 以 27B 规模实现"分分钟交付网页"，设计 + 前端一口气完成（后端仍需补齐），在代码生成与前端交付场景展现出极强的实用性，是国内开源模型工程能力的又一证明。
- **DeepSeek (深度求索)**: 本周采集数据中无直接更新，但其在开源推理模型上的持续迭代仍是国内 Agent 生态的重要底座，建议持续关注其下一代发布节奏。
- **智谱清言 / ChatGLM (智谱AI)**: 本周无直接更新，但 GLM 系列在 Coding Agent 方向（如 ZCode）有动作——需注意 ZCode 被曝静默上传 Git 历史，引发隐私争议，对国内 Coding Agent 的数据安全信任度是一次警示。

> 其余国内 Agent（文心一言、豆包/扣子、Kimi、腾讯元宝、讯飞星火）本周采集数据中未见实质性更新。

## 📰 AI 行业动态

1. **AI 抓取争议升级为法律战**：微软高管在未删减法庭文件中称 AI 抓取是"人类历史上最大的劳动力盗窃"，配合 Reddit 热帖发酵，数据版权与训练合规正从道德讨论转向司法博弈。

2. **AI 军事应用出现"幻觉情报"险情**：CNN 报道美军因使用 AI 生成的虚假情报（涉及中国船只）而出现近距离误判，AI 在高风险决策场景的可靠性问题被推上风口浪尖。

3. **安全事件频发**：OpenAI 内部仓库被曝因堆溢出 + SSO 配置错误遭入侵；ZCode 被指静默上传用户 Git 历史——AI 工具链自身的安全与隐私风险正成为行业级议题。

4. **AI 与就业/开源社区摩擦加剧**：PS5 Linux 负责人因"一群不懂代码的 noob 用 LLM"而辞职，折射出开源社区对 AI 生成代码的质量与文化的深层焦虑。

5. **技术前沿持续突破**：arXiv 论文《Breaking the 1.58-bit Barrier for Ternary LLMs》探索三值 LLM 的极限压缩，为端侧与低成本推理打开新空间。

## 💡 本周洞察

本周最鲜明的信号是 **AI 正从"能力竞赛"转入"信任与治理竞赛"**——微软的"劳动力盗窃"论、美军 AI 幻觉情报、OpenAI 仓库被黑、ZCode 静默上传，四件事共同指向同一个问题：当 AI 深度嵌入关键流程，可靠性、合规性与透明度已成为比模型分数更紧迫的瓶颈。与此同时，GitHub 上 Jev/System One 生态的爆发说明行业正在用"小而专的决策模型 + 路由"来对冲大模型的高成本与不确定性，这可能是下一阶段 Agent 架构的重要演化方向。对从业者而言，**"能跑通"已不够，"可审计、可信任、可负担"才是新的竞争门槛**。

---
*🤖 由 AI Radar 自动生成 · 下期播报预计 09.20 后约5天推送*