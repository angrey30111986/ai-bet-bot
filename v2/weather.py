import requests

API_KEY = "03b997d33e6e88f7b1dc3e9f179d7f17"

headers = {
    "x-apisports-key": API_KEY
}


def get_weather(fixture_id):
    url = "https://v3.football.api-sports.io/fixtures"

    response = requests.get(
        url,
        headers=headers,
        params={"id": fixture_id}
    )

    if response.status_code != 200:
        return {
            "temperature": 20,
            "wind": 0,
            "rain": 0
        }

    data = response.json()["response"]

    if not data:
        return {
            "temperature": 20,
            "wind": 0,
            "rain": 0
        }

    fixture = data[0]

    weather = fixture.get("weather")

    if not weather:
        return {
            "temperature": 20,
            "wind": 0,
            "rain": 0
        }

    return {
        "temperature": weather.get("temperature", 20),
        "wind": weather.get("wind", 0),
        "rain": weather.get("rain", 0)
    }
