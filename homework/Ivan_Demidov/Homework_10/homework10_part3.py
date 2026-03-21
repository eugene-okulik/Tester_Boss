# 1. Декоратор
def operation_selector(func):
    def wrapper(first, second, operation):
        # Проверяем условия в ПРАВИЛЬНОМ порядке
        if first < 0 or second < 0:
            operation = "*"
        elif first == second:
            operation = "+"
        elif first > second:
            operation = "-"
        else:  # second > first
            operation = "/"

        return func(first, second, operation)

    return wrapper


# 2. Функция калькулятора
@operation_selector
def calc(first, second, operation):
    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    elif operation == "*":
        return first * second
    elif operation == "/":
        return first / second


# 3. Ввод от пользователя
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

# 4. Вызов функции (операция не важна, декоратор её изменит)
result = calc(num1, num2, "?")
print(f"Результат: {result}")
