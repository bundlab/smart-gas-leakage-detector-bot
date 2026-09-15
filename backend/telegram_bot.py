import requests
from backend.config import TELEGRAM_TOKEN, CHAT_ID

def send_alert(level):
    message = f"🚨 GAS LEAK DETECTED! Level: {level}"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})