# Соседние элементы

# Соседняя пара — элементы с индексами i и i + 1.

numbers = [10, 15, 8, 21, 4]

# 1. Перебрать все соседние пары
for i in range(len(numbers) - 1):
    a = numbers[i]
    b = numbers[i + 1]
    print(a, b)

# 2. Посчитать пары, сумма которых больше 20
count = 0
for i in range(len(numbers) - 1):
    a = numbers[i]
    b = numbers[i + 1]

    if a + b > 20:
        count += 1

print(count)

# 3. Найти максимальную сумму соседней пары
maximum = None
for i in range(len(numbers) - 1):
    pair_sum = numbers[i] + numbers[i + 1]

    if maximum is None or pair_sum > maximum:
        maximum = pair_sum

print(maximum)

# 4. Пара должна удовлетворять нескольким условиям
count = 0
for i in range(len(numbers) - 1):
    a = numbers[i]
    b = numbers[i + 1]

    if (a % 2 == 0 or b % 2 == 0) and a + b > 20:
        count += 1

print(count)

# 5. Найти максимальное произведение подходящей пары
maximum = None
for i in range(len(numbers) - 1):
    a = numbers[i]
    b = numbers[i + 1]

    if a % 2 == 0 and b % 2 == 0:
        product = a * b

        if maximum is None or product > maximum:
            maximum = product

print(maximum)

# 6. Пары в строке
text = 'ABACABA'
for i in range(len(text) - 1):
    print(text[i:i + 2])

# Частые ошибки:
# 1. Писать range(len(numbers)) и получить выход за границы на i + 1.
# 2. Путать соседние пары со всеми возможными парами.
# 3. Сравнивать сами элементы, когда по условию нужна сумма/произведение пары.
# 4. Не обработать случай, когда подходящих пар нет.

# Универсальный шаблон:
# count = 0
# maximum = None
#
# for i in range(len(numbers) - 1):
#     a = numbers[i]
#     b = numbers[i + 1]
#
#     if условие:
#         count += 1
#         value = выражение_для_пары
#         if maximum is None or value > maximum:
#             maximum = value
