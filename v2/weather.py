import requests
from config import BASE_URL, HEADERS, TIMEOUT


def get_weather(fixture_id):

    if fixture_id is None:
        return {
            "temperature": None,
            "weather": None,
            "wind": None,
            "humidity": None
        }

    try:

        response = requests.get(
            f"{BASE_URL}/fixtures",
            headers=HEADERS,
            params={"id": fixture_id},
            timeout=TIMEOUT
        )

        if response.status_code != 200:
            raise Exception()

        data = response.json().get("response", [])

        if not data:
            raise Exception()

        fixture = data[0].get("fixture", {})

        return {
            "temperature": fixture.get("temperature"),
            "weather": fixture.get("weather"),
            "wind": fixture.get("wind"),
            "humidity": fixture.get("humidity")
        }

    except Exception:

        return {
            "temperature": None,
            "weather": None,
            "wind": None,
            "humidity": None
        }


if __name__ == "__main__":

    print(get_weather(1035038))
