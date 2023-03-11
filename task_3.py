from random import randint

LOW_LIMIT = 0
UPPER_LIMIT = 1000
TRIES_NUMBER = 10

hidden_number = randint(LOW_LIMIT, UPPER_LIMIT)

print(
    f"Угадайте загаданное число в диапазоне от {LOW_LIMIT} до {UPPER_LIMIT} за {TRIES_NUMBER} попыток")

tries = 1
while tries <= TRIES_NUMBER:
    N = None
    while (True):
        N = int(input(f"Попытка {tries} - Ваш вариант? "))
        if N < LOW_LIMIT or N > UPPER_LIMIT:
            print(
                f"Число должно быть в диапазоне {LOW_LIMIT} - {UPPER_LIMIT}")
        else:
            break

    if N == hidden_number:
        print(f"Вы угадали с {TRIES_NUMBER} попытки!")
        break
    else:
        print(f"{N} больше загаданного числа" if N >
              hidden_number else f"{N} меньше загаданного числа")
        tries += 1
else:
    print("Попытки закончились. Не повезло!")
