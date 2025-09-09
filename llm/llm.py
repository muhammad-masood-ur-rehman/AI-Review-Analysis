import os
import json
import requests
from dotenv import load_dotenv
from prompts.review import get_review_prompt

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

def call_openrouter(messages, model="openai/gpt-oss-20b"):

    if not OPENROUTER_API_KEY:
        return "Our Ai Services are currently unavailable"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": model,
        "messages": messages,
        "temperature": 0.3,
    }

    response = requests.post(BASE_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"Our Ai Services are currently unavailable")

    return response.json()["choices"][0]["message"]["content"]
