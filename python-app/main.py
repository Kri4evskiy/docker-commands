import calendar


print(f"Добро пожаловать в супер календарь")

year = int(input("Введите год: "))
month = int(input("Введите номер месяца: "))

print(calendar.month(year, month))

print(f"Спасибо за использование программы")
