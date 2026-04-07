import re
import datetime

file_path = r"C:\Users\Mi\Desktop\окулик_курс\Tester_Boss\homework\eugene_okulik\Lesson_13\dates.py"

with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        match = re.match(r"^(\d+)\.\s*(\d{4}-\d{2}-\d{2})\s*-\s*(.+)", line)
        if not match:
            continue

        num = int(match.group(1))
        task_text = match.group(3).strip()

        print(f"Задание {num}: {task_text}")

        if num == 1:
            print(datetime.datetime.now())
        elif num == 2:
            now = datetime.datetime.now()
            print(now.replace(hour=0, minute=0, second=0, microsecond=0))
        elif num == 3:
            now = datetime.datetime.now()
            midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
            print((now - midnight).seconds)
        elif num == 4:
            now = datetime.datetime.now()
            midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
            print(now - midnight)
        elif num == 5:
            print(datetime.datetime.now() + datetime.timedelta(days=10, hours=10))
