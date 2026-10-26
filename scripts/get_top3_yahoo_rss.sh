#!/bin/bash
# 1. FastAPI サーバーにリクエストを送り、レスポンスを変数に格納
response=$(curl -s -X POST "http://127.0.0.1:8000/invocations" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "https://news.yahoo.co.jp/rss/topics/top-picks.xml の最新ニュースを3件教えて"}')

# 2. jq コマンドを使って "output" の中身を抽出し、\n を実際の改行として出力
# 実行前に下記コマンドでjqをインストールしてください
# $ sudo apt install jq
echo "$response" | jq -r '.output'
