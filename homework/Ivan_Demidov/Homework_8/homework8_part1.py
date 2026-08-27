import random

# 1. Спросить зарплату
salary = int(input("Введите зарплату: "))

# 2. Случайный bonus
bonus = random.choice([True, False])

# 3. Если bonus True — добавить случайную сумму
if bonus:
    salary = salary + random.randint(1, 5000)

# 4. Вывести с $
print(f"${salary}")
