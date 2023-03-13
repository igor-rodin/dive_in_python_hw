import math

fract_1: str = input("Введите первую дробь ('a/b'): ")
fract_2: str = input("Введите вторую дробь ('a/b'): ")

parts_1 = fract_1.split('/')
parts_2 = fract_2.split('/')

# Находим сумму дробей

numenator_sum = int(parts_1[0]) * int(parts_2[1]) + \
    int(parts_2[0]) * int(parts_1[1])
denomenator_sum = int(parts_1[1]) * int(parts_2[1])

if numenator_sum % denomenator_sum == 0:
    sum_res = str(numenator_sum // denomenator_sum)
else:
    gcd_ = math.gcd(numenator_sum, denomenator_sum)
    numenator_sum //= gcd_
    denomenator_sum //= gcd_
    sum_res = f"{numenator_sum}/{denomenator_sum}"

sum_fr = f"{fract_1} + {fract_2} = {sum_res}"


# Находим произведение дробей

numenator_prod = int(parts_1[0]) * int(parts_2[0])
denomenator_prod = int(parts_1[1]) * int(parts_2[1])

if numenator_prod % denomenator_prod == 0:
    prod_res = str(numenator_prod // denomenator_prod)
else:
    gcd_ = math.gcd(numenator_prod, denomenator_prod)
    numenator_prod //= gcd_
    denomenator_prod //= gcd_
    prod_res = f"{numenator_prod}/{denomenator_prod}"

prod_fr = f"{fract_1} * {fract_2} = {prod_res}"


print(sum_fr)
print(prod_fr)
