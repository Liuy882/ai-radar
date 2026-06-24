"""PushPlus 微信推送模块。"""

import os

import requests

PUSHPLUS_TOKEN = os.environ["PUSHPLUS_TOKEN"]
PUSHPLUS_URL = "https://www.pushplus.plus/send"


def push_to_wechat(content: str):
    """通过 PushPlus 将 Markdown 内容推送到微信。"""
    # 提取标题（第一个一级标题）
    title = "AI 热点播报"
    for line in content.strip().split("\n"):
        line = line.strip()
        if line.startswith("# ") and "播报" in line:
            title = line.lstrip("# ").strip()
            break

    payload = {
        "token": PUSHPLUS_TOKEN,
        "title": title,
        "content": content,
        "template": "markdown",
    }

    resp = requests.post(PUSHPLUS_URL, json=payload, timeout=30)
    data = resp.json()

    if data.get("code") != 200:
        raise Exception(f"PushPlus 推送失败: {data}")

    print(f"  推送成功: {data.get('msg', 'ok')}")
