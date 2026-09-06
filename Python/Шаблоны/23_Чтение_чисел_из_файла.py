# Чтение чисел из файла

# В задачах ЕГЭ данные часто хранятся в текстовом файле.
# Ниже — самые частые форматы входных данных.

# ------------------------------------------------------------
# 1. В каждой строке находится одно число

with open('input.txt', 'r', encoding='utf-8') as file:
    numbers = [int(line) for line in file]

print(numbers)

# ------------------------------------------------------------
# 2. Читать файл построчно, не сохраняя весь список

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        number = int(line)
        print(number)

# Этот вариант удобен для больших файлов.

# ------------------------------------------------------------
# 3. Все числа записаны в одной строке через пробел

with open('input.txt', 'r', encoding='utf-8') as file:
    numbers = list(map(int, file.readline().split()))

print(numbers)

# ------------------------------------------------------------
# 4. Числа могут находиться в нескольких строках

with open('input.txt', 'r', encoding='utf-8') as file:
    numbers = []

    for line in file:
        numbers.extend(map(int, line.split()))

print(numbers)

# ------------------------------------------------------------
# 5. Короткий вариант: прочитать весь файл и разбить по пробельным символам

with open('input.txt', 'r', encoding='utf-8') as file:
    numbers = list(map(int, file.read().split()))

print(numbers)

# split() без аргументов работает и с пробелами, и с переводами строк.

# ------------------------------------------------------------
# 6. Первая строка — количество элементов
# Пример файла:
# 5
# 10
# 20
# 30
# 40
# 50

with open('input.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    numbers = [int(file.readline()) for _ in range(n)]

print(n)
print(numbers)

# ------------------------------------------------------------
# 7. Первая строка — количество, далее пары чисел
# Пример:
# 3
# 10 20
# 30 40
# 50 60

with open('input.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())

    pairs = []
    for _ in range(n):
        a, b = map(int, file.readline().split())
        pairs.append((a, b))

print(pairs)

# ------------------------------------------------------------
# 8. Таблица: несколько чисел в каждой строке

rows = []

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        row = list(map(int, line.split()))
        rows.append(row)

print(rows)

# ------------------------------------------------------------
# 9. Пропустить первую строку
# Иногда первая строка содержит служебное значение, которое дальше не нужно.

with open('input.txt', 'r', encoding='utf-8') as file:
    file.readline()
    numbers = [int(line) for line in file]

print(numbers)

# ------------------------------------------------------------
# 10. Удаление перевода строки

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        print(line)

# strip() особенно нужен при работе со строковыми данными.

# ------------------------------------------------------------
# Частые ошибки

# 1. Неправильно указать имя или путь к файлу -> FileNotFoundError.
# 2. Забыть int(), если нужны числа.
# 3. Забыть split(), если в строке несколько чисел.
# 4. Использовать readlines() и забыть про символы \n.
# 5. Считать первую строку обычным элементом, хотя там хранится количество.
# 6. Загружать огромный файл в список, хотя можно обработать его построчно.

# ------------------------------------------------------------
# Универсальные шаблоны

# Одно число в строке:
# with open('input.txt') as file:
#     numbers = [int(line) for line in file]

# Все числа независимо от строк:
# with open('input.txt') as file:
#     numbers = list(map(int, file.read().split()))

# Обработка построчно:
# with open('input.txt') as file:
#     for line in file:
#         number = int(line)
#         # обработка number
