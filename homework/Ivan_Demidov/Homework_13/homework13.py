import datetime
from pathlib import Path

file_path = Path("homework/eugene_okulik/hw_13/data.txt")

with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        parts = line.split(" - ", 1)
        if len(parts) < 2:
            continue

        header = parts[0]
        task = parts[1]

        dot_index = header.find(".")
        num = int(header[:dot_index])
        date_str = header[dot_index + 1:].strip()

        dt = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")

        print(f"Задание {num}: {task}")

        if num == 1:
            new_date = dt + datetime.timedelta(weeks=1)
            print(new_date)

        elif num == 2:
            print(dt.strftime("%A"))

        elif num == 3:
            now = datetime.datetime.now()
            delta = now - dt
            print(f"{delta.days} дней назад")

        print("-" * 20)
