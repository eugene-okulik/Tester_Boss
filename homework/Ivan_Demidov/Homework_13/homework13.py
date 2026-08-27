import datetime
from pathlib import Path

# Определяем путь к data.txt относительно расположения этого файла
script_dir = Path(__file__).parent
repo_root = script_dir.parent.parent.parent
data_file = repo_root / "homework" / "eugene_okulik" / "hw_13" / "data.txt"

with open(data_file, encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        parts = line.split(" - ", 1)
        if len(parts) < 2:
            continue

        header, task = parts
        dot_index = header.find(".")
        num = int(header[:dot_index])
        date_str = header[dot_index + 1:].strip()

        dt = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")

        if num == 1:
            result = dt + datetime.timedelta(weeks=1)
            print(result)
        elif num == 2:
            result = dt.strftime("%A")
            print(result)
        elif num == 3:
            now = datetime.datetime.now()
            delta = now - dt
            print(delta.days)
