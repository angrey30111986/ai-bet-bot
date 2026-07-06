def predict(home_form, away_form):

    score = home_form - away_form

    if score >= 6:
        return "П1", 88

    elif score >= 3:
        return "П1", 78

    elif score >= 1:
        return "П1", 65

    elif score == 0:
        return "X", 55

    elif score <= -6:
        return "П2", 88

    elif score <= -3:
        return "П2", 78

    else:
        return "П2", 65
