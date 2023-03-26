import random

'''
Задача о 8 ферзях
'''

__all__ = ['check_bit_queen', 'gen_queens_position']


def gen_queens_position(queen_count: int) -> tuple[(int, int)]:
    '''
    Генерирует случаюную расстановку queen_count ферзей на доске
    '''
    pos = []
    prev_row = None
    for _ in range(queen_count):
        cur_row = random.randrange(1, queen_count + 1)
        while cur_row == prev_row:
            cur_row = random.randrange(1, queen_count + 1)
        prev_row = cur_row
        cur_col = random.randrange(1, queen_count + 1)
        pos.append((cur_row, cur_col))

    return tuple(pos)


def check_bit_queen(positions: tuple((int, int))) -> bool:
    '''
    Проверяет, бьют ли ферзи в расстановке position друг друга.
    Возвращает True, если не бьют и  False - если бьюь
    '''

    def check_line(line: dict[int, int]) -> bool:
        '''
        Возвращает False если количество ферзей в ряду больше 1.
        Значит они бьют друг друга
        '''
        for queen_count in line.values():
            if queen_count > 1:
                return False
        return True

    row_dict = dict()
    col_dict = dict()
    main_diag_dict = dict()
    sec_diag_dict = dict()

    for row, col in positions:
        row_dict[row] = row_dict.setdefault(row, 0) + 1
        col_dict[col] = col_dict.setdefault(col, 0) + 1
        main_diag_dict[row - col] = main_diag_dict.setdefault(row - col, 0) + 1
        sec_diag_dict[row + col] = sec_diag_dict.setdefault(row + col, 0) + 1

    return check_line(row_dict) and check_line(col_dict) \
        and check_line(main_diag_dict) and check_line(sec_diag_dict)


if __name__ == '__main__':
    position = ((1, 2), (2, 3), (3, 4))
    print(check_bit_queen(position))
