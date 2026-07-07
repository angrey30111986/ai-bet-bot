from predictor import predict


def main():
    print("=== AI BET BOT ===")

    home = input("Домашня команда: ")
    away = input("Гостьова команда: ")

    result = predict(home, away, 0)

    print("\nПрогноз:")
    print(f"🏠 Домашня: {result['home']}%")
    print(f"🤝 Нічия: {result['draw']}%")
    print(f"✈️ Гості: {result['away']}%")


if __name__ == "__main__":
    main()
