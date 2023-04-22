__all__ = [
    "NotValidDataDimensionExeption",
    "ArithmeticMatrixExeptions",
    "AddOperMatrixExeption",
    "MulOperMatrixExeption",
]


class BaseMatrixExeption(Exception):
    """Базовое исключение при работе с Matrix"""

    def __init__(self, rows: int, cols: int) -> None:
        self._rows = rows
        self._cols = cols


class NotValidDataDimensionExeption(BaseMatrixExeption):
    """Исключение выбрасывается, когда размер матрицы не совпадает с размером входных данных"""

    def __init__(self, rows: int, cols: int, data_rows: int, data_cols: int) -> None:
        super().__init__(rows, cols)
        self._data_rows = data_rows
        self._data_cols = data_cols

    def __str__(self) -> str:
        return f"Размерность массива ({self._rows} x {self._cols}) не совпадает с размером входных данных ({self._data_rows} x {self._data_cols})"


class ArithmeticMatrixExeptions(BaseMatrixExeption):
    """Базовое исключение для арифметических лперациях с матрицами"""

    def __init__(self, rows: int, cols: int, right_rows: int, right_cols: int) -> None:
        super().__init__(rows, cols)
        self._right_rows = right_rows
        self._right_cols = right_cols


class AddOperMatrixExeption(ArithmeticMatrixExeptions):
    """Исключение выбрасывается при операции сложения матриц, когда размеры левой и правой матриц не совпадают"""

    def __str__(self) -> str:
        return f"Размерность левой матрицы ({self._rows} x {self._cols}) не совпадает с размерностью правой матрицы ({self._right_rows} x {self._right_cols})"


class MulOperMatrixExeption(ArithmeticMatrixExeptions):
    """Исключение выбрасывается при операции умножения матриц, когда размеры левой и правой матриц не согласованы"""

    def __str__(self) -> str:
        return f"Количество столбцов левой матрицы ({self._cols}) не равно количеству строк правой матрицы ({self._right_rows})"
