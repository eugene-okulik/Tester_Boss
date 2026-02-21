import math

a = float(input("Введите первый катет: "))
b = float(input("Введите второй катет: "))

hypotenuse = math.sqrt(a ** 2 + b ** 2)
area = (a * b) / 2

print(f"Гипотенуза: {hypotenuse:.2f}")
print(f"Площадь: {area:.2f}")

