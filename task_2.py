import math


def normalize(nominator: int, denominator: int) -> tuple:
    gcd_ = math.gcd(nominator, denominator)
    nominator //= gcd_
    denominator //= gcd_
    return (nominator, denominator)


fract_1: str = input("Введите первую дробь ('a/b'): ")
fract_2: str = input("Введите вторую дробь ('a/b'): ")

nom_denom_1 = fract_1.split('/')
nom_denom_2 = fract_2.split('/')

# Находим сумму дробей

nominator_sum = int(nom_denom_1[0]) * int(nom_denom_2[1]) + \
    int(nom_denom_2[0]) * int(nom_denom_1[1])
denominator_sum = int(nom_denom_1[1]) * int(nom_denom_2[1])

if nominator_sum % denominator_sum == 0:
    sum_res = str(nominator_sum // denominator_sum)
else:
    nominator_sum, denominator_sum = normalize(nominator_sum, denominator_sum)
    sum_res = f"{nominator_sum}/{denominator_sum}"

sum_fr = f"({fract_1}) + ({fract_2}) = {sum_res}"


# Находим произведение дробей

nominator_prod = int(nom_denom_1[0]) * int(nom_denom_2[0])
denominator_prod = int(nom_denom_1[1]) * int(nom_denom_2[1])

if nominator_prod % denominator_prod == 0:
    prod_res = str(nominator_prod // denominator_prod)
else:
    nominator_prod, denominator_prod = normalize(
        nominator_prod, denominator_prod)
    prod_res = f"{nominator_prod}/{denominator_prod}"

prod_fr = f"({fract_1}) * ({fract_2}) = {prod_res}"


print(sum_fr)
print(prod_fr)
