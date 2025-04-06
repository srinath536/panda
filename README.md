# 🐼 Panda Search Engine

A lightweight, decentralized search engine prototype — inspired by Google, built with Python + FastAPI + React.  
Panda allows users to search web pages and vote on relevance, forming a small-scale search experience.

---

## 🚀 Features

- 🌐 Web crawler to scrape and collect content from websites
- 🧠 Indexer that maps keywords to web pages
- 🔍 Search API powered by FastAPI
- 🧾 Frontend built with React + TypeScript + Vite
- 📊 User voting system to rank search results

---

## 🛠 Installation & Running

1. Clone the repo

git clone https://github.com/srinath536/panda.git
cd panda

2. Setup Backend

cd backend
pip install -r requirements.txt

# Run crawler and indexer
python crawler.py
python indexer.py

# Start backend server
uvicorn search:app --reload

3. Setup Frontend
cd frontend
npm install
npm run dev




