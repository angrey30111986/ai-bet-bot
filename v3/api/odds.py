"""
AI BET BOT v3
Bookmaker Odds
"""

from api.client import client


def get_odds(match):

    response = client.get(
        "/odds",
        {
            "fixture": match["fixture_id"]
        }
    )

    match["odds"] = {
        "home": None,
        "draw": None,
        "away": None,
        "bookmaker": None
    }

    if not response.get("response"):
        return match

    bookmakers = response["response"][0].get("bookmakers", [])

    if not bookmakers:
        return match

    bookmaker = bookmakers[0]

    match["odds"]["bookmaker"] = bookmaker["name"]

    for bet in bookmaker.get("bets", []):

        if bet["name"] != "Match Winner":
            continue

        for value in bet["values"]:

            if value["value"] == "Home":
                match["odds"]["home"] = float(value["odd"])

            elif value["value"] == "Draw":
                match["odds"]["draw"] = float(value["odd"])

            elif value["value"] == "Away":
                match["odds"]["away"] = float(value["odd"])

    return match


def favorite(match):

    odds = match["odds"]

    values = {
        "Home": odds["home"],
        "Draw": odds["draw"],
        "Away": odds["away"]
    }

    values = {
        k: v for k, v in values.items()
        if v is not None
    }

    if not values:
        return None

    return min(values, key=values.get)


if __name__ == "__main__":

    print("Odds module loaded")
