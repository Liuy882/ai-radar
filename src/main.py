"""AI Radar 5日播报 — 主入口

GitHub Actions 每天触发，脚本内判断是否已满5天。
"""

import json
import os
from datetime import datetime, timedelta, timezone

from collectors import collect_all
from summarizer import summarize
from pusher import push_to_wechat

STATE_FILE = ".state.json"
SUMMARY_FILE = "SUMMARY.md"
INTERVAL_DAYS = 5


def should_run() -> bool:
    """检查距上次运行是否已满5天。"""
    if not os.path.exists(STATE_FILE):
        return True

    with open(STATE_FILE, encoding="utf-8") as f:
        state = json.load(f)

    last_run = datetime.fromisoformat(state["last_run"])
    now = datetime.now(timezone.utc)
    days_passed = (now - last_run).days
    print(f"距上次运行: {days_passed} 天 (需要 {INTERVAL_DAYS} 天)")

    return days_passed >= INTERVAL_DAYS


def update_state():
    """更新 last_run 为当前时间。"""
    state = {"last_run": datetime.now(timezone.utc).isoformat()}
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)


def main():
    print("=" * 50)
    print("AI Radar 5日播报机器人")
    print("=" * 50)

    if not should_run():
        print("未满5天，跳过本次运行。")
        return

    print("\n[1/4] 采集数据...")
    data = collect_all()

    if not data["github_trending"] and not data["hacker_news"]:
        print("警告: 未采集到任何数据，但仍继续生成摘要。")

    print("\n[2/4] DeepSeek 生成摘要...")
    try:
        summary = summarize(data)
    except Exception as e:
        print(f"DeepSeek API 调用失败: {e}")
        raise

    print("\n[3/4] 推送到微信...")
    try:
        push_to_wechat(summary)
    except Exception as e:
        print(f"PushPlus 推送失败: {e}")
        raise

    print("\n[4/4] 写入 SUMMARY.md...")
    with open(SUMMARY_FILE, "w", encoding="utf-8") as f:
        f.write(summary)

    update_state()
    print("\n✅ 完成！下期播报将在5天后推送。\n")


if __name__ == "__main__":
    main()
