"""
AI BET BOT v3
Feature Builder
"""


FEATURES = [

    "home_form",
    "away_form",

    "home_elo",
    "away_elo",

    "home_rank",
    "away_rank",

    "home_points",
    "away_points",

    "home_h2h",
    "away_h2h",

    "home_injuries",
    "away_injuries",

    "home_fatigue",
    "away_fatigue",

    "home_travel",
    "away_travel",

    "home_odds",
    "draw_odds",
    "away_odds"

]


def build_features(match):

    return [

        match["form"]["home"]["score"],
        match["form"]["away"]["score"],

        match["elo"]["home"],
        match["elo"]["away"],

        match["standings"]["home"]["rank"],
        match["standings"]["away"]["rank"],

        match["standings"]["home"]["points"],
        match["standings"]["away"]["points"],

        match["h2h"]["home_win"],
        match["h2h"]["away_win"],

        len(match["injuries"]["home"]),
        len(match["injuries"]["away"]),

        match["fatigue"]["home"],
        match["fatigue"]["away"],

        match["travel"]["home"],
        match["travel"]["away"],

        match["odds"]["home"],
        match["odds"]["draw"],
        match["odds"]["away"]

    ]
