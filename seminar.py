# Задание №1
# Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.
import logging
from typing import Callable, Any
import argparse

# logging.basicConfig(filename="error.log", encoding="utf-8", level=logging.WARNING)
# logger = logging.getLogger(__name__)


def div(a: int, b: int) -> float:
    res = None
    try:
        res = a / b
    except ZeroDivisionError as e:
        logger.error(e)
    return res


# Задание №2
# На семинаре про декораторы был создан логирующий декоратор.
# Он сохранял аргументы функции и результат её работы в файл.
# Напишите аналогичный декоратор, но внутри используйте модуль logging.

# FORMAT = "{levelname:<8} - {asctime}. {msg}"

# logging.basicConfig(
#     filename="data.log",
#     encoding="utf-8",
#     level=logging.INFO,
#     style="{",
#     format=FORMAT,
# )
# logger = logging.getLogger(__name__)


def log(func: Callable) -> Callable:
    def wrapper(*args) -> Any:
        result = func(*args)
        json_dict = {"args": args, "res": str(result)}
        msg = f"Функция: {func.__name__}, {json_dict} "
        logger.info(msg)
        return result

    return wrapper


# Задание №3
# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.

# Задание №4
# Функция получает на вход текст вида: “1-й четверг ноября”, “3- я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.


import datetime
import sys

logging.basicConfig(
    filename="data.log",
    encoding="utf-8",
    level=logging.ERROR,
    style="{",
)
logger = logging.getLogger(__name__)

months = [
    "янв",
    "фев",
    "мар",
    "апр",
    "мая",
    "июн",
    "июл",
    "авг",
    "сен",
    "окт",
    "ноя",
    "дек",
]

days = ["пон", "вто", "сре", "чет", "пят", "суб", "вос"]


def parse_date(date: str) -> datetime:
    try:
        week_num, day, month = date.split()
        week_num = int(week_num.split("-")[0])
    except ValueError as e:
        logger.error("Не смогли распарсить")
        return None

    year = datetime.datetime.now().year
    month_num = months.index(month[:3]) + 1
    day_num = days.index(day[:3])

    counter = 0
    for i in range(1, 32):
        dat = datetime.datetime(day=i, month=month_num, year=year)
        if dat.weekday() == day_num:
            counter += 1
            if counter == week_num:
                return dat


# Задание №5
# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить.
# В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
# *Научите функцию распознавать не только текстовое  названия дня недели и месяца, но и числовые, т.е не мая, а 5.

def get_args():
    args = argparse.ArgumentParser(description="Получаем аргументы")
    args.add_argument("-d", "--day", default=1)
    args.add_argument("-w", "--week", default=datetime.datetime.now().weekday())
    args.add_argument("-m", "--month", default=datetime.datetime.now().month)

    arg_res = args.parse_args()
    month_str = (
        months[arg_res.month - 1] if isinstance(arg_res.month, int) else arg_res.month
    )
    print(f"{arg_res.day} {arg_res.week} {month_str}")
    return parse_date(f"{arg_res.day} {arg_res.week} {month_str}")


if __name__ == "__main__":
    # print(div(4, 3))
    # print(div(4, 0))
    # sum(2.6, 90)
    # sum(21, -8)

    dt = "3-я среда мая"
    print(get_args())
    # print(parse_date(dt))
