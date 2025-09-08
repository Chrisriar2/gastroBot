from fastapi import FastAPI, Request
import requests
from handlers import handle_message

import os
app = FastAPI()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN") or "YOUR_TOKEN"
BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

@app.get("/")
def home():
    return {"status": "Chatbot educativo sobre síntomas gastrointestinales activo"}

@app.post("/webhook")
async def telegram_webhook(req: Request):
    data = await req.json()
    print("Update recibido:", data)

    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")

        reply = handle_message(chat_id, text)
        send_message(chat_id, reply)

    return {"ok": True}

def send_message(chat_id: int, text: str):
    url = f"{BASE_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)


