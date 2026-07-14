import requests
import json
from engine.models.history import ConversationHistory

def call_llm(messages, temperature:float = 0.8) -> str:
    resp = requests.post(
    "http://localhost:11434/api/chat",
    json={
        "model": "llama3.2",
        "messages": messages,
        "stream": False,
        "options": {
            "temperature": temperature
        }
    },
    timeout=30,
)
    resp.raise_for_status()
    return resp.json()["message"]["content"].strip()

def generate_response(phrase:str, messages) -> str:

    prompt = f"""You are going to receive INSTRUCTIONS about what a response must say.
This is NOT a user message asking you something: it is an order stating
what text you must produce. Do not comment on the instructions, do not
greet them, do not reply to them as if it were a conversation. Your only
task is to GENERATE the final text that someone else will read.

INSTRUCTIONS:
Original sentence: "{phrase}"
- Rewrite it as a single short, clear, grammatically correct sentence in
  neutral English.
- Fix spelling errors and remove filler words.
- Do not add new information
  or change the meaning.
- Do not include intros like "Sure, here you go" or quotation marks.
- Variate the words and structure to make it sound more natural and fluent, but keep the meaning intact.

FINAL TEXT TO SAY (start directly, no preamble):"""
    

    resp = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.8
        }
    },
    timeout=30,
    )

    resp.raise_for_status()
    return resp.json()["response"].strip()

