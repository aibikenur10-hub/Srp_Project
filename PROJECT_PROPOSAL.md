# Project Proposal — ClimateGuard

## Problem / Idea

Kazakhstan faces increasingly severe climate disasters — catastrophic spring floods and prolonged droughts that destroy harvests and threaten food security for millions. Farmers and agronomists currently have no accessible tool for accurate, field-level risk forecasting. Generic weather services are useless at this scale. The problem is global: the same dynamics affect agricultural regions in the US, Australia, and sub-Saharan Africa.

## What the Agent Does

ClimateGuard is an autonomous multi-agent AI system. The user submits a plain-language query — "assess flood risk for my district over the next two weeks" — and the agent autonomously connects to satellite APIs, downloads and processes raw geospatial data, applies hydrological models, self-corrects errors in its own calculations, and returns a precise risk map with actionable recommendations. No GIS expertise required.

## Why ChatGPT Cannot Do This

ChatGPT has no access to real-time satellite feeds, cannot open or process GeoTIFF or NetCDF files, has no connection to Kazhydromet or ISSAI local datasets, and cannot run autonomous code-test-fix cycles. ClimateGuard's agent does all of this autonomously.

## Key Features

- Natural language interface for farmers and agronomists
- Real-time satellite data ingestion — NASA Landsat, ESA Sentinel-2
- Autonomous Python script generation, execution, and self-correction
- Flood risk modeling based on snowmelt and water runoff data
- Drought and soil degradation analysis using multi-year historical records
- Integration with Kazhydromet archives and ISSAI hydrological datasets
- Georeferenced risk maps accurate to the meter

## Why a Wrapper

The Oylan model lives behind an API. Our FastAPI backend wraps it to hide the API key, validate and sanitize all input, inject geospatial context and historical data into every agent request, manage the autonomous code execution loop securely, and log all agent actions for debugging and research analysis.

## Tech Stack

Python · FastAPI · Uvicorn · Pydantic · PostgreSQL + PostGIS · React · Leaflet.js · Oylan API · NASA Earthdata API · ESA Copernicus API · rasterio · xarray · geopandas

## Research Roadmap

Phase 1 — Architecture design and data pipeline for one region of Kazakhstan.
Phase 2 — Flood risk module: snowmelt modeling for North Kazakhstan river basins.
Phase 3 — Drought module: soil degradation index from multi-year Sentinel-2 data.
Phase 4 — Validation against Kazhydromet ground truth data.
Phase 5 — Architecture generalization: transfer pipeline to a US or African agricultural region for international comparison and publication.
