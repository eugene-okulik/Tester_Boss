results = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2",
]


def process(text):
    """Извлекает число из строки и прибавляет 10."""
    print(int(text.strip().split()[-1]) + 10)


for result in results:
    process(result)
