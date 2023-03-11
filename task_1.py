print("Введите три стороны треугольника")
a = int(input("Сторона A: "))
b = int(input("Сторона B: "))
c = int(input("Сторона C: "))

message = None

if a + b <= c or a + c <= b or a + c <= b:
    message = "Треугольник с такими сторонами существовать не может"
elif a == b == c:
    message = "Треугольник равносторонний"
elif a == b or a == c or b == c:
    message = "Треугольник равнобедренный"
else:
    message = "Треугольник разносторонний"

print(message)
