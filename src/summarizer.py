"""DeepSeek API 摘要生成模块。"""

import json
import os

import requests

DEEPSEEK_API_KEY = os.environ["DEEPSEEK_API_KEY"]
DEEPSEEK_URL = "https://api.deepseek.com/v1/chat/completions"


def build_prompt(data: dict) -> str:
    """从采集数据构建摘要提示词。"""

    # GitHub 项目列表
    gh_lines = []
    for r in data["github_trending"]:
        gh_lines.append(
            f"- **{r['name']}** (⭐{r['stars']}, {r['language']}): "
            f"{r.get('description', '无描述')}"
        )
    github_section = "\n".join(gh_lines) if gh_lines else "暂无数据"

    # Hacker News 热帖
    hn_lines = []
    for r in data["hacker_news"]:
        hn_lines.append(
            f"- [{r['title']}]({r['url']}) — 👍{r['points']} 💬{r['comments']}"
        )
    hn_section = "\n".join(hn_lines) if hn_lines else "暂无数据"

    # Agent RSS 更新
    agent_lines = []
    for r in data["agent_news"]:
        agent_lines.append(
            f"- **[{r['agent']}]** {r['title']}\n  摘要: {r['summary'][:200]}\n  链接: {r['url']}"
        )
    agent_section = (
        "\n".join(agent_lines) if agent_lines else "暂无数据"
    )

    intl_agents = "\n".join(f"  - {a}" for a in data["agents_intl"])
    cn_agents = "\n".join(f"  - {a}" for a in data["agents_cn"])

    return f"""你是一个专业的AI行业热点播报员。请根据以下采集到的近5天数据，生成一份结构化的中文AI热点5日播报。

# 采集到的原始数据

## GitHub 近5天热门AI项目
{github_section}

## Hacker News AI相关热帖
{hn_section}

## Agent/媒体官方博客更新
{agent_section}

# 输出要求

请严格按以下 Markdown 格式输出（不要输出任何其他内容，直接输出Markdown正文）：

# 🤖 AI 热点 5 日播报（{data['period_start']} - {data['period_end']}）

## 🔥 GitHub 热门 AI 项目
（从采集数据中挑选5-10个最值得关注的项目，每个项目用1-2句话说明为什么值得关注。带上项目链接。每个项目前面加上序号。）

## 🧠 国际 Agent 更新

请根据采集数据和你的知识，关注以下产品近期的实质性更新：
{intl_agents}

（只列出有实质性更新的Agent，简要说明更新内容和影响。没有更新的可以不列。如果采集数据中没有某个Agent的信息，但你知道它有近期更新，也可以简要提及。）

## 🇨🇳 国内 Agent 更新

请根据采集数据和你的知识，关注以下产品近期的实质性更新：
{cn_agents}

（只列出有实质性更新的Agent，简要说明更新内容和影响。没有更新的可以不列。如果采集数据中没有某个Agent的信息，但你知道它有近期更新，也可以简要提及。）

## 📰 AI 行业动态
（整理3-5条本周最重要的AI行业新闻或趋势，每条用1-2句话说明）

## 💡 本周洞察
（用2-3句话总结本周期AI领域的核心趋势或值得关注的方向，要有自己的观点和分析）

---
*🤖 由 AI Radar 自动生成 · 下期播报预计 {data['period_end']} 后约5天推送*"""


def summarize(data: dict) -> str:
    """调用 DeepSeek API 生成结构化摘要。"""
    prompt = build_prompt(data)
    print(f"  Prompt 长度: {len(prompt)} 字符")

    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "system",
                "content": "你是一个专业的AI行业热点播报员。你擅长整理和解读AI领域的最新动态，输出结构清晰、有洞察力的中文内容。",
            },
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.7,
        "max_tokens": 4096,
    }

    resp = requests.post(DEEPSEEK_URL, headers=headers, json=payload, timeout=120)

    if resp.status_code != 200:
        raise Exception(f"DeepSeek API 返回 {resp.status_code}: {resp.text}")

    result = resp.json()
    content = result["choices"][0]["message"]["content"]
    print(f"  摘要长度: {len(content)} 字符")
    return content
