from analyzer import analyze_match

def main():
    team1 = "Real Madrid"
    team2 = "Barcelona"

    result = analyze_match(team1, team2)

    print("Матч:", result["team1"], "-", result["team2"])
    print("Ймовірність:", result["confidence"], "%")
    print("Рекомендація:", result["recommendation"])

if __name__ == "__main__":
    main()
