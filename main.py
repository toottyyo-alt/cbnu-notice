import requests
import os

def send_telegram(msg):
    token = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": msg
    }

    requests.post(url, data=data)

if __name__ == "__main__":
    send_telegram("✅ 텔레그램 테스트 성공")
