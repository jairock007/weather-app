from flask import Flask, render_template
import requests

app = Flask(__name__)

# OpenWeatherMap API endpoint and API key
api_endpoint = "http://api.openweathermap.org/data/2.5/weather"
api_key = "ebb7b311c4c78c3b0b8fe2f185d45d72"
city = "Bhopal"

# Fetch weather data from OpenWeatherMap API
def get_weather_data():
    params = {
        "q": city,
        "units": "metric",
        "appid": api_key
    }
    response = requests.get(api_endpoint, params=params)
    weather_data = response.json()
    return weather_data

# Render the weather data in the browser
@app.route("/")
def index():
    weather_data = get_weather_data()
    return render_template("weather.html", weather_data=weather_data)

if __name__ == "__main__":
    app.run(debug=True)