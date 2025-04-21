# 🧠 AI Message Generator API

This project is a FastAPI-based microservice that generates personalized messages using different AI models — OpenAI, Claude, Gemini, and DeepSeek. It supports model-specific backends, clean modular design, and logs generation activities to file.

# 🚀 Features


## 1) Generate personalized messages:

Generate 5 personalized messages based on:
- Relationship (spouse, friend, etc.)
- Tone (funny, formal, etc.)
- Occasion (birthday, anniversary, etc.)
- Optional Note

🔌 Pluggable model support: OpenAI, Claude, Gemini, DeepSeek
🔒 Rate limiting per IP (via slowapi)

🛠️ Setup

1. Install Dependencies

pip install -r requirements.txt

2. Set Environment Variables

# .env or export manually
OPENAI_API_KEY=your-openai-key
GEMINI_API_KEY=your-gemini-key
CLAUDE_API_KEY=your-claude-key
DEEPSEEK_API_KEY=your-deepseek-key

3. Run the App

uvicorn main:app --reload

🧺 API Usage

POST /api/v1/generate-message

Body:

{
  "relationship": "spouse",
  "tone": "funny",
  "occasion": "birthday",
  "note": "Hope your day is as awesome as you!"
}

Response:

{
  "model": "openai",
  "suggestions": [
    "Hey love, happy birthday! You're the reason my socks always go missing.",
    "Just wanted to say... you’re older and still cooler than me. 🎉",
    "... (3 more)"
  ]
}

🔒 Throttling

Rate-limited to 10 requests/minute per IP using slowapi.

📜 Logging

Logs for each model are written to logs/generators.log in structured format.

📦 Models Supported

- OpenAI (gpt-4, gpt-3.5-turbo)

- Claude (claude-2, claude-3)

- Gemini

- DeepSeek

Set the preferred model in settings.py.

📄 License

MIT © 2025

👨‍💼 Author

Built with ❤️ by Hayas Ismail
