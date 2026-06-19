# ClimateGuard-AI Agent for Climate Risk Monitoring in Kazakhstan

A multi-agent AI system that autonomously analyzes satellite imagery and hydrological data to predict flood and drought risks for agricultural regions in Kazakhstan, with persistent conversation memory powered by PostgreSQL.

---

## The Problem

Climate change is causing increasingly severe floods and droughts across Kazakhstan, destroying harvests and threatening food security. Farmers and agronomists have no accessible tool to get accurate, location-specific risk forecasts. Existing weather services provide generic predictions-not actionable, field-level intelligence.

ChatGPT and similar tools cannot solve this: they have no access to real-time satellite data, cannot process GeoTIFF or NetCDF files, and cannot run autonomous geospatial computation pipelines.

---

## What It Does

ClimateGuard is an autonomous AI agent. A farmer or agronomist types a natural language query — "assess flood risk for my district in North Kazakhstan"-and the agent analyzes regional climate risk and returns a structured assessment with risk level, key factors, and recommendations. Every conversation is saved to PostgreSQL, so the assistant remembers prior context within a session.

---

## Key Features

| Feature | Description |
|---|---|
| Region & Risk Dashboard | Select a region, risk type (flood/drought), and season for instant analysis |
| Conversation Memory | PostgreSQL stores every message; Oylan receives full history on each request |
| Region Comparison | Compare flood/drought risk between two regions side by side |
| AI-Generated Summary | Each analysis includes a short, plain-language summary |
| Multi-language | Responses in Russian, Kazakh, or English |
| Conversation History API | `GET /history/{session_id}` retrieves the full saved conversation |

---

## Architecture Overview

```
React Frontend
      |
      v
FastAPI Backend
      |
   +--+-------------------+
   |                      |
PostgreSQL            Oylan API
(messages table:      (reasoning,
 session_id, role,     contextual responses)
 content, created_at)
```

---

## Tech Stack

- **Backend:** Python / FastAPI / Uvicorn
- **Database:** PostgreSQL + SQLAlchemy (async, via asyncpg)
- **AI:** Oylan API-conversational analysis with memory
- **Frontend:** React
- **Validation:** Pydantic

---

## Getting Started

### 1. Install PostgreSQL

```bash
brew install postgresql@16
brew services start postgresql@16
```

### 2. Create the database and user

```bash
psql postgres
```

```sql
CREATE DATABASE oylan_chat;
CREATE USER chatuser WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE oylan_chat TO chatuser;
\c oylan_chat
GRANT ALL ON SCHEMA public TO chatuser;
\q
```

### 3. Set up environment variables

Create a `.env` file in the project root:

```
OYLAN_API_KEY=your_oylan_api_key
OYLAN_ASSISTANT_ID=your_assistant_id
OYLAN_BASE_URL=https://oylan.nu.edu.kz/api/v1
DATABASE_URL=postgresql+asyncpg://chatuser:yourpassword@localhost/oylan_chat
```

### 4. Install dependencies and run

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

The server runs at `http://127.0.0.1:8000`. The `messages` table is created automatically on startup. Interactive API docs are at `http://127.0.0.1:8000/docs`.

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Confirms the server is running |
| GET | `/health` | Health check |
| POST | `/chat` | Send a message; saves to DB and returns AI reply with conversation memory |
| GET | `/history/{session_id}` | Retrieve full saved conversation for a session |
| POST | `/analyze` | Analyze flood/drought risk for a Kazakhstan region |

---

## Usage

Send a message with memory:

```http
POST /chat
Content-Type: application/json

{
  "message": "Привет! Меня зовут Алия.",
  "session_id": "alice"
}
```

```http
POST /chat
Content-Type: application/json

{
  "message": "Как меня зовут?",
  "session_id": "alice"
}
```

The assistant correctly recalls "Алия" because the conversation history is stored in PostgreSQL and passed to Oylan on every request.

Retrieve history:

```http
GET /history/alice
```

---

## Project Status

In development-Lesson 5: PostgreSQL-backed conversation memory implemented. `/chat` saves and recalls message history per session; `/analyze` powers the region risk dashboard.

---

## Author

Aibike Nurakhan