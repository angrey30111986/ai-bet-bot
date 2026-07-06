import joblib

model = joblib.load("football_ai.pkl")

def predict(goal_diff, total_goals):

    probs = model.predict_proba([[goal_diff, total_goals]])[0]

    return {
        "home": round(probs[0] * 100, 1),
        "draw": round(probs[1] * 100, 1),
        "away": round(probs[2] * 100, 1)
    }


if __name__ == "__main__":

    result = predict(1, 3)

    print(result)
