import requests
import csv
import os
from datetime import datetime

API_KEY = os.environ.get("YOUTUBE_API_KEY")

channels = {
    "好房網": "UCub_c6M78NnPwe_WyOpSe1A",
    "5168實價登錄比價王": "UC6A-kU7A5HkN8LtiBPiq5aQ",
    "35線上賞屋": "UCnWB4yjKnm6AeW-pj4E3dQw",
    "樂居": "UC4QPIwv37y0_u6yGKXHMvAA",
    "591旗艦房產": "UC_5AjKFz3tww1WSPzM6wF1A",
}

def get_subscribers(channel_id):
    url = "https://www.googleapis.com/youtube/v3/channels"
    params = {
        "part": "statistics",
        "id": channel_id,
        "key": API_KEY,
    }
    try:
        res = requests.get(url, params=params, timeout=15)
        data = res.json()
        return data["items"][0]["statistics"]["subscriberCount"]
    except Exception as e:
        return f"ERROR:{e}"

today = datetime.today().strftime("%Y-%m-%d")
rows = []

for name, channel_id in channels.items():
    subs = get_subscribers(channel_id)
    print(f"{name}: {subs}")
    rows.append([today, "YOUTUBE", name, channel_id, subs])

os.makedirs("data", exist_ok=True)
with open("data/latest.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["date", "platform", "account_name", "account_id", "followers"])
    writer.writerows(rows)

print("完成，已寫入 data/latest.csv")
