import requests
from bs4 import BeautifulSoup
import json

# 你的 Google Scholar ID
SCHOLAR_ID = "GX05vA4AAAAJ"
URL = f"https://scholar.google.com/citations?user={SCHOLAR_ID}&hl=en"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# print("soup:",soup)
# 获取总引用数
citations_tag = soup.find_all("td", class_="gsc_rsb_std")
citations = citations_tag[0].text if citations_tag else "N/A"

# print("citations_tag:",citations_tag)
# print("citations:",citations)

if citations != "N/A":
    # 构造符合 Shields.io 要求的 JSON
    badge_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": citations,
        "color": "9cf"
    }
    
    # 输出到 JSON 文件
    with open("citations.json", "w") as f:
        json.dump(badge_data, f, indent=2)
    
    print(f"Updated citations.json with total citations: {citations}")

else:
    print(f"Citations == N/A. Updated citations.json failed")
