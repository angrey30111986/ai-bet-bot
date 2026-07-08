"""
AI BET BOT v3
Weather API
"""

from api.client import client


def get_weather(match):

    response = client.get(
        "/fixtures",
        {
            "id": match["fixture_id"]
        }
    )

    match["weather"] = {
        "temperature": None,
        "feels_like": None,
        "humidity": None,
        "pressure": None,
        "wind_speed": None,
        "wind_direction": None,
        "description": None
    }

    if not response.get("response"):
        return match

    fixture = response["response"][0]["fixture"]

    weather = fixture.get("weather")

    if not weather:
        return match

    match["weather"]["temperature"] = weather.get("temp")
    match["weather"]["feels_like"] = weather.get("feels_like")
    match["weather"]["humidity"] = weather.get("humidity")
    match["weather"]["pressure"] = weather.get("pressure")
    match["weather"]["wind_speed"] = weather.get("wind_speed")
    match["weather"]["wind_direction"] = weather.get("wind_deg")
    match["weather"]["description"] = weather.get("description")

    return match


def is_bad_weather(match):

    weather = match["weather"]

    if weather["wind_speed"] is None:
        return False

    if weather["wind_speed"] >= 10:
        return True

    return False


if __name__ == "__main__":

    print("Weather module loaded")
