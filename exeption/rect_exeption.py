__all__ = ["NegativeRectSizeExeption"]


class NegativeRectSizeExeption(Exception):
    """Исключение выбрасывается при попвтке создать прямоугольник с отрицательными размерами"""

    def __init__(self, size: int) -> None:
        self._size = size

    def __str__(self) -> str:
        return f"Нельзя создать прямоугольник с отрицательной сотороной {self._size}"
