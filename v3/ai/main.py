"""
AI BET BOT v3
Main
"""

from api.fixtures import get_today_matches

from api.standings import get_standings
from api.h2h import get_h2h
from api.injuries import get_injuries
from api.lineups import get_lineups
from api.odds import get_odds
from api.weather import get_weather
from api.team_stats import get_team_stats

from analysis.form import calculate_form
from analysis.elo import calculate_elo
from analysis.fatigue import calculate_fatigue
from analysis.travel import calculate_travel
from analysis.importance import calculate_importance
from analysis.confidence import calculate_confidence

from analysis.score_engine import engine

from ai.predictor import predictor


def process(match):

    get_standings(match)
    get_h2h(match)
    get_injuries(match)
    get_lineups(match)
    get_odds(match)
    get_weather(match)
    get_team_stats(match)

    calculate_form(match)
    calculate_elo(match)
    calculate_fatigue(match)
    calculate_travel(match)
    calculate_importance(match)
    calculate_confidence(match)

    engine.calculate(match)

    predictor.predict(match)

    return match


def main():

    matches = get_today_matches()

    print("=" * 70)
    print("AI BET BOT v3")
    print("=" * 70)

    for match in matches:

        process(match)

        print()

        print(
            match["home"]["name"],
            "-",
            match["away"]["name"]
        )

        print(
            "AI:",
            match["ai"]["home"],
            "%",
            "|",
            match["ai"]["draw"],
            "%",
            "|",
            match["ai"]["away"],
            "%"
        )

        print(
            "Confidence:",
            match["confidence"]
        )

        print("-" * 70)


if __name__ == "__main__":

    main()
