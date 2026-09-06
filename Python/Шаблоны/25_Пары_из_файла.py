# Пары из файла

# Частый тип задач: в каждой строке файла записана пара чисел.
# Нужно проверить условие для пары, посчитать подходящие строки,
# найти максимум/минимум суммы, произведения и т.д.

# ------------------------------------------------------------
# 1. Прочитать пары из файла
# Пример строки: 10 25

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        a, b = map(int, line.split())
        print(a, b)

# ------------------------------------------------------------
# 2. Посчитать пары, удовлетворяющие условию

count = 0

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        a, b = map(int, line.split())

        if a % 2 == 0 and b % 2 == 0:
            count += 1

print(count)

# ------------------------------------------------------------
# 3. Условие: хотя бы одно число подходит

count = 0

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        a, b = map(int, line.split())

        if a % 5 == 0 or b % 5 == 0:
            count += 1

print(count)

# ------------------------------------------------------------
# 4. Условие: ровно одно число подходит

count = 0

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        a, b = map(int, line.split())

        condition_a = a % 3 == 0
        condition_b = b % 3 == 0

        if condition_a != condition_b:
            count += 1

print(count)

# condition_a != condition_b означает:
# одно условие True, другое False.

# ------------------------------------------------------------
# 5. Максимальная сумма среди подходящих пар

maximum_sum = None

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        a, b = map(int, line.split())

        if a > 0 and b > 0:
            pair_sum = a + b

            if maximum_sum is None or pair_sum > maximum_sum:
                maximum_sum = pair_sum

print(maximum_sum)

# ------------------------------------------------------------
# 6. Минимальное произведение среди подходящих пар

minimum_product = None

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        a, b = map(int, line.split())

        if a % 2 != 0 and b % 2 != 0:
            product = a * b

            if minimum_product is None or product < minimum_product:
                minimum_product = product

print(minimum_product)

# ------------------------------------------------------------
# 7. Первая строка — количество пар

with open('input.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())

    for _ in range(n):
        a, b = map(int, file.readline().split())
        print(a, b)

# ------------------------------------------------------------
# 8. Сохранить все пары в список

pairs = []

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        a, b = map(int, line.split())
        pairs.append((a, b))

print(pairs)

# ------------------------------------------------------------
# 9. Работа с тройками и большим количеством чисел

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        a, b, c = map(int, line.split())
        print(a, b, c)

# Принцип тот же: число переменных должно соответствовать числу значений в строке.

# ------------------------------------------------------------
# 10. Сравнение элементов пары

count = 0

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        a, b = map(int, line.split())

        if a < b:
            count += 1

print(count)

# ------------------------------------------------------------
# Частые ошибки

# 1. Забыть split() перед map(int, ...).
# 2. Использовать and там, где по условию нужно or, и наоборот.
# 3. Не различать «хотя бы одно» и «ровно одно».
# 4. Искать максимум суммы, сравнивая только a или только b.
# 5. Начинать максимум с 0 при возможных отрицательных значениях.
# 6. Пытаться распаковать строку из трёх чисел в две переменные.

# ------------------------------------------------------------
# Универсальный шаблон

# count = 0
# maximum = None
#
# with open('input.txt') as file:
#     for line in file:
#         a, b = map(int, line.split())
#
#         if условие_для_пары:
#             count += 1
#             value = ...  # например, a + b
#
#             if maximum is None or value > maximum:
#                 maximum = value
#
# print(count, maximum)
