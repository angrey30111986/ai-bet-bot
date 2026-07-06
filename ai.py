from confidence import confidence

def predict(home_power, away_power):

    if home_power > away_power:

        return {
            "prediction": "П1",
            "confidence": confidence(home_power, away_power)
        }

    elif away_power > home_power:

        return {
            "prediction": "П2",
            "confidence": confidence(home_power, away_power)
        }

    else:

        return {
            "prediction": "Х",
            "confidence": 55
        }
