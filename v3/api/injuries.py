"""
AI BET BOT v3
Team Injuries
"""

from api.client import client


def get_injuries(match):

    season = match["league"]["season"]

    home = client.get(
        "/injuries",
        {
            "team": match["home"]["id"],
            "season": season
        }
    )

    away = client.get(
        "/injuries",
        {
            "team": match["away"]["id"],
            "season": season
        }
    )

    match["injuries"] = {

        "home": home.get("response", []),

        "away": away.get("response", [])

    }

    return match


def count_home(match):

    return len(match["injuries"]["home"])


def count_away(match):

    return len(match["injuries"]["away"])


if __name__ == "__main__":

    print("Injuries module")
