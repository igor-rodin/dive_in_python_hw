# Задание №1
# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и их факториалов.


# Задание №2
# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.


import json
from typing import Self


class Factorial:
    res = {}
    JSON_FILE = 'factorial.json'

    def __init__(self, k: int) -> None:
        self.k = k

    def __call__(self, num) -> int:
        if num not in self.res:
            fac = 1
            for i in range(1, num + 1):
                fac *= i
            if len(self.res) >= self.k:
                self.res.pop(list(self.res.keys())[0])
            self.res[num] = fac
            return fac
        return self.res[num]

    def __str__(self) -> str:
        return '\n'.join([f'{num}! = {res}'for num, res in self.res.items()])

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(self.JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.res, f, ensure_ascii=False, indent=2)

# Задание №3
# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step = 1.
# Если передан один параметр, также считаем start = 1


class FactorialRange:

    def __init__(self, *args) -> None:
        match args:
            case (stop, ):
                self.start, self.stop, self.step = 1, stop, 1
            case (start, stop):
                self.start, self.stop, self.step = start, stop, 1
            case (start, stop, step):
                self.start, self.stop, self.step = start, stop, step

    @staticmethod
    def _fac(n: int) -> int:
        fac = 1
        for i in range(1, n + 1):
            fac *= i
        return fac

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.stop:
            res = self._fac(self.start)
            self.start += self.step
            return res

        raise StopIteration


# Задание №4
# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений (отрицательных).
# Используйте декораторы свойств.

# Задание №5
# Доработаем прямоугольник и добавим экономию памяти для хранения свойств экземпляра без словаря __dict__.

# Задание №6
# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.

class IsPositive:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(
                'Стороны приямоугольника должны быть положительными числами')
        setattr(instance, self.param_name, value)


class Rectangle:
    '''Описывает прямоугольник со сторонами width и height '''
    # __slots__ = ('_width', '_height')
    width = IsPositive()
    height = IsPositive()

    def __init__(self, width: int | float, height: int | float) -> None:
        self.width = width
        self.height = height

    # @property
    # def width(self):
    #     return self._width

    # @property
    # def height(self):
    #     return self._height

    # @width.setter
    # def width(self, value: int | float) -> None:
    #     if value < 0:
    #         raise ValueError(
    #             'Стороны приямоугольника должны быть положительными числами')
    #     self._width = value

    # @height.setter
    # def height(self, value: int | float) -> None:
    #     if value < 0:
    #         raise ValueError(
    #             'Стороны приямоугольника должны быть положительными числами')
    #     self._height = value

    def perimetr(self) -> int | float:
        '''Возвращает периметр прямоугольника'''

        return 2 * (self.width + self.height)

    def area(self) -> int | float:
        '''Возвращает площадь прямоугольника'''

        return self.width * self.height

    def __add__(self, other) -> Self:
        new_perimetr = self.perimetr() + other.perimetr()
        return Rectangle(new_perimetr / 4, new_perimetr / 4)

    def __sub__(self, other) -> Self:
        if other.perimetr() > self.perimetr():
            return None
        new_perimetr = self.perimetr() - other.perimetr()
        return Rectangle(new_perimetr / 4, new_perimetr / 4)

    def __eq__(self, __value: object) -> bool:
        if self is __value:
            return True
        return self.area() == __value.area()

    def __lt__(self, __value: object) -> bool:
        return self.area() < __value.area()

    def __le__(self, __value: object) -> bool:
        return self.area() < __value.area() or self == __value

    def __str__(self) -> str:
        return f'Прямоугольник: {self.width} x {self.height}'

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name}({self.width},{self.height})'


if __name__ == '__main__':
    # with Factorial(3) as f:
    #     print(f(2))
    #     print(f(5))
    #     print(f(10))
    #     print(f(12))

    # for n in FactorialRange(2, 10):
    #     print(n)

    p1 = Rectangle(20, 19)
    print(p1.height)
    p2 = Rectangle(2, 10)
    # print(Rectangle.__dict__)
    # print(p.__dict__)
    p2.height = -1
