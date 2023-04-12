'''Класс Matrix с базовыми операциями сложения, умножения, сравнения'''

import random
import copy
from typing import Self


class Matrix:
    def __init__(self, rows: int, cols: int, data: list[list[int | float] | int | float] = None) -> None:
        self.__rows = rows
        self.__cols = cols

        if data is None:
            self._data_type = 'd'
            self._data = [
                [0 for _ in range(self.cols)] for _ in range(self.rows)]
        else:
            if isinstance(data, list) and (self.rows != len(data) or self.cols != len(data[0])):
                raise TypeError(
                    f"Размер массива {self.rows} x {self.cols} не соответствует размеру данных data")

            self._data_type = 'd' if type(data) is int or type(
                data[0]) is int or type(data[0][0]) is int else 'f'
            if type(data) is list:
                self._data = copy.deepcopy(data)
            else:
                self._data = [
                    [data for _ in range(self.cols)] for _ in range(self.rows)]

    @property
    def rows(self):
        return self.__rows

    @property
    def cols(self):
        return self.__cols

    def __str__(self) -> str:
        res = []
        for row in self._data:
            l = [f'{val:>6.2f}' if self._data_type ==
                 'f' else f'{val:>4d}' for val in row]
            res.append(', '.join(l))
        return '\n'.join(res)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name}({self.rows}, {self.cols}, {self._data})'

    def fill_random_int(self, start: int = -10, stop: int = 10):
        '''Заполняет матрицу случайными целыми числами от start до stop'''
        self._data_type = 'd'
        self._data = [
            [random.randrange(start, stop + 1) for _ in range(self.cols)] for _ in range(self.rows)]

    def fill_random_float(self, start: float = -10, stop: float = 10):
        '''Заполняет матрицу случайными вещественными числами от start до stop'''
        self._data_type = 'f'
        self._data = [
            [random.uniform(start, stop) for _ in range(self.cols)] for _ in range(self.rows)]

    def set(self, row: int, col: int, value: int | float):
        '''Устанавливает значение value матрицы для строки row и колоники col'''
        self._data[row][col] = value

    def get(self, row: int, col: int) -> int | float:
        '''Получает значение матрицы для строки row и колоники col'''
        return self._data[row][col]

    def __eq__(self, __value: object) -> bool:
        if self is __value:
            return True
        if type(__value) != type(self):
            return False

        if self.rows != __value.rows or self.cols != __value.cols:
            return False

        return self._data == __value._data

    def __validate(self, other: Self, add: bool = True) -> None:
        '''Проверяет, что с other можно осуществлять арифметические операции для матриц'''
        if type(other) != type(self):
            raise TypeError("Несовместимый тип")

        if add:
            if self.rows != other.rows or self.cols != other.cols:
                raise TypeError(
                    "Количество строк и столбцов у матриц должны совпадать")
        else:
            if self.cols != other.rows:
                raise TypeError(
                    "Количество столбцов левой матрицы должно быть равно количеству строк правой матрицы")

    def __add__(self, other: Self) -> Self:
        self.__validate(other)

        res = Matrix(self.rows, self.cols)
        res._data = [[self._data[i][j] + other._data[i][j]
                     for j in range(self.cols)] for i in range(self.rows)]
        res._data_type = self._data_type
        return res

    def __iadd__(self, other: Self) -> Self:
        self.__validate(other)
        self._data = [[self._data[i][j] + other._data[i][j]
                       for j in range(self.cols)] for i in range(self.rows)]
        return self

    def __sub__(self, other: Self) -> Self:
        self.__validate(other)

        res = Matrix(self.rows, self.cols)
        res._data = [[self._data[i][j] - other._data[i][j]
                     for j in range(self.cols)] for i in range(self.rows)]
        res._data_type = self._data_type
        return res

    def __isub__(self, other: Self) -> Self:
        self.__validate(other)
        self._data = [[self._data[i][j] - other._data[i][j]
                       for j in range(self.cols)] for i in range(self.rows)]
        return self

    def __mul__(self, other: Self) -> Self:
        '''Операция матричного умножения'''
        self.__validate(other, add=False)

        res = Matrix(self.rows, other.cols)
        res._data = [[0 for _ in range(other.cols)] for _ in range(self.rows)]

        for i in range(self.rows):
            for j in range(other.cols):
                res._data[i][j] = 0
                for k in range(self.cols):
                    res._data[i][j] += self._data[i][k] * other._data[k][j]
        res._data_type = self._data_type
        return res


def test_matrix():
    print(' Test '.center(70, '='))
    m = Matrix(3, 4, 1)
    m2 = Matrix(3, 4, 1)
    print(f'm == m2: {m == m2}')
    m.set(1, 2, 5)
    m2.set(1, 2, 3)
    print(f'm == m2: {m == m2}')
    print(m.get(1, 2))
    m.fill_random_int()
    m2.fill_random_int()
    print(f'm = \n{m}')
    print(f'm2 = \n{m2}')
    sum_m = m + m2
    print(f'm + m2 = \n{sum_m}')
    m -= m2
    print(f'm -= m2 \n{m}')

    ml = Matrix(2, 3, [[1, 3, 0], [-1, 1, 2]])
    print(f'ml = \n{ml}')
    mr = Matrix(3, 1, [[-1], [1], [2]])
    print(f'mr = \n{mr}')
    m_mul = ml * mr
    print(f'ml * mr = \n{m_mul}')


if __name__ == '__main__':
    test_matrix()
