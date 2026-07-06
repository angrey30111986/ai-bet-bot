from team_stats import team_statistics

def build(home_id, away_id, league, season):

    home = team_statistics(home_id, league, season)
    away = team_statistics(away_id, league, season)

    return {

        "home_played":
            home["fixtures"]["played"]["total"],

        "away_played":
            away["fixtures"]["played"]["total"],

        "home_win":
            home["fixtures"]["wins"]["total"],

        "away_win":
            away["fixtures"]["wins"]["total"],

        "home_draw":
            home["fixtures"]["draws"]["total"],

        "away_draw":
            away["fixtures"]["draws"]["total"],

        "home_loss":
            home["fixtures"]["loses"]["total"],

        "away_loss":
            away["fixtures"]["loses"]["total"],

        "home_scored":
            home["goals"]["for"]["total"]["total"],

        "away_scored":
            away["goals"]["for"]["total"]["total"],

        "home_conceded":
            home["goals"]["against"]["total"]["total"],

        "away_conceded":
            away["goals"]["against"]["total"]["total"]

    }
