# AI Radar 🤖

AI 热点 5 日播报机器人 — 自动采集 GitHub / Hacker News / Agent 更新，通过 DeepSeek 生成中文摘要，推送到微信。

## 工作流程

- 每天自动检查，满 5 天触发
- 并行采集：GitHub Trending AI 项目 + Hacker News 热帖 + Agent 官方博客
- DeepSeek API 生成结构化摘要（国内外 Agent 全覆盖）
- PushPlus 推送到微信
- 自动覆盖最新摘要

## 项目结构

```
.
├── .github/workflows/radar.yml   # GitHub Actions 定时任务
├── src/
│   ├── main.py                   # 入口
│   ├── collectors.py             # 数据采集
│   ├── summarizer.py             # DeepSeek 摘要
│   └── pusher.py                 # PushPlus 推送
├── SUMMARY.md                    # 最新摘要
├── .state.json                    # 运行状态
└── requirements.txt
```
