import requests
import pandas as pd

def get_coordinates(city_name):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1"
    response = requests.get(url)
    data = response.json()
    result = data["results"][0]
    return result["latitude"], result["longitude"]

city = input("Enter city name: ")
lat, lon = get_coordinates(city)
print(f"{city} coordinates: {lat}, {lon}")

params = {
    "latitude": lat,
    "longitude": lon,
    "hourly": "temperature_2m,windspeed_10m,relativehumidity_2m",
    "forecast_days": 3
}

response = requests.get("https://api.open-meteo.com/v1/forecast", params=params)
data = response.json()

df = pd.DataFrame({
    "Time": data["hourly"]["time"],
    "Temperature (°C)": data["hourly"]["temperature_2m"],
    "Wind Speed (km/h)": data["hourly"]["windspeed_10m"],
    "Humidity (%)": data["hourly"]["relativehumidity_2m"]
})

print(df.head(5))
df.to_csv("lagos_weather_forecast.csv", index=False)
print(f"\nSaved {len(df)} hourly readings to CSV")
print(data)
