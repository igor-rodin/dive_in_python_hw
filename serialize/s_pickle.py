'''Содержит функции для сериализации(десеарилизации) в формат pickle'''

import pickle
from typing import Any

__all__ = ['write_pickle', 'read_pickle']


def write_pickle(data: dict | list, pickle_file: str) -> None:
    '''
    Сериализует объект data в pickle_file
    '''
    with open(pickle_file, 'wb') as f:
        pickle.dump(data, f, protocol=pickle.DEFAULT_PROTOCOL)


def write_pickles(data: dict | list) -> str:
    '''
    Сериализует объект data в pickle строку
    '''
    return pickle.dumps(data, protocol=pickle.DEFAULT_PROTOCOL)


def read_pickle(pickle_file: str) -> Any:
    '''
    Десерилизует объект в pickle формате из pickle_file
    '''
    with open(pickle_file, mode='rb') as f:
        data = pickle.load(f)
    return data
