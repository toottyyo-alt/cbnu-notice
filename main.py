import requests
import os

token = os.environ["TELEGRAM_TOKEN"]
chat_id = os.environ["TELEGRAM_CHAT_ID"]

url = f"https://api.telegram.org/bot{token}/sendMessage"
data = {
    "chat_id": chat_id,
    "text": "✅ 텔레그램 테스트 성공"
}

r = requests.post(url, data=data)
print(r.status_code)
print(r.text)
