"""
AI BET BOT v3
Predict Match
"""

import joblib

from config import MODEL_PATH

from ai.features import build_features


class Predictor:

    def __init__(self):

        self.model = joblib.load(MODEL_PATH)

    def predict(self, match):

        features = [build_features(match)]

        prediction = self.model.predict(features)[0]

        probability = self.model.predict_proba(features)[0]

        match["ai"] = {

            "prediction": int(prediction),

            "home": round(probability[0] * 100, 2),

            "draw": round(probability[1] * 100, 2),

            "away": round(probability[2] * 100, 2)

        }

        return match


predictor = Predictor()


if __name__ == "__main__":

    print("Predictor loaded")
