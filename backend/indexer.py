import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin, urlparse
import os

visited = set()
pages = []

def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def crawl(url, depth=2):
    if depth == 0 or url in visited:
        return
    try:
        print(f"Crawling: {url}")
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")
        text = soup.get_text(separator=" ", strip=True)
        title = soup.title.string.strip() if soup.title else url

        pages.append({
            "url": url,
            "title": title,
            "content": text
        })
        visited.add(url)

        for link in soup.find_all("a", href=True):
            href = link['href']
            full_url = urljoin(url, href)

            # Stay within the same domain
            if urlparse(full_url).netloc == urlparse(url).netloc and is_valid_url(full_url):
                crawl(full_url, depth - 1)

    except Exception as e:
        print(f"Failed to crawl {url}: {e}")

# Start crawling from base URLs
start_urls = ["http://books.toscrape.com"]

print("🔍 Starting crawl...\n")
for url in start_urls:
    crawl(url, depth=3)

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

# Save results
with open("data/pages.json", "w", encoding='utf-8') as f:
    json.dump(pages, f, indent=2, ensure_ascii=False)

print(f"\n✅ Crawling finished. {len(pages)} pages saved to data/pages.json")
