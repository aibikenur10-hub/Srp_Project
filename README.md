# ClimateGuard — AI Agent for Climate Risk Monitoring in Kazakhstan

A multi-agent AI system that autonomously analyzes satellite imagery and hydrological data to predict flood and drought risks for agricultural regions in Kazakhstan.

---

## The Problem

Climate change is causing increasingly severe floods and droughts across Kazakhstan, destroying harvests and threatening food security. Farmers and agronomists have no accessible tool to get accurate, location-specific risk forecasts. Existing weather services provide generic predictions — not actionable, field-level intelligence.

ChatGPT and similar tools cannot solve this: they have no access to real-time satellite data, cannot process GeoTIFF or NetCDF files, and cannot run autonomous geospatial computation pipelines.

---

## What It Does

ClimateGuard is an autonomous AI agent. A farmer or agronomist types a natural language query — "assess flood risk for my district in North Kazakhstan over the next two weeks" — and the agent handles everything else:

1. Connects to NASA Landsat and ESA Sentinel satellite APIs and downloads relevant imagery
2. Writes and executes Python scripts to process raw geospatial data (GeoTIFF, NetCDF)
3. Applies hydrological and soil degradation models using historical data from Kazhydromet and ISSAI
4. Detects errors in its own calculations and self-corrects
5. Returns a flood or drought risk map accurate to the meter, with concrete recommendations

---

## Key Features

| Feature | Description |
|---|---|
| Satellite Data Integration | Real-time connection to NASA Landsat and ESA Sentinel APIs |
| Autonomous Code Generation | Agent writes, runs, and debugs its own Python processing scripts |
| Flood Risk Assessment | Snowmelt and water runoff modeling for river basins in Kazakhstan |
| Drought & Soil Degradation Analysis | Multi-year soil moisture trend analysis per geographic zone |
| Local Data Layer | Integration with Kazhydromet historical archives and ISSAI datasets |
| Risk Visualization | Outputs georeferenced risk maps with field-level precision |
| Natural Language Interface | Plain-language queries — no GIS expertise required |

---

## Architecture Overview

```
User (farmer / agronomist)
         |
         v
Web Interface (React)
         |
    HTTP / JSON
         |
         v
FastAPI Backend — Agent Orchestrator
         |
    +----+----------------+------------------+
    |                     |                  |
Oylan API           Satellite APIs      Local Data Layer
(reasoning,         NASA Landsat        Kazhydromet archives
 code generation,   ESA Sentinel        ISSAI hydrological
 self-correction)   (GeoTIFF, NetCDF)   datasets
    |
    v
Python Execution Engine
(geospatial processing:
 rasterio, xarray, numpy)
    |
    v
Risk Map Output + Recommendations
```

---

## Tech Stack

- **Backend:** Python / FastAPI / Uvicorn
- **Agent AI:** Oylan API — reasoning, code generation, self-correction loop
- **Satellite Data:** NASA Earthdata API (Landsat), ESA Copernicus API (Sentinel-2)
- **Geospatial Processing:** rasterio, xarray, numpy, geopandas
- **Local Data:** Kazhydromet API, ISSAI internal datasets
- **Frontend:** React + Leaflet.js (interactive map rendering)
- **Database:** PostgreSQL + PostGIS (geospatial extension)
- **Validation:** Pydantic
- **Auth:** JWT

---

## Research Potential

This project is designed as a scalable architecture. The geospatial pipeline and agent design can be transferred to any agricultural region by changing satellite coordinates — Great Plains (USA), sub-Saharan Africa, Scandinavia. Kazakhstan serves as the primary testbed due to its extreme continental climate and high vulnerability to both flood and drought events.

---

## Getting Started

```bash
git clone https://github.com/yourusername/climateguard
cd climateguard
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

The server runs at `http://127.0.0.1:8000`. Interactive API docs (Swagger) are available at `http://127.0.0.1:8000/docs`, and ReDoc at `http://127.0.0.1:8000/redoc`.

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Confirms the server is running |
| GET | `/health` | Health check for monitoring |
| POST | `/chat` | Sends a message to the agent and receives a response |

---

## Usage

Check server status:

```http
GET /
```

```json
{
  "message": "ClimateGuard assistant is running!"
}
```

Send a message to the agent:

```http
POST /chat
Content-Type: application/json

{
  "message": "Assess flood risk for North Kazakhstan"
}
```

Response (current placeholder — real Oylan integration comes next):

```json
{
  "reply": "You said: Assess flood risk for North Kazakhstan"
}
```

---

## Project Status

In development — Lesson 2: FastAPI backend skeleton with `/`, `/health`, and `/chat` (echo placeholder). Real Oylan API integration and satellite data pipelines are planned for upcoming lessons.

---

## Author

[Your Name] — ISSAI, Nazarbayev University
