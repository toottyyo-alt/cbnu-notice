import requests
from bs4 import BeautifulSoup
import os

URL = "https://www.cbnu.ac.kr/www/selectBbsNttList.do?bbsNo=313&key=1850"

def get_latest_notice():
    res = requests.get(URL)
    soup = BeautifulSoup(res.text, "html.parser")

    title = soup.select_one("table tbody tr td.subject a")
    if title:
        return title.text.strip()
    return None

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
    notice = get_latest_notice()
    if notice:
        send_telegram(f"📢 새 공지 확인:\n{notice}")
