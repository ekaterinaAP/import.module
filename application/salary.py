from datetime import datetime


def calculate_salary():
    time = datetime.today()
    print(f"время расчёта заработной платы: {time}")


if __name__ == '__main__':
    calculate_salary()
    print("В феврале фонд оплаты труда составил 5000000 рублей")
    