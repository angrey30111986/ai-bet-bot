"""
AI BET BOT v3
Travel Analysis
"""

import math


EARTH_RADIUS = 6371


def haversine(lat1, lon1, lat2, lon2):

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)

    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        math.sin(dlat / 2) ** 2
        + math.cos(lat1)
        * math.cos(lat2)
        * math.sin(dlon / 2) ** 2
    )

    c = 2 * math.atan2(
        math.sqrt(a),
        math.sqrt(1 - a)
    )

    return EARTH_RADIUS * c


def calculate_travel(match):

    home = match["home"]
    away = match["away"]

    if (
        "lat" not in home or
        "lon" not in home or
        "lat" not in away or
        "lon" not in away
    ):

        match["travel"] = {
            "distance_km": None,
            "home": 100,
            "away": 100
        }

        return match

    distance = haversine(

        home["lat"],
        home["lon"],

        away["lat"],
        away["lon"]

    )

    away_score = 100

    if distance > 100:

        away_score = 90

    if distance > 300:

        away_score = 80

    if distance > 600:

        away_score = 70

    if distance > 1000:

        away_score = 60

    if distance > 2000:

        away_score = 45

    match["travel"] = {

        "distance_km": round(distance),

        "home": 100,

        "away": away_score

    }

    return match
