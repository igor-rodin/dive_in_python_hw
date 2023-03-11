import math

LOW_LIMIT = 0
UPPER_LIMIT = 100000

while (True):
    N = int(input("Введите число: "))
    if N < LOW_LIMIT or N > UPPER_LIMIT:
        print(f"Число должно быть в диапазоне {LOW_LIMIT} - {UPPER_LIMIT}")
    elif N == 0:
        print(f"Число {N} не является ни составным, ни простым")
        break
    else:
        isPrime = True
        for i in range(2, round(math.sqrt(N)) + 1):
            if N % i == 0:
                isPrime = False
                break
        print(f"Число {N} простое" if isPrime else f"Число {N} составное")
        break
