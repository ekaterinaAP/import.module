from datetime import date


def get_employees():
    today = date.today()
    print(f"информация о сотрудниках на дату: {today}")


if __name__ == '__main__':
    get_employees()
    