import requests

def get_current_location():
    response = requests.get(
        "https://ipinfo.io/json",
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    latitude, longitude = data["loc"].split(",")

    return {
        "city": data.get("city"),
        "country": data.get("country"),
        "latitude": float(latitude),
        "longitude": float(longitude)
    }

print(get_current_location())