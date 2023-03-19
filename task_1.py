import random
N: int = 3
M: int = 4

matrix = [[random.randrange(10) for _ in range(1, N + 1)]
          for _ in range(1, M + 1)]


def print_matrix(matrix: list[list[int | float]]) -> None:
    for row in matrix:
        print(f"{row}", end="\t")
        print()


def transpose(matrix: list[list[int | float]]) -> list[list[int | float]]:
    '''
    Возвращает трансонированную матрицу
    '''
    return [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]


print("Исходная матрица")
print_matrix(matrix)
transp_matrix = transpose(matrix)
print("Транспонированная матрица")
print_matrix(transp_matrix)
