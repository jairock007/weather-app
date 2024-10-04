# Weather App

This is a simple weather app built using Streamlit and the OpenWeatherMap API.

## Functionality

The app allows users to select a city from a list and displays the current weather data for that city. The weather data includes:

- Description
- Temperature (in Celsius)
- Humidity
- Wind Speed

## Code Overview

The code is written in Python and uses the following libraries:

- `streamlit` for building the app
- `requests` for making API calls to OpenWeatherMap
- `os` and `dotenv` for loading environment variables

The code consists of the following main components:

- `get_weather_data` function: makes an API call to OpenWeatherMap to retrieve weather data for a given city ID
- Streamlit app: creates a dropdown menu for selecting a city, retrieves weather data for the selected city, and displays the weather data

## Environment Variables

The app uses an environment variable `API_KEY` to store the OpenWeatherMap API key. This variable is loaded using the `dotenv` library.

## Cities

The app includes a list of cities with their corresponding IDs. The list can be modified to include additional cities.

## API Endpoint

The app uses the OpenWeatherMap API endpoint `http://api.openweathermap.org/data/2.5/weather` to retrieve weather data.

## Usage

To run the app, simply execute the `app.py` file using `streamlit run app.py`. Select a city from the dropdown menu to view the current weather data.

## Limitations

The app does not handle errors that may occur when making API calls to OpenWeatherMap. Additionally, the app only displays weather data for a limited number of cities.

## Contributing

This project is open to contributions. If you would like to add additional features or cities, please submit a pull request.
