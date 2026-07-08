"""
AI BET BOT v3
Fixtures Loader
"""

from datetime import datetime, timedelta

from api.client import client
from config import TIMEZONE


def _empty_match():

    return {
        "fixture_id": None,
        "date": None,
        "timestamp": None,
        "status": None,

        "league": {},

        "home": {},

        "away": {},

        "standings": {},

        "h2h": {},

        "injuries": {},

        "lineups": {},

        "weather": {},

        "odds": {},

        "elo": {},

        "form": {},

        "fatigue": {},

        "travel": {},

        "importance": {},

        "analysis": {},

        "prediction": {}
    }


def build_match(fixture):

    match = _empty_match()

    match["fixture_id"] = fixture["fixture"]["id"]
    match["date"] = fixture["fixture"]["date"]
    match["timestamp"] = fixture["fixture"]["timestamp"]
    match["status"] = fixture["fixture"]["status"]["short"]

    match["league"] = {
        "id": fixture["league"]["id"],
        "name": fixture["league"]["name"],
        "country": fixture["league"]["country"],
        "season": fixture["league"]["season"],
        "round": fixture["league"]["round"]
    }

    match["home"] = {
        "id": fixture["teams"]["home"]["id"],
        "name": fixture["teams"]["home"]["name"]
    }

    match["away"] = {
        "id": fixture["teams"]["away"]["id"],
        "name": fixture["teams"]["away"]["name"]
    }

    return match


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

        matches.append(build_match(fixture))

    return matches


def today():

    return load(

        datetime.now().strftime("%Y-%m-%d")

    )


def tomorrow():

    return load(

        (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

    )


def all_matches():

    return today() + tomorrow()


if __name__ == "__main__":

    matches = all_matches()

    print(f"Loaded {len(matches)} matches")

    for match in matches:

        print(
            f'{match["home"]["name"]} vs {match["away"]["name"]}'
        )
