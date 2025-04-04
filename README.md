#  NeoGraphConnect: Neo4j Graph Database with Cypher Queries using Python

A full-stack implementation of a graph database system using **Neo4j**, **Python**, and **Streamlit**. This project supports dynamic relationship creation, CSV data ingestion, and web-based interaction with the graph through a clean UI. Ideal for visualizing startup ecosystems, funding relationships, and sectoral insights.

---

##  Features

- Create and manage graph-based data using Neo4j
- Interactive and intuitive web UI built with Streamlit
- Import bulk data via CSV using Cypher queries
- Establish semantic relationships like:
  - `FOUNDED_BY`
  - `FUNDED_BY`
  - `OPERATES_IN`
- Visualize and explore graph structure directly in Neo4j Browser
- Modular, scalable codebase ready for extensions

---

## Tech Stack

- **Backend**: Python
- **Database**: Neo4j (Sandbox/Cloud or Local)
- **Frontend**: Streamlit
- **Query Language**: Cypher

---

## Project Structure

```
neo4j_project/
├── app/
│   ├── __init__.py
│   ├── config.py            # Neo4j credentials and settings
│   ├── graph_logic.py       # Core functions for graph creation
│   └── ui.py                # Streamlit-based frontend
├── data/
│   └── sample_data.csv      # Sample dataset for testing
├── load_csv.py              # Script for CSV data ingestion
├── main.py                  # Script for local testing/debugging
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

---

## Setup Instructions (Local)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/neographconnect.git
cd neographconnect
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Neo4j Access

Update `app/config.py` with your Neo4j credentials:

```python
NEO4J_URI = "bolt://<your-neo4j-uri>:7687"
NEO4J_USERNAME = "neo4j"
NEO4J_PASSWORD = "<your-password>"
```

---

## Running the Project

### 1. Bulk Load Data from CSV

```bash
python load_csv.py
```

### 2. Launch Streamlit Web Interface

```bash
streamlit run app/ui.py
```

Then open `http://localhost:8501` in your browser.

---

## Deployment on Streamlit Cloud

1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub repository
4. Set environment secrets:
   - `NEO4J_URI`
   - `NEO4J_USERNAME`
   - `NEO4J_PASSWORD`
5. Deploy 

---

## Example Cypher Queries

```cypher
// View all startups and their relationships
MATCH (s:Startup)-[r]-(n) RETURN s, r, n LIMIT 50;

// Find all startups in a specific sector
MATCH (s:Startup)-[:OPERATES_IN]->(sec:Sector {name: "FinTech"}) RETURN s;

// Get founders linked to a startup
MATCH (s:Startup {name: "ZappGo"})-[:FOUNDED_BY]->(f:Founder) RETURN f;
```

---

##  Future Enhancements

- User authentication and session storage
- Real-time graph update with WebSocket
- Export graph as PNG/PDF
- Editable graph UI through Streamlit

---

## 👨‍💻 Author

**Divyanshu** – [@github](https://github.com/divyanshu-gh)


