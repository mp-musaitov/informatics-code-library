# Пары элементов

# Здесь рассматриваются ВСЕ пары элементов последовательности,
# а не только соседние.

numbers = [3, 8, 12, 5]

# 1. Перебрать все пары
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        print(numbers[i], numbers[j])

# Условие j > i гарантирует, что:
# - элемент не образует пару сам с собой;
# - каждая пара рассматривается один раз.

# 2. Посчитать пары с суммой больше 15
count = 0

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] > 15:
            count += 1

print(count)

# 3. Максимальная сумма пары по условию
maximum = None

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        a = numbers[i]
        b = numbers[j]

        if a % 2 == 0 or b % 2 == 0:
            pair_sum = a + b

            if maximum is None or pair_sum > maximum:
                maximum = pair_sum

print(maximum)

# 4. Минимальное произведение подходящей пары
minimum = None

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        a = numbers[i]
        b = numbers[j]

        if a > 0 and b > 0:
            product = a * b

            if minimum is None or product < minimum:
                minimum = product

print(minimum)

# 5. Пара элементов должна быть различной по значению
count = 0

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] != numbers[j]:
            count += 1

print(count)

# 6. Найти сами элементы лучшей пары
best_pair = None
maximum = None

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        pair_sum = numbers[i] + numbers[j]

        if maximum is None or pair_sum > maximum:
            maximum = pair_sum
            best_pair = (numbers[i], numbers[j])

print(best_pair, maximum)

# 7. Пары символов строки
text = 'ABCD'

for i in range(len(text)):
    for j in range(i + 1, len(text)):
        print(text[i], text[j])

# 8. Количество всех пар без перебора
# Если элементов n, количество пар равно n * (n - 1) // 2.

n = 10
pairs_count = n * (n - 1) // 2
print(pairs_count)  # 45

# Частые ошибки:
# 1. Начинать j с 0 и считать одну пару дважды.
# 2. Писать j = i и получать пары элемента с самим собой.
# 3. Путать все пары с соседними парами.
# 4. Использовать такой полный перебор для очень больших n, не оценив сложность.

# ВАЖНО:
# два вложенных цикла дают примерно O(n^2) операций.
# Для больших наборов данных часто нужен более умный способ.

# Универсальный шаблон:
# count = 0
# maximum = None
#
# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         a = numbers[i]
#         b = numbers[j]
#
#         if условие:
#             count += 1
#             value = выражение_для_пары
#             if maximum is None or value > maximum:
#                 maximum = value
