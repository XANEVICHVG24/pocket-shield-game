"""Вывод интерфейса симулятора смартфона в консоль."""

LINE = "─" * 46


def show_header():
    print("\n" + "═" * 46)
    print("        📱 КАРМАННЫЙ ЩИТ")
    print("═" * 46)


def show_intro():
    show_header()
    print(
        "\nДобро пожаловать! Сегодня тебе предстоит проверить\n"
        "свою внимательность. В течение дня ты будешь получать\n"
        "сообщения от разных организаций и людей. Некоторые из\n"
        "них могут оказаться мошенническими.\n\n"
        "Твоя задача — защитить свой смартфон и личные данные."
    )
    print("\n[1] Начать игру\n[2] Правила\n[0] Выход")


def show_rules():
    print("\n" + LINE)
    print("ПРАВИЛА:")
    print("• Проверяй отправителя и ссылки")
    print("• Не сообщай коды подтверждения")
    print("• Не переходи по незнакомым QR-кодам")
    print("• Можешь взять до 3 подсказок (это снизит баллы)")
    print(LINE)

    def show_task(task: dict):
        print("\n" + LINE)
        print(f"📨 {task['type']} от: {task['sender']}")
        print(LINE)
        print(task["text"])
        print(LINE)
        for i, opt in enumerate(task["options"], 1):
            print(f"  {i}. {opt}")
        print("  9. Взять подсказку")
        print(LINE)

    def show_feedback(correct: bool, explanation: str, points: int):
        print("\n" + LINE)
        if correct:
            print(f"✅ Верно! +{points} баллов")
        else:
            print("❌ Ошибка! +0 баллов")
        print(f"ℹ️  {explanation}")
        print(LINE)

    def show_hint(level: int, task: dict):
        hints = {
            1: f"Обрати внимание на отправителя: «{task['sender']}».",
            2: "Есть ли признаки срочности или просьба перейти по ссылке?",
            3: f"Правильный ответ: {task['options'][task['correct']]}",
        }
        print(f"\n💡 Подсказка {level}: {hints[level]}")