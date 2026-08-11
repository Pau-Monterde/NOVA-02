import requests
from engine.models.context_model import RequestContext
from engine.models.parser_models import EntityData
from db import get_user
from llm_manager import generate_response

def get_coordinates(location:str):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": location,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    if "results" not in data or not data["results"]:
        return None

    result = data["results"][0]

    return {
        "name": result["name"],
        "latitude": result["latitude"],
        "longitude": result["longitude"],
        "admin": result["admin2"]
    }

def get_weather(location:str):
    url = "https://api.open-meteo.com/v1/forecast"
    coordinates = get_coordinates(location)

    WEATHER_CODES = {
        0: "clear sky",

        1: "mainly clear",
        2: "partly cloudy",
        3: "overcast",

        45: "fog",
        48: "depositing rime fog",

        51: "light drizzle",
        53: "moderate drizzle",
        55: "dense drizzle",

        56: "light freezing drizzle",
        57: "dense freezing drizzle",

        61: "slight rain",
        63: "moderate rain",
        65: "heavy rain",

        66: "light freezing rain",
        67: "heavy freezing rain",

        71: "slight snow fall",
        73: "moderate snow fall",
        75: "heavy snow fall",

        77: "snow grains",

        80: "slight rain showers",
        81: "moderate rain showers",
        82: "violent rain showers",

        85: "slight snow showers",
        86: "heavy snow showers",

        95: "thunderstorm",
        96: "thunderstorm with slight hail",
        99: "thunderstorm with heavy hail"
    }

    params = {
        "latitude": coordinates["latitude"],
        "longitude": coordinates["longitude"],
        "current": "temperature_2m,weather_code",
        "timezone": "auto"
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    w_data = data["current"]


    return f"The current weather in {location} is {w_data["temperature_2m"]} ºC and {WEATHER_CODES[w_data["weather_code"]]}"

def show_wheather(context:RequestContext):
    url = "https://api.open-meteo.com/v1/forecast"
    ner_list = context.parsed_text.linguistic_analisys.ner
    locations:list[EntityData] = []
    response = ""

    for ner in ner_list:
        if ner.label == "GPE":
            locations.append(ner.text)

    if len(locations) == 0:
        user_location = get_user().location

        if user_location != "":
            locations.append(user_location)

        else:
            locations.append(input(generate_response("Of which location should I give you the weather?") + ": "))
    
    for location in locations:
        w_string = get_weather(location)
        response += w_string
        
    return response
            

    