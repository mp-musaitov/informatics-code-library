# Счётчик и экстремум из файла

# Один из самых частых шаблонов в задачах ЕГЭ:
# определить количество подходящих элементов и максимальный/минимальный среди них.

# ------------------------------------------------------------
# 1. Количество подходящих чисел

count = 0

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        number = int(line)

        if number % 2 == 0:
            count += 1

print(count)

# ------------------------------------------------------------
# 2. Максимум среди подходящих

maximum = None

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        number = int(line)

        if number % 2 == 0:
            if maximum is None or number > maximum:
                maximum = number

print(maximum)

# ------------------------------------------------------------
# 3. Количество и максимум одновременно

count = 0
maximum = None

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        number = int(line)

        if number % 5 == 0:
            count += 1

            if maximum is None or number > maximum:
                maximum = number

print(count, maximum)

# ------------------------------------------------------------
# 4. Количество и минимум

count = 0
minimum = None

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        number = int(line)

        if number < 0:
            count += 1

            if minimum is None or number < minimum:
                minimum = number

print(count, minimum)

# ------------------------------------------------------------
# 5. Сложное условие

count = 0
maximum = None

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        number = int(line)

        # пример: положительное число, кратное 7 и не кратное 5
        if number > 0 and number % 7 == 0 and number % 5 != 0:
            count += 1

            if maximum is None or number > maximum:
                maximum = number

print(count, maximum)

# ------------------------------------------------------------
# 6. Если первая строка содержит количество элементов

count = 0
maximum = None

with open('input.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())

    for _ in range(n):
        number = int(file.readline())

        if number % 3 == 0:
            count += 1

            if maximum is None or number > maximum:
                maximum = number

print(count, maximum)

# ------------------------------------------------------------
# 7. Одновременно сумма, количество и максимум

count = 0
total = 0
maximum = None

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        number = int(line)

        if number % 10 == 3:
            count += 1
            total += number

            if maximum is None or number > maximum:
                maximum = number

print(count, total, maximum)

# ------------------------------------------------------------
# 8. Среднее подходящих элементов

count = 0
total = 0

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        number = int(line)

        if number > 100:
            count += 1
            total += number

if count > 0:
    average = total / count
    print(average)
else:
    print('Подходящих элементов нет')

# ------------------------------------------------------------
# 9. Почему maximum = 0 может быть ошибкой

# Если все подходящие числа отрицательные,
# максимум среди них тоже будет отрицательным.
# Поэтому универсальнее начинать с None.

maximum = None

# ------------------------------------------------------------
# 10. Короткий вариант через список

with open('input.txt', 'r', encoding='utf-8') as file:
    suitable = [int(line) for line in file if int(line) % 2 == 0]

if suitable:
    print(len(suitable), max(suitable))

# Такой вариант короче, но для очень больших файлов
# построчная обработка экономнее по памяти.

# ------------------------------------------------------------
# Частые ошибки

# 1. Считать максимум среди всех чисел, а не только среди подходящих.
# 2. Увеличивать count вне условия.
# 3. Использовать maximum = 0 при возможных отрицательных значениях.
# 4. Не обработать случай, когда подходящих элементов нет.
# 5. Для среднего делить сумму на общее количество элементов,
#    а не на количество подходящих.
# 6. Несколько раз открывать файл там, где всё можно посчитать за один проход.

# ------------------------------------------------------------
# Универсальный шаблон

# count = 0
# maximum = None
#
# with open('input.txt') as file:
#     for line in file:
#         number = int(line)
#
#         if условие:
#             count += 1
#
#             if maximum is None or number > maximum:
#                 maximum = number
#
# print(count, maximum)
