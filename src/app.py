import os
import feedparser
import uvicorn
from fastapi import FastAPI, Request
from strands import Agent, tool
from dotenv import load_dotenv

load_dotenv()

MODEL_ID = os.getenv("MODEL_ID")

# 1. RSS取得ツール
@tool
def fetch_rss_feed(url: str, limit: int = 5) -> str:
    """指定されたURLのRSS/Atomフィードを取得し、最新のエントリ一覧を返します。"""
    feed = feedparser.parse(url)
    if feed.bozo and not feed.entries:
        return f"エラー: RSSフィードの取得に失敗しました (URL: {url})"

    entries = feed.entries[:limit]
    if not entries:
        return "フィード内に記事が見つかりませんでした。"

    results = [f"【{feed.feed.get('title', 'RSS Feed')}】最新{len(entries)}件:\n"]
    for i, entry in enumerate(entries, 1):
        title = entry.get("title", "タイトルなし")
        link = entry.get("link", "#")
        published = entry.get("published", entry.get("updated", "日時不明"))
        summary = entry.get("summary", "")[:100]
        results.append(
            f"{i}. {title}\n   - リンク: {link}\n   - 公開日: {published}\n   - 概要: {summary}...\n"
        )
    return "\n".join(results)

# 2. Strands Agent の定義 (東京リージョンでオンデマンド可能なモデル)
rss_agent = Agent(
    ##model="anthropic.claude-3-5-sonnet-20241022-v1:0",
    model=MODEL_ID,
    tools=[fetch_rss_feed],
    system_prompt="あなたはRSSフィードを取得してまとめるニュースアシスタントです。"
)

# 3. FastAPIサーバーの定義
app = FastAPI()

@app.post("/invocations")
def handle_agent_invocation(request: Request):
    import asyncio
    payload = asyncio.run(request.json()) if asyncio.iscoroutinefunction(request.json) else request._json
    prompt = payload.get("prompt") or payload.get("message", "")
    response = rss_agent(prompt)
    return {"output": str(response)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)