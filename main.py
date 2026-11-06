"""Карманный щит — обучающая игра по смишингу и QRishing."""

from tasks import TASKS
from scoring import task_points, get_rank
import ui


def play_round() -> tuple[int, int, int]:
    """Проходит 6 заданий. Возвращает (баллы, верных, подсказок)."""
    total_score = 0
    correct_count = 0
    hints_total = 0

    for task in TASKS:
        hints_used = 0
        while True:
            ui.show_task(task)
            choice = input("Твой выбор: ").strip()

            if choice == "9":
                if hints_used < 3:
                    hints_used += 1
                    hints_total += 1
                    ui.show_hint(hints_used, task)
                else:
                    print("Подсказки закончились.")
                continue

            if choice not in {"1", "2", "3"}:
                print("Введи 1–3 или 9 для подсказки.")
                continue

            is_correct = (int(choice) - 1) == task["correct"]
            points = task_points(is_correct, hints_used)
            total_score += points
            if is_correct:
                correct_count += 1

            ui.show_feedback(is_correct, task["explanation"], points)

            if is_correct:
                break

            again = input("Повторить задание? (д/н): ").strip().lower()
            if again != "д":
                break

    return total_score, correct_count, hints_total


def main():
    while True:
        ui.show_intro()
        cmd = input("\nВыбор: ").strip()

        if cmd == "1":
            score, correct, hints = play_round()
            ui.show_results(score, correct, hints, get_rank(score))
            if input("\nВыбор: ").strip() != "1":
                print("До встречи!")
                break
        elif cmd == "2":
            ui.show_rules()
        elif cmd == "0":
            print("До встречи!")
            break


if __name__ == "__main__":
    main()