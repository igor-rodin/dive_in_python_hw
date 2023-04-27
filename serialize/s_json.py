'''Содержит функции для сериализации(десеарилизации) в формат json'''

__all__ = ['write_json', 'read_json']

import json


def write_json(data: list | dict, json_file: str, preaty_print=False) -> None:
    '''
    Записывает в файл json_file объект data
    '''
    with open(json_file, mode='w', encoding='utf-8') as f:
        indent_size = 2 if preaty_print else None
        json.dump(data, f, ensure_ascii=False, indent=indent_size)


def read_json(json_file: str) -> list | dict:
    with open(json_file, mode='r', encoding='utf-8') as f:
        data = json.load(f)
    return data
