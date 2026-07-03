from analyzer import analyze_match

def main():
    result = analyze_match("Реал Мадрид", "Барселона")

    print("=== ПРОГНОЗ ===")
    print("Матч:", "Реал Мадрид", "-", "Барселона")
    print("Переможець:", result["winner"])
    print("Ймовірність:", str(result["confidence"]) + "%")
    print("Ставка:", result["prediction"])

if __name__ == "__main__":
    main()
