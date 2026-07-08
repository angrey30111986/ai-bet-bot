"""
AI BET BOT v3
Team Statistics
"""

from api.client import client


def get_team_stats(match):

    fixture_id = match["fixture_id"]

    response = client.get(
        "/fixtures/statistics",
        {
            "fixture": fixture_id
        }
    )

    match["team_stats"] = {

        "home": {},

        "away": {}

    }

    if not response.get("response"):

        return match

    for team in response["response"]:

        side = None

        if team["team"]["id"] == match["home"]["id"]:

            side = "home"

        elif team["team"]["id"] == match["away"]["id"]:

            side = "away"

        if side is None:

            continue

        stats = {}

        for item in team["statistics"]:

            key = (
                item["type"]
                .lower()
                .replace(" ", "_")
                .replace("%", "percent")
            )

            stats[key] = item["value"]

        match["team_stats"][side] = stats

    return match


def get_stat(match, side, stat_name, default=0):

    return match.get(
        "team_stats",
        {}
    ).get(
        side,
        {}
    ).get(
        stat_name,
        default
    )


if __name__ == "__main__":

    print("Team Stats module loaded")
