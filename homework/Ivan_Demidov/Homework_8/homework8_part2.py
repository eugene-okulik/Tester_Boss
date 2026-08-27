import sys

sys.set_int_max_str_digits(100000)


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def get_nth_fib(n):
    gen = fibonacci()
    for _ in range(n):
        result = next(gen)
    return result


# 3. Тестируем
print(get_nth_fib(5))  # 5-е число
print(get_nth_fib(200))  # 200-е число
print(get_nth_fib(1000))  # 1000-е число


result = get_nth_fib(100000)
print(f"100000-е число имеет {len(str(result))} цифр")
print(f"Первые 20 цифр: {str(result)[:20]}...")
