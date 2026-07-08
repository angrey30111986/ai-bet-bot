"""
AI BET BOT v3
Head To Head
"""

from api.client import client


def get_h2h(match, last=10):

    response = client.get(
        "/fixtures/headtohead",
        {
            "h2h": f'{match["home"]["id"]}-{match["away"]["id"]}',
            "last": last
        }
    )

    games = response.get("response", [])

    home_win = 0
    away_win = 0
    draw = 0

    for game in games:

        home = game["teams"]["home"]["id"]
        away = game["teams"]["away"]["id"]

        goals_home = game["goals"]["home"]
        goals_away = game["goals"]["away"]

        if goals_home is None or goals_away is None:
            continue

        if goals_home == goals_away:
            draw += 1

        elif goals_home > goals_away:

            if home == match["home"]["id"]:
                home_win += 1
            else:
                away_win += 1

        else:

            if away == match["home"]["id"]:
                home_win += 1
            else:
                away_win += 1

    match["h2h"] = {

        "matches": len(games),

        "home_win": home_win,

        "draw": draw,

        "away_win": away_win

    }

    return match
