"""
AI BET BOT v3
League Standings
"""

from api.client import client


def get_standings(match):

    response = client.get(
        "/standings",
        {
            "league": match["league"]["id"],
            "season": match["league"]["season"]
        }
    )

    if not response.get("response"):
        return match

    table = response["response"][0]["league"]["standings"][0]

    home_id = match["home"]["id"]
    away_id = match["away"]["id"]

    home = None
    away = None

    for team in table:

        if team["team"]["id"] == home_id:
            home = team

        if team["team"]["id"] == away_id:
            away = team

    match["standings"] = {
        "home": {
            "rank": home["rank"] if home else None,
            "points": home["points"] if home else None,
            "played": home["all"]["played"] if home else None,
            "win": home["all"]["win"] if home else None,
            "draw": home["all"]["draw"] if home else None,
            "lose": home["all"]["lose"] if home else None,
            "goals_for": home["all"]["goals"]["for"] if home else None,
            "goals_against": home["all"]["goals"]["against"] if home else None,
            "goal_diff": home["goalsDiff"] if home else None,
            "form": home["form"] if home else None
        },

        "away": {
            "rank": away["rank"] if away else None,
            "points": away["points"] if away else None,
            "played": away["all"]["played"] if away else None,
            "win": away["all"]["win"] if away else None,
            "draw": away["all"]["draw"] if away else None,
            "lose": away["all"]["lose"] if away else None,
            "goals_for": away["all"]["goals"]["for"] if away else None,
            "goals_against": away["all"]["goals"]["against"] if away else None,
            "goal_diff": away["goalsDiff"] if away else None,
            "form": away["form"] if away else None
        }
    }

    return match
