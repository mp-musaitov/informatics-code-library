# Последовательности

# Базовые шаблоны обработки последовательности чисел.

# 1. Сумма и количество
numbers = [5, 12, 7, 20, 3]

total = 0
count = 0

for number in numbers:
    total += number
    count += 1

print(total, count)

# 2. Количество элементов по условию
count = 0
for number in numbers:
    if number % 2 == 0:
        count += 1
print(count)

# 3. Сумма элементов по условию
total = 0
for number in numbers:
    if number > 10:
        total += number
print(total)

# 4. Максимум и минимум без max()/min()
maximum = None
minimum = None

for number in numbers:
    if maximum is None or number > maximum:
        maximum = number
    if minimum is None or number < minimum:
        minimum = number

print(maximum, minimum)

# 5. Обработка до стоп-значения
# Например, вводим числа до нуля.
count = 0

while True:
    number = int(input())

    if number == 0:
        break

    count += 1

print(count)

# 6. Считать последовательность из файла
with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        number = int(line)
        # обработка number

# 7. Считать все числа в список
with open('input.txt', 'r', encoding='utf-8') as file:
    numbers = [int(line) for line in file]

# 8. Первая строка — количество элементов
with open('input.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())

    numbers = []
    for _ in range(n):
        numbers.append(int(file.readline()))

# Частые ошибки:
# 1. Перепутать количество всех элементов и количество подходящих.
# 2. Забыть break при обработке до стоп-значения.
# 3. Включить стоп-значение в расчёты, хотя оно не является частью последовательности.
# 4. Использовать максимум = 0 при возможных отрицательных числах.

# Универсальный шаблон:
# count = 0
# total = 0
# maximum = None
#
# for number in numbers:
#     if условие:
#         count += 1
#         total += number
#         if maximum is None or number > maximum:
#             maximum = number
