from elo import get_elo
from fatigue import get_fatigue
from injuries import get_injuries
from cards import get_cards
from weather import get_weather


def collect_data(home_team, away_team, fixture_id=None):

    data = {}

    data.update(get_elo(home_team, away_team))
    data.update(get_fatigue(home_team, away_team))

    if fixture_id:

        injuries = get_injuries(fixture_id)

        data["home_injuries"] = 0
        data["away_injuries"] = 0

        if isinstance(injuries, list):

            for player in injuries:

                team = player.get("team", {}).get("name", "")

                if team == home_team:
                    data["home_injuries"] += 1

                elif team == away_team:
                    data["away_injuries"] += 1

        cards = get_cards(fixture_id)

        if isinstance(cards, dict):
            data.update(cards)

        weather = get_weather(fixture_id)

        if isinstance(weather, dict):
            data.update(weather)

    else:

        data["home_injuries"] = 0
        data["away_injuries"] = 0

        data["home_yellow"] = 0
        data["away_yellow"] = 0

        data["home_red"] = 0
        data["away_red"] = 0

        data["temperature"] = None
        data["weather"] = None
        data["wind"] = None
        data["humidity"] = None

    return data
