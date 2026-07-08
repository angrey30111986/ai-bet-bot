"""
AI BET BOT v3
Predicted Lineups
"""

from api.client import client


def get_lineups(match):

    response = client.get(
        "/fixtures/lineups",
        {
            "fixture": match["fixture_id"]
        }
    )

    match["lineups"] = {

        "home": {},

        "away": {}

    }

    for team in response.get("response", []):

        side = None

        if team["team"]["id"] == match["home"]["id"]:
            side = "home"

        elif team["team"]["id"] == match["away"]["id"]:
            side = "away"

        if side is None:
            continue

        match["lineups"][side] = {

            "formation": team.get("formation"),

            "coach": team.get("coach", {}),

            "startXI": team.get("startXI", []),

            "substitutes": team.get("substitutes", [])

        }

    return match


def starting_players(match, side):

    players = []

    if side not in ("home", "away"):
        return players

    lineup = match["lineups"].get(side, {})

    for player in lineup.get("startXI", []):

        players.append(player["player"]["name"])

    return players


if __name__ == "__main__":

    print("Lineups module loaded")
