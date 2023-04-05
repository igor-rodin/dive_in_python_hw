'''Содержит декоратор, применяющий данные из csv файла в качестве параметров функции'''

from typing import Callable, Any
from serialize.s_csv import read_l_csv

CSV_FILE = 'params.csv'


def csv_params(csv_file: str = CSV_FILE) -> Callable:
    def decor(func: Callable) -> Callable:
        params = []
        result = []
        params = read_l_csv(csv_file)

        def wrapper() -> Any:
            for param in params:
                res = func(*param)
                result.append(res)
        return wrapper
    return decor
