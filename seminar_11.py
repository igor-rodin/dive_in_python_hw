from typing import Self
from time import time
# Задание №1
# Создайте класс Моя Строка, где: будут доступны все возможности str дополнительно хранятся имя автора строки и время создания
# (time.time)


class MyStr(str):
    '''Дополняет стандартные возможности класса str автором строки и датой создания'''

    def __new__(cls, val, author: str, created_time: float) -> Self:
        obj = super().__new__(cls, val)
        obj.author = author
        obj.created_time = created_time
        return obj

    def __str__(self) -> str:
        return super().__str__()

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name}({super().__str__()}, {self.author}, {self.created_time})'

# Задание №2
# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра


class Archive:
    '''Хранит историю создания экземпляров класса'''
    _instance = None

    def __new__(cls, num: int | float, message: str, *args, **kwargs) -> Self:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.numbers = [num]
            cls._instance.messages = [message]
            return cls._instance
        else:
            obj = super().__new__(cls)
            cls._instance.numbers.append(num)
            obj.numbers = cls._instance.numbers.copy()
            cls._instance.messages.append(message)
            obj.messages = cls._instance.messages.copy()
            return obj

    def __init__(self, num: int | float, message: str) -> None:
        self._num = num
        self._message = message

    def __str__(self) -> str:
        return f'Архив прошлых значений: {self.numbers = } и {self.messages = }'

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name}({self._num}, {self._message})'


# Задание №5
# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

# Задание №6
# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения


class Rectangle:
    '''Описывает прямоугольник со сторонами width и height '''

    def __init__(self, width: int | float, height: int | float) -> None:
        self._width = width
        self._height = height

    def perimetr(self) -> int | float:
        '''Возвращает периметр прямоугольника'''

        return 2 * (self._width + self._height)

    def area(self) -> int | float:
        '''Возвращает площадь прямоугольника'''

        return self._width * self._height

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
        return f'Прямоугольник: {self._width} x {self._height}'

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f'{class_name}({self._width},{self._height})'


def test_mystr():
    print(' Test MyStr '.center(70, '*'))
    my_str = MyStr('String', "I'am", time())
    my_str_2 = MyStr('String_2', "I'am", time())
    print(my_str)
    print(my_str_2)
    print(f'{my_str = }')
    print(f'{my_str_2 = }')


def test_archive():
    print(' Test Archive '.center(70, '*'))
    arch = Archive(1, 'First')
    print(f'{arch.numbers = }, {arch.messages = }')
    arch_2 = Archive(2, 'Second')
    print(f'{arch.numbers = }, {arch.messages = }')
    arch_3 = Archive(3, 'Third')
    print(f'{arch.numbers = }, {arch.messages = }')
    print(f'{arch_2.numbers = }, {arch_2.messages = }')
    print(f'{arch_3.numbers = }, {arch_3.messages = }')

    print(f'{arch_2}')
    print(f'{arch = }')
    print(f'{arch_2 = }')
    print(f'{arch_3 = }')


def test_rectangle():
    print(' Test Rectangle '.center(70, '*'))
    rec = Rectangle(30, 6)
    print(rec)
    rec_2 = Rectangle(3, 6)
    print(rec_2)
    rec_sum = rec + rec_2
    rec_sub = rec - rec_2
    print(f'{rec_sum = }')
    print(f'{rec_sub = }')
    print(rec == rec_2)
    print(rec <= rec_2)
    print(help(rec))


if __name__ == '__main__':
    test_mystr()
    test_archive()
    test_rectangle()
