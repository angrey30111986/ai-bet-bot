"""
AI BET BOT v3
AI Score Engine
"""


class ScoreEngine:

    def __init__(self):

        self.weights = {

            "elo": 18,

            "form": 18,

            "standings": 8,

            "h2h": 10,

            "injuries": 12,

            "lineups": 8,

            "odds": 12,

            "fatigue": 5,

            "travel": 3,

            "importance": 2,

            "weather": 2

        }

    def calculate(self, match):

        home = 0.0
        away = 0.0

        # ---------------- ELO ----------------

        home += match["elo"]["home"] * self.weights["elo"] / 100
        away += match["elo"]["away"] * self.weights["elo"] / 100

        # ---------------- FORM ----------------

        home += match["form"]["home"]["score"] * self.weights["form"] / 100
        away += match["form"]["away"]["score"] * self.weights["form"] / 100

        # ---------------- STANDINGS ----------------

        home_rank = match["standings"]["home"]["rank"]
        away_rank = match["standings"]["away"]["rank"]

        if home_rank and away_rank:

            total = home_rank + away_rank

            home += (
                away_rank /
                total
            ) * self.weights["standings"]

            away += (
                home_rank /
                total
            ) * self.weights["standings"]

        # ---------------- H2H ----------------

        games = match["h2h"]["matches"]

        if games:

            home += (
                match["h2h"]["home_win"] /
                games
            ) * self.weights["h2h"]

            away += (
                match["h2h"]["away_win"] /
                games
            ) * self.weights["h2h"]

        # ---------------- INJURIES ----------------

        home_inj = len(match["injuries"]["home"])
        away_inj = len(match["injuries"]["away"])

        if home_inj < away_inj:

            home += self.weights["injuries"]

        elif away_inj < home_inj:

            away += self.weights["injuries"]

        # ---------------- FATIGUE ----------------

        home += (
            match["fatigue"]["home"] *
            self.weights["fatigue"] / 100
        )

        away += (
            match["fatigue"]["away"] *
            self.weights["fatigue"] / 100
        )

        # ---------------- TRAVEL ----------------

        home += (
            match["travel"]["home"] *
            self.weights["travel"] / 100
        )

        away += (
            match["travel"]["away"] *
            self.weights["travel"] / 100
        )

        # ---------------- WEATHER ----------------

        if not match["weather"]:

            home += 1
            away += 1

        # ---------------- ODDS ----------------

        odds = match["odds"]

        if (
            odds["home"] and
            odds["away"]
        ):

            if odds["home"] < odds["away"]:

                home += self.weights["odds"]

            else:

                away += self.weights["odds"]

        total = home + away

        if total == 0:

            match["prediction"] = {

                "home": 33.3,

                "draw": 33.3,

                "away": 33.3

            }

            return match

        home_percent = round(home / total * 100, 2)
        away_percent = round(away / total * 100, 2)

        draw = round(
            max(
                0,
                100 - home_percent - away_percent
            ),
            2
        )

        match["prediction"] = {

            "home": home_percent,

            "draw": draw,

            "away": away_percent

        }

        return match


engine = ScoreEngine()
