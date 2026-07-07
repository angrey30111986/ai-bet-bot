import requests
from config import API_KEY

URL = "https://v3.football.api-sports.io/fixtures"

HEADERS = {
    "x-apisports-key": API_KEY
}


def get_weather(fixture_id):
    response = requests.get(
        URL,
        headers=HEADERS,
        params={
            "id": fixture_id
        },
        timeout=20
    )

    if response.status_code != 200:
        return None

    data = response.json()

    if not data["response"]:
        return None

    fixture = data["response"][0]

    return {
        "temperature": fixture.get("fixture", {}).get("temperature"),
        "weather": fixture.get("fixture", {}).get("weather"),
        "wind": fixture.get("fixture", {}).get("wind"),
        "humidity": fixture.get("fixture", {}).get("humidity")
    }


if __name__ == "__main__":
    print(get_weather(1035038))
