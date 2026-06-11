import requests
import csv
import os
import re
from datetime import datetime

def get_youtube_subscribers(handle):
    url = f"https://www.youtube.com/{handle}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    }
    try:
        res = requests.get(url, headers=headers, timeout=15)
        patterns = [
            r'"subscriberCountText":\{"simpleText":"([^"]+)"',
            r'"shortSubscriberCountText":\{"simpleText":"([^"]+)"',
            r'"subscriberCount":"(\d+)"',
        ]
        for pattern in patterns:
            match = re.search(pattern, res.text)
            if match:
                return match.group(1)
        return "N/A"
    except Exception as e:
        return f"ERROR:{e}"

channels
