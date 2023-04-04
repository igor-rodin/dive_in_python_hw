'''Функции для решения квадратного уравнения'''

__all__ = ['solve_quad', 'gen_params_csv']

from random import uniform
from typing import Any
import serialize.s_csv as s_csv


def _desc(a: float | int, b: float | int, c: float | int) -> float:
    '''Возвращает дескриминант квадратного уравнения'''
    return b**2 - 4 * a * c


def _valid(a: Any) -> bool:
    '''
    Проверяет тип аргумента уравнения
    '''
    return type(a) == int or type(a) == float


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


def solve_quad(* args) -> tuple[float | complex, float | complex] | float | None:
    '''
    Находит корни кавдратного уравнения a * x^2 + b * x + c = 0
    '''
    if len(args) != 3:
        print(
            f'Неверное количество аргументов. Ожидается 3, получено {len(args)}')
        return None

    a, b, c = args

    if not _valid(a) or not _valid(b) or not _valid(c):
        print(
            'Неверный тип параметров уравнения')
        return None

    if a == 0 and b == 0:
        print(
            'Уранение не имеет решений')
        return None
    elif a == 0:
        return -c / b

    desc = _desc(a, b, c)
    x1 = (-b + desc ** 0.5) / 2 * a
    x2 = (-b - desc ** 0.5) / 2 * a

    return (x1, x2) if abs(x1) < abs(x2) else (x2, x1)


if __name__ == '__main__':
    params = [1., 0., -1]
    gen_params_csv()
    roots = solve_quad(*params)

    print(f'{roots= }')
