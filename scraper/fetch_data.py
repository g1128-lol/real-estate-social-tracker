import requests
from bs4 import BeautifulSoup
import csv
import os
from datetime import datetime

def get_youtube_subscribers(channel_id):
    url = f"https://www.youtube.com/channel/{channel_id}"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    meta = soup.find("meta", itemprop="subscriberCount")
    if meta:
        return meta["content"]
    return "N/A"

channels = {
    "好房網": "UCxxxxx",
    "5168實價登錄比價王": "UCyyyyy",
    "591看豪宅": "UCzzzzz",
    "樂居": "UCaaaa",
    "35線上賞屋": "UCbbbb",
    "信義房屋": "UCcccc",
    "住展": "UCdddd",
    "阿明當家": "UCeeee",
}

today = datetime.today().strftime("%Y-%m-%d")
rows = []

for name, channel_id in channels.items():
    subs = get_youtube_subscribers(channel_id)
    rows.append([today, "YOUTUBE", name, channel_id, subs])

os.makedirs("data", exist_ok=True)
with open("data/latest.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["date", "platform", "account_name", "account_id", "followers"])
    writer.writerows(rows)

print("完成，已寫入 data/latest.csv")
