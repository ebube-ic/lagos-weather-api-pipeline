# Lagos Weather API Pipeline

A Python data pipeline that fetches live 3-day hourly weather 
forecast data for Lagos, Nigeria using the Open-Meteo API.

## Tools Used
- Python (requests, pandas)
- Open-Meteo API (free, no authentication required)
- Tableau Public

## What it does
- Calls the Open-Meteo REST API with custom parameters
- Extracts hourly temperature, wind speed and humidity data
- Structures the response into a clean pandas DataFrame
- Exports 72 hourly readings to CSV
- Visualizes temperature and wind speed trends as time-series charts

## Why this matters for EEE
This pipeline mirrors how industrial IoT systems work —
sensors transmit data to an API endpoint, Python pulls and 
processes it, and engineers monitor trends on a dashboard.
The same logic applies to SCADA systems and process historians.

## Dashboard
[View live on Tableau Public] — paste your link here

## Files
- `api_intro.py` — the API pipeline script
- `lagos_weather_forecast.csv` — 72 hours of forecast data
