import requests

url = "http://127.0.0.1:8000/invocations"
payload = {
    "prompt": "https://aws.amazon.com/jp/blogs/news/feed/ のAWS最新情報を3件取得して要約してください。"
}

try:
    response = requests.post(url, json=payload, timeout=15)
    if response.status_code == 200:
        print("【エージェントからの応答（API経由）】\n")
        print(response.json().get("output"))
    else:
        print(f"エラーが発生しました (Status Code: {response.status_code})")
        print("レスポンステキスト:", response.text)
except requests.exceptions.ConnectionError as e:
    print("サーバーに接続できませんでした。ポート 8000 でサーバーが正しく起動しているか確認してください。")
