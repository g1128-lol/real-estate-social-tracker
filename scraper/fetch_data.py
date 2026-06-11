import requests
from bs4 import BeautifulSoup
import csv
import os
import re
from datetime import datetime

def get_youtube_subscribers(channel_id):
    url = f"https://www.youtube.com/channel/{channel_id}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    try:
        res = requests.get(url, headers=headers, timeout=15)
        match = re.search(r'"subscriberCountText":\{"simpleText":"([^"]+)"', res.text)
        if match:
            return match.group(1)
        match2 = re.search(r'"subscriberCount":"(\d+)"', res.text)
        if match2:
            return match2.group(1)
        return "N/A"
    except:
        return "ERROR"

channels = {
    "好房網": "UCub_c6M78NnPwe_WyOpSe1A",
    "5168實價登錄比價王": "UC6A-kU7A5HkN8LtiBPiq5aQ",
    "35線上賞屋": "UCnWB4yjKnm6AeW-pj4E3dQw",
    "樂居": "UC4QPIwv37y0_u6yGKXHMvAA",
    "591旗艦房產": "UC_5AjKFz3tww1WSPzM6wF1A",
}

today = datetime.today().strftime("%Y-%m-%d")
rows = []

for name, channel_id in channels.items():
    subs = get_youtube_subscribers(channel_id)
    print(f"{name}: {subs}")
    rows.append([today, "YOUTUBE", name, channel_id, subs])

os.makedirs("data", exist_ok=True)
with open("data/latest.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["date", "platform", "account_name", "account_id", "followers"])
    writer.writerows(rows)

print("完成，已寫入 data/latest.csv")
