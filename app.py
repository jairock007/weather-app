import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenWeatherMap API endpoint and API key
api_endpoint = "http://api.openweathermap.org/data/2.5/weather"

api_key = os.getenv('API_KEY')


# List of cities
cities = [
    {"name": "Bhopal", "id": "1275841"},
    {"name": "Mumbai", "id": "1275339"},
    {"name": "Delhi", "id": "1273294"},
    {"name": "Bangalore", "id": "1277333"},
    {"name": "Hyderabad", "id": "1269843"}
]

# Fetch weather data from OpenWeatherMap API
def get_weather_data(city_id):
    params = {
        "id": city_id,
        "units": "metric",
        "appid": api_key
    }
    response = requests.get(api_endpoint, params=params)
    weather_data = response.json()
    return weather_data

# Streamlit app
st.title("Weather App")

# City selection
city_id = st.selectbox("Select a city", [city["name"] for city in cities])

# Get weather data for selected city
for city in cities:
    if city["name"] == city_id:
        weather_data = get_weather_data(city["id"])

# Display weather data
if 'weather' in weather_data and weather_data['weather']:
    st.write(f"Weather in {city_id}")
    st.write(f"Description: {weather_data['weather'][0]['description']}")
    st.write(f"Temperature: {weather_data['main']['temp']}°C")
    st.write(f"Humidity: {weather_data['main']['humidity']}%")
    st.write(f"Wind Speed: {weather_data['wind']['speed']} m/s")
else:
    st.write(f"Unable to retrieve weather data for {city_id}.")