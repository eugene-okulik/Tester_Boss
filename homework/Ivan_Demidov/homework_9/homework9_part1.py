from datetime import datetime

# Исходная строка даты
date_string = "Jan 15, 2023 - 12:05:33"

# Парсинг строки в объект datetime
date_obj = datetime.strptime(date_string, "%b %d, %Y - %H:%M:%S")

# 1. Полное название месяца
print(date_obj.strftime("%B"))

# 2. Дата в формате "15.01.2023, 12:05"
print(date_obj.strftime("%d.%m.%Y, %H:%M"))
