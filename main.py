import lesson_6.date as dt
import lesson_6.chess as chess

# Task 1

date = "31.05.2023"
print(f"Дата {date} существует.") if dt.check_date(
    date) else print(f"Дата {date} не существует.")

# Task 2, 3
QUEENS_COUNT = 8
GOOD_POSITION_COUNT = 4

good_pos = set()
for i in range(GOOD_POSITION_COUNT):
    pos = chess.gen_queens_position(QUEENS_COUNT)
    while pos in good_pos or not chess.check_bit_queen(pos):
        pos = chess.gen_queens_position(QUEENS_COUNT)
    good_pos.add(pos)
    print(f"Расстановка {i + 1}: {sorted(pos, key= lambda item: item[0])}")
