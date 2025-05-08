# app/openai_utils.py

import os
import httpx
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "openai/gpt-3.5-turbo"  # можно заменить на другой, поддерживаемый OpenRouter

def chat_with_model(messages):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "https://yourdomain.com",  # замените при необходимости
        "X-Title": "BuergergeldChatbot"
    }

    data = {
        "model": MODEL,
        "messages": messages,
    }

    try:
        response = httpx.post(OPENROUTER_API_URL, json=data, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Fehler beim Abrufen der Antwort: {e}"