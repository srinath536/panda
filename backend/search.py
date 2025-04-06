from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Allow frontend to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

with open("data/index.json") as f:
    index = json.load(f)

@app.get("/search")
def search(q: str):
    keyword = q.lower()
    results = index.get(keyword, [])
    return sorted(results, key=lambda x: x["score"], reverse=True)
