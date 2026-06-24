"""数据采集模块 — GitHub Trending、Hacker News、Agent官方博客RSS。"""

import concurrent.futures
from datetime import datetime, timedelta, timezone
import re

import requests
import feedparser

SINCE_DAYS = 5

# ── Agent 列表 ──────────────────────────────────────────────

AGENTS_INTL = [
    "Claude (Anthropic)",
    "ChatGPT (OpenAI)",
    "Gemini (Google)",
    "GitHub Copilot (Microsoft)",
    "Cursor IDE",
    "Claude Code (Anthropic)",
    "Llama (Meta)",
    "Mistral AI",
    "Perplexity AI",
]

AGENTS_CN = [
    "文心一言 (百度)",
    "通义千问 (阿里)",
    "豆包/扣子 (字节跳动)",
    "Kimi (月之暗面)",
    "智谱清言/ChatGLM (智谱AI)",
    "DeepSeek (深度求索)",
    "腾讯元宝",
    "讯飞星火 (科大讯飞)",
]

# ── Agent 官方博客 RSS ──────────────────────────────────────

AGENT_RSS_FEEDS = [
    ("OpenAI", "https://openai.com/blog/rss.xml"),
    ("Anthropic", "https://www.anthropic.com/blog/rss.xml"),
    ("Google AI", "https://blog.google/technology/ai/rss/"),
    ("Meta AI", "https://ai.meta.com/blog/feed/"),
    ("Mistral AI", "https://mistral.ai/news/rss.xml"),
    ("Perplexity AI", "https://www.perplexity.ai/hub/blog/rss.xml"),
    # 国内 AI 媒体 RSS
    ("机器之心", "https://www.jiqizhixin.com/rss"),
    ("量子位", "https://www.qbitai.com/feed"),
    # Reddit r/artificial (RSS via Reddit)
    ("Reddit r/artificial", "https://www.reddit.com/r/artificial/.rss"),
    ("Reddit r/MachineLearning", "https://www.reddit.com/r/MachineLearning/.rss"),
]

# ── 辅助函数 ────────────────────────────────────────────────


def _since_timestamp() -> int:
    dt = datetime.now(timezone.utc) - timedelta(days=SINCE_DAYS)
    return int(dt.timestamp())


def _strip_html(text: str) -> str:
    """去除HTML标签。"""
    return re.sub(r"<[^>]+>", "", text)[:300]


# ── GitHub Trending ─────────────────────────────────────────


def collect_github_trending() -> list[dict]:
    """从 GitHub Search API 获取近5天热门 AI 仓库。"""
    since_date = (datetime.now(timezone.utc) - timedelta(days=SINCE_DAYS)).strftime(
        "%Y-%m-%d"
    )
    results = []
    queries = ["topic:ai", "topic:machine-learning", "topic:llm"]

    for q in queries:
        try:
            resp = requests.get(
                "https://api.github.com/search/repositories",
                params={
                    "q": f"{q} created:>={since_date}",
                    "sort": "stars",
                    "order": "desc",
                    "per_page": 5,
                },
                headers={"Accept": "application/vnd.github+json"},
                timeout=15,
            )
            if resp.status_code == 403:
                print(f"  GitHub API 限流，跳过搜索 '{q}'")
                continue
            resp.raise_for_status()
            for item in resp.json().get("items", []):
                results.append({
                    "name": item["full_name"],
                    "url": item["html_url"],
                    "description": (item.get("description") or "").strip(),
                    "stars": item["stargazers_count"],
                    "language": item.get("language") or "N/A",
                })
        except Exception as e:
            print(f"  GitHub 搜索错误 ({q}): {e}")

    # 按星数降序去重
    seen = set()
    unique = []
    for r in sorted(results, key=lambda x: x["stars"], reverse=True):
        if r["name"] not in seen:
            seen.add(r["name"])
            unique.append(r)
    return unique[:15]


# ── Hacker News ─────────────────────────────────────────────


def collect_hacker_news() -> list[dict]:
    """从 Hacker News Algolia API 搜索近5天 AI 相关热门故事。"""
    timestamp = _since_timestamp()
    results = []

    queries = ["AI", "LLM", "agent", "Claude", "OpenAI", "ChatGPT"]

    for q in queries:
        try:
            resp = requests.get(
                "https://hn.algolia.com/api/v1/search",
                params={
                    "query": q,
                    "tags": "story",
                    "numericFilters": f"created_at_i>{timestamp}",
                    "hitsPerPage": 5,
                },
                timeout=15,
            )
            resp.raise_for_status()
            for hit in resp.json().get("hits", []):
                results.append({
                    "title": hit.get("title", ""),
                    "url": hit.get("url")
                    or f"https://news.ycombinator.com/item?id={hit['objectID']}",
                    "points": hit.get("points", 0),
                    "comments": hit.get("num_comments", 0),
                })
        except Exception as e:
            print(f"  HN 搜索错误 ({q}): {e}")

    # 去重 + 按热度排序
    seen = set()
    unique = []
    for r in sorted(results, key=lambda x: x["points"], reverse=True):
        if r["title"] not in seen:
            seen.add(r["title"])
            unique.append(r)
    return unique[:15]


# ── Agent 博客 RSS ──────────────────────────────────────────


def collect_agent_news() -> list[dict]:
    """从 Agent 官方博客 RSS 获取近期更新。"""
    results = []
    cutoff = datetime.now(timezone.utc) - timedelta(days=SINCE_DAYS)

    for name, feed_url in AGENT_RSS_FEEDS:
        try:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries[:3]:
                # 尽量解析发布时间
                pub = entry.get("published_parsed") or entry.get("updated_parsed")
                if pub:
                    pub_date = datetime(*pub[:6], tzinfo=timezone.utc)
                    if pub_date < cutoff:
                        continue

                summary = entry.get("summary") or entry.get("description") or ""
                results.append({
                    "agent": name,
                    "title": entry.get("title", ""),
                    "url": entry.get("link", ""),
                    "summary": _strip_html(summary),
                })
        except Exception as e:
            print(f"  RSS 错误 ({name}): {e}")

    return results


# ── 汇总入口 ────────────────────────────────────────────────


def collect_all() -> dict:
    """并行采集所有数据源，返回汇总字典。"""
    print("  启动并行采集 (GitHub / Hacker News / RSS)...")

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
        fut_gh = ex.submit(collect_github_trending)
        fut_hn = ex.submit(collect_hacker_news)
        fut_rss = ex.submit(collect_agent_news)

        github_data = fut_gh.result()
        hn_data = fut_hn.result()
        agent_data = fut_rss.result()

    print(
        f"  采集完成: GitHub {len(github_data)}条, "
        f"HN {len(hn_data)}条, RSS {len(agent_data)}条"
    )

    now = datetime.now(timezone.utc)
    return {
        "github_trending": github_data,
        "hacker_news": hn_data,
        "agent_news": agent_data,
        "agents_intl": AGENTS_INTL,
        "agents_cn": AGENTS_CN,
        "period_start": (now - timedelta(days=SINCE_DAYS)).strftime("%m.%d"),
        "period_end": now.strftime("%m.%d"),
    }
