"""
AI BET BOT v3
Fixtures Loader
"""

from datetime import datetime, timedelta

from api.client import client
from config import TIMEZONE


def create_match(fixture):

    return {

        "fixture_id": fixture["fixture"]["id"],

        "date": fixture["fixture"]["date"],

        "timestamp": fixture["fixture"]["timestamp"],

        "status": fixture["fixture"]["status"]["short"],

        "league": {

            "id": fixture["league"]["id"],
            "name": fixture["league"]["name"],
            "country": fixture["league"]["country"],
            "season": fixture["league"]["season"],
            "round": fixture["league"]["round"]

        },

        "home": {

            "id": fixture["teams"]["home"]["id"],
            "name": fixture["teams"]["home"]["name"]

        },

        "away": {

            "id": fixture["teams"]["away"]["id"],
            "name": fixture["teams"]["away"]["name"]

        },

        "weather": {},
        "standings": {},
        "h2h": {},
        "injuries": {},
        "lineups": {},
        "odds": {},
        "elo": {},
        "form": {},
        "fatigue": {},
        "travel": {},
        "importance": {},
        "analysis": {},
        "prediction": {}

    }


def load(date):

    response = client.get(

        "/fixtures",

        {

            "date": date,
            "timezone": TIMEZONE

        }

    )

    matches = []

    for fixture in response.get("response", []):

        matches.append(

            create_match(fixture)

        )

    return matches


def today():

    return load(

        datetime.now().strftime("%Y-%m-%d")

    )


def tomorrow():

    return load(

        (

            datetime.now() +

            timedelta(days=1)

        ).strftime("%Y-%m-%d")

    )


def all_matches():

    return today() + tomorrow()


if __name__ == "__main__":

    games = all_matches()

    print(f"Matches: {len(games)}")

    for game in games:

        print(

            game["home"]["name"],

            "-",

            game["away"]["name"]

        )
