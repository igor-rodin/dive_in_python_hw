BASE = 16

num_to_alpha = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

print("Перевод числа в шестнадцатеричное представление")
num: int = int(input("Введите число: "))
num_copy = num

result: str = ""
while num > 0:
    rem = num % BASE
    result = (str(rem) if rem < 10 else num_to_alpha[rem]) + result
    num //= BASE

print(f"Шестнадцатеричное представление числа {num_copy}: Ox{result}")
