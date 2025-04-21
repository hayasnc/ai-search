import os

from dotenv import load_dotenv

load_dotenv()

# Choose one: "openai", "deepseek", "gemini", "claude"
AI_MODEL_PROVIDER = os.getenv("AI_MODEL_PROVIDER", "openai")

# Optional: Add API keys or secrets
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPEN_AI_MODEL_PROVIDER = os.getenv("OPEN_AI_MODEL_PROVIDER", "gpt-3.5-turbo")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
