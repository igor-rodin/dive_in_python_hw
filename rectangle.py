from typing import Self


class IsPositive:
    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError(
                "Стороны приямоугольника должны быть положительными числами"
            )
        setattr(instance, self.param_name, value)


class Rectangle:
    """Описывает прямоугольник со сторонами width и height"""

    width = IsPositive()
    height = IsPositive()

    def __init__(self, width: int | float, height: int | float) -> None:
        self.width = width
        self.height = height

    def perimetr(self) -> int | float:
        """Возвращает периметр прямоугольника"""

        return 2 * (self.width + self.height)

    def area(self) -> int | float:
        """Возвращает площадь прямоугольника"""

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
        return f"Прямоугольник: {self.width} x {self.height}"

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f"{class_name}({self.width},{self.height})"
