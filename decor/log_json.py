'''Содержит декоратор, сохраняющий параметры функции и езультат ее выполнения в json файл'''

from typing import Callable, Any
from pathlib import Path
from serialize.s_json import write_json, read_json

JSON_FILE = 'params.json'


def log_json(json_file: str = JSON_FILE, preaty_print: bool = True) -> Callable:
    def decor(func: Callable) -> Callable:
        data = read_json(json_file) if Path(json_file).is_file() else []

        def wrapper(*args) -> Any:
            result = func(*args)
            json_dict = {'args': args, 'res': str(result)}
            data.append(json_dict)
            write_json(data, json_file, preaty_print=preaty_print)
            return result
        return wrapper
    return decor
