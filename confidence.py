def confidence(home_power, away_power):

    diff = abs(home_power - away_power)

    if diff > 60:
        return 95

    if diff > 40:
        return 90

    if diff > 30:
        return 85

    if diff > 20:
        return 80

    if diff > 10:
        return 75

    return 60
