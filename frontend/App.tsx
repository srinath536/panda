import { useState } from "react";
import React from 'react';


function App() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  const search = async () => {
    const res = await fetch(`http://localhost:8000/search?q=${query}`);
    const data = await res.json();
    console.log(data); // 👈 Add this line
    setResults(data);
  };
  

  const vote = async (url: string, delta: number) => {
    await fetch("http://localhost:8000/vote", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ keyword: query, url, delta }),
    });
    search();
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Panda Search 🐼</h1>
      <input
        value={query}
        onChange={e => setQuery(e.target.value)}
        placeholder="Search something..."
        style={{ padding: "0.5rem", width: "300px", marginRight: "1rem" }}
      />
      <button onClick={search}>Search</button>

      <div style={{ marginTop: "2rem" }}>
        {results.map(r => (
          <div key={r.url} style={{ border: "1px solid #ccc", padding: "1rem", marginBottom: "1rem" }}>
            <h3>{r.title}</h3>
            <p><a href={r.url} target="_blank" rel="noopener noreferrer">{r.url}</a></p>
            <button onClick={() => vote(r.url, 1)}>👍</button>
            <button onClick={() => vote(r.url, -1)}>👎</button>
            <p>Score: {r.score}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;