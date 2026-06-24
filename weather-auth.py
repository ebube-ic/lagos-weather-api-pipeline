import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("WEATHER_API_KEY")

city = input("Enter city name: ")

def get_coordinates(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    response = requests.get(url)
    data = response.json()
    results = data["results"][0]       
    return results["latitude"], results["longitude"] 

lat, long = get_coordinates(city)
print(f"{city} coordinates: {lat}, {long}")

#################################################################################################################################

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

print(f"\nWeather in {city}:")
print(f"Temperature: {data['main']['temp']}°C")
print(f"Feels like: {data['main']['feels_like']}°C")
print(f"Humidity: {data['main']['humidity']}%")
print(f"Condition: {data['weather'][0]['description']}")
print(f"Wind Speed: {data['wind']['speed']} m/s")

#################################################################################################################################

params = {
    "latitude": lat,
    "longitude": long,
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

#################################################################################################################################

print(df.head(5))
df.to_csv("lagos_weather_forecast.csv", index=False)
print(f"\nSaved {len(df)} hourly readings to CSV")
