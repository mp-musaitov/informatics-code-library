# Тройки элементов

# Тройка подряд идущих элементов имеет индексы i, i + 1 и i + 2.

numbers = [5, 12, 7, 20, 3, 8]

# 1. Перебрать все тройки
for i in range(len(numbers) - 2):
    a = numbers[i]
    b = numbers[i + 1]
    c = numbers[i + 2]
    print(a, b, c)

# 2. Посчитать тройки с суммой больше 30
count = 0
for i in range(len(numbers) - 2):
    a = numbers[i]
    b = numbers[i + 1]
    c = numbers[i + 2]

    if a + b + c > 30:
        count += 1

print(count)

# 3. Найти максимальную сумму тройки
maximum = None
for i in range(len(numbers) - 2):
    triple_sum = numbers[i] + numbers[i + 1] + numbers[i + 2]

    if maximum is None or triple_sum > maximum:
        maximum = triple_sum

print(maximum)

# 4. Условие на количество чётных элементов в тройке
count = 0
for i in range(len(numbers) - 2):
    a = numbers[i]
    b = numbers[i + 1]
    c = numbers[i + 2]

    even_count = (a % 2 == 0) + (b % 2 == 0) + (c % 2 == 0)

    if even_count >= 2:
        count += 1

print(count)

# В Python True считается как 1, False — как 0.
# Поэтому сумму логических выражений можно использовать как счётчик.

# 5. Минимальное произведение подходящей тройки
minimum = None
for i in range(len(numbers) - 2):
    a = numbers[i]
    b = numbers[i + 1]
    c = numbers[i + 2]

    if a > 0 and b > 0 and c > 0:
        product = a * b * c

        if minimum is None or product < minimum:
            minimum = product

print(minimum)

# 6. Тройки символов в строке
text = 'ABCDE'
for i in range(len(text) - 2):
    print(text[i:i + 3])

# Частые ошибки:
# 1. Использовать range(len(numbers) - 1) вместо -2.
# 2. Получить выход за границы по индексу i + 2.
# 3. Путать подряд идущую тройку с любыми тремя элементами.
# 4. Не обнулить счётчик для каждой новой тройки.

# Универсальный шаблон:
# count = 0
# maximum = None
#
# for i in range(len(numbers) - 2):
#     a = numbers[i]
#     b = numbers[i + 1]
#     c = numbers[i + 2]
#
#     if условие:
#         count += 1
#         value = выражение_для_тройки
#         if maximum is None or value > maximum:
#             maximum = value
