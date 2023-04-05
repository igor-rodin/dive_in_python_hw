'''Содержит функцию для генерации параметров уравнений'''

from random import uniform
import serialize.s_csv as s_csv


def gen_params_csv(file_csv: str = 'params.csv', count=10, min_val=-5, max_val=5) -> None:
    '''
    Генерирует параметры квадратного уравнения и записывает в csv файл
    '''
    data = []
    for _ in range(count):
        params = {}
        params['a'] = uniform(min_val, max_val)
        params['b'] = uniform(min_val, max_val)
        params['c'] = uniform(min_val, max_val)
        data.append(params)

    s_csv.write_ld_csv(data, file_csv)
