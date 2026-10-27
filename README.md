# fastapi-rss-agent

An asynchronous FastAPI server integrated with Strands Agent and Amazon Bedrock to fetch, parse, and summarize RSS/Atom feeds using advanced Language Models.

[![Python Version](https://img.shields.io/badge/Python->=3.10-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI->=0.161.1-blue)](https://tiangolo.com)
[![Built with uv](https://img.shields.io/badge/uv-0.13.5-blue)](https://github.com)

## 🚀 Overview

`fastapi-rss-agent` provides a structured API endpoint (`/invocations`) that utilizes an AI Agent equipped with tool-calling capabilities. When given a prompt containing an RSS feed URL, the agent automatically triggers the `fetch_rss_feed` tool to retrieve the latest articles, parses the XML content, and generates a concise, readable summary.

### Key Features
- **Modern Dependency Management:** Powered by `uv` and structured via `pyproject.toml`.
- **FastAPI Endpoint:** Robust and synchronous execution handling via thread pools to avoid event-loop blocking.
- **Agentic Workflows:** Integrated with `strands-agents` to seamlessly manage LLM tool-calling.
- **Flexible Summary Tools:** Robust RSS/Atom parsing using `feedparser`.

---

## 🛠️ Tech Stack & Architecture

- **Backend Framework:** FastAPI / Uvicorn
- **Agent Framework:** `strands-agents` (utilizing AWS Amazon Bedrock / Claude models)
- **Package Manager:** `uv` (Astral)
- **Feed Parser:** `feedparser`

---

## 📦 Installation & Setup

This project uses `uv` for lightning-fast and reliable dependency management.

### Prerequisites
- Python >= 3.10
- `uv` installed (`curl -LsSf https://astral.sh | sh`)

### 1. Clone the Repository
```bash
git clone https://github.com/atsupi/fastapi-rss-agent.git
cd fastapi-rss-agent
```

### 2. Environment Variables
Create a `.env` file in the root directory and configure your credentials:

```ini
MODEL_ID="jp.anthropic.claude-sonnet-4-6"
AWS_ACCESS_KEY_ID="your-aws-access-key"
AWS_SECRET_ACCESS_KEY="your-aws-secret-key"
AWS_DEFAULT_REGION="ap-northeast-1"
```

### 3. Sync Dependencies
Install and synchronize all necessary packages into the virtual environment:
```bash
uv sync
```

---

## 🏃 Running the Server

Start the FastAPI development server with `uv run`:

```bash
uv run uvicorn src.app:app --host 127.0.0.1 --port 8000 --reload
```

---

## 🧪 API Usage & Testing

### Request Schema
- **Endpoint:** `POST /invocations`
- **Content-Type:** `application/json`

| Field | Type | Description |
| :--- | :--- | :--- |
| `prompt` | `string` (Optional) | Instruction for the agent including the RSS URL. |
| `message` | `string` (Optional) | Alternative field to pass the instruction. |

### Example via cURL
You can use the built-in testing script or run the cURL command directly:

```bash
curl -X POST "http://127.0.0.1:8000/invocations" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "https://news.yahoo.co.jp/rss/topics/top-picks.xml の最新ニュースを3件教えて"}'
```

To parse the output with actual line breaks, pipe the response into `jq`:
```bash
./scripts/get_top3_yahoo_rss.sh
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to open a Pull Request or create an Issue for any bug fixes or feature requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
