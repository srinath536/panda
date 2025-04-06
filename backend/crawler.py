import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin, urlparse
import os

visited = set()
pages = []

def crawl(url, depth=2):
    if depth == 0 or url in visited:
        return
    try:
        print(f"📍 Visiting: {url}")
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")

        title = soup.title.string.strip() if soup.title else url
        text = soup.get_text(separator=" ", strip=True)

        if len(text.strip()) > 0:
            pages.append({
                "url": url,
                "title": title,
                "content": text
            })
            print(f"✅ Added: {title} ({url})")
        else:
            print("⚠️ Skipped empty content.")

        visited.add(url)

        for link in soup.find_all("a", href=True):
            href = link['href']
            full_url = urljoin(url, href)

            if urlparse(full_url).netloc == urlparse(url).netloc:
                crawl(full_url, depth - 1)

    except Exception as e:
        print(f"❌ Failed to crawl {url}: {e}")

# Start point
start_urls = ["http://books.toscrape.com"]
for url in start_urls:
    crawl(url, depth=2)

os.makedirs("data", exist_ok=True)
with open("data/pages.json", "w", encoding='utf-8') as f:
    json.dump(pages, f, indent=2, ensure_ascii=False)

print(f"\n🔁 Done. Collected {len(pages)} pages.")
