# Два максимума

# Задача:
# найти два наибольших элемента последовательности.
# Особенно полезно уметь делать это без сортировки — за один проход.

# ------------------------------------------------------------
# 1. Самый простой вариант через сортировку

numbers = [12, 7, 35, 18, 42, 9, 30]

numbers.sort(reverse=True)

maximum1 = numbers[0]
maximum2 = numbers[1]

print(maximum1, maximum2)  # 42 35

# Способ простой, но сортирует весь список,
# хотя нам нужны только два элемента.


# ------------------------------------------------------------
# 2. Через sorted(), не изменяя исходный список

numbers = [12, 7, 35, 18, 42, 9, 30]

sorted_numbers = sorted(numbers, reverse=True)

print(sorted_numbers[0], sorted_numbers[1])  # 42 35
print(numbers)  # исходный список не изменился


# ------------------------------------------------------------
# 3. Два максимума за один проход

numbers = [12, 7, 35, 18, 42, 9, 30]

maximum1 = None
maximum2 = None

for number in numbers:
    if maximum1 is None or number > maximum1:
        maximum2 = maximum1
        maximum1 = number
    elif maximum2 is None or number > maximum2:
        maximum2 = number

print(maximum1, maximum2)  # 42 35

# Логика:
# maximum1 — самое большое найденное число;
# maximum2 — второе по величине.
#
# Если найден новый maximum1,
# старый maximum1 становится maximum2.


# ------------------------------------------------------------
# 4. Разберём алгоритм по шагам

numbers = [10, 30, 20, 50, 40]

maximum1 = None
maximum2 = None

for number in numbers:
    if maximum1 is None or number > maximum1:
        maximum2 = maximum1
        maximum1 = number
    elif maximum2 is None or number > maximum2:
        maximum2 = number

    print(number, '->', maximum1, maximum2)

# Получим примерно такую картину:
# 10 -> 10 None
# 30 -> 30 10
# 20 -> 30 20
# 50 -> 50 30
# 40 -> 50 40


# ------------------------------------------------------------
# 5. Что происходит с одинаковыми максимумами

numbers = [10, 50, 20, 50, 30]

maximum1 = None
maximum2 = None

for number in numbers:
    if maximum1 is None or number > maximum1:
        maximum2 = maximum1
        maximum1 = number
    elif maximum2 is None or number > maximum2:
        maximum2 = number

print(maximum1, maximum2)  # 50 50

# Здесь два элемента со значением 50 считаются двумя максимумами.


# ------------------------------------------------------------
# 6. Два РАЗЛИЧНЫХ максимума

numbers = [10, 50, 20, 50, 30]

maximum1 = None
maximum2 = None

for number in numbers:
    if maximum1 is None or number > maximum1:
        maximum2 = maximum1
        maximum1 = number
    elif number != maximum1 and (maximum2 is None or number > maximum2):
        maximum2 = number

print(maximum1, maximum2)  # 50 30

# Условие number != maximum1 не позволяет
# одному и тому же значению занять оба места.


# ------------------------------------------------------------
# 7. Почему maximum1 = maximum2 = 0 опасно

numbers = [-20, -5, -30, -10]

maximum1 = 0
maximum2 = 0

for number in numbers:
    if number > maximum1:
        maximum2 = maximum1
        maximum1 = number
    elif number > maximum2:
        maximum2 = number

print(maximum1, maximum2)  # 0 0 — неверно

# Поэтому универсальнее использовать None
# или правильно инициализировать максимумы элементами последовательности.


# ------------------------------------------------------------
# 8. Вариант через первые два элемента списка

numbers = [-20, -5, -30, -10]

if numbers[0] > numbers[1]:
    maximum1 = numbers[0]
    maximum2 = numbers[1]
else:
    maximum1 = numbers[1]
    maximum2 = numbers[0]

for number in numbers[2:]:
    if number > maximum1:
        maximum2 = maximum1
        maximum1 = number
    elif number > maximum2:
        maximum2 = number

print(maximum1, maximum2)  # -5 -10

# Этот вариант не использует None,
# но требует, чтобы в списке было минимум два элемента.


# ------------------------------------------------------------
# 9. Два максимума среди элементов, подходящих по условию

numbers = [15, 8, 27, 12, 40, 19, 24, 36]

maximum1 = None
maximum2 = None

for number in numbers:
    if number % 2 == 0:  # рассматриваем только чётные
        if maximum1 is None or number > maximum1:
            maximum2 = maximum1
            maximum1 = number
        elif maximum2 is None or number > maximum2:
            maximum2 = number

print(maximum1, maximum2)  # 40 36


# ------------------------------------------------------------
# 10. Два максимума из файла без хранения всех чисел

maximum1 = None
maximum2 = None

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        number = int(line)

        if maximum1 is None or number > maximum1:
            maximum2 = maximum1
            maximum1 = number
        elif maximum2 is None or number > maximum2:
            maximum2 = number

print(maximum1, maximum2)

# Для большого файла это удобно:
# в памяти хранятся только два текущих максимума.


# ------------------------------------------------------------
# 11. Проверка: достаточно ли элементов

numbers = [42]

if len(numbers) < 2:
    print('Нужно минимум два элемента')
else:
    maximum1 = None
    maximum2 = None

    for number in numbers:
        if maximum1 is None or number > maximum1:
            maximum2 = maximum1
            maximum1 = number
        elif maximum2 is None or number > maximum2:
            maximum2 = number

    print(maximum1, maximum2)


# ------------------------------------------------------------
# Частые ошибки

# 1. Задать maximum1 = maximum2 = 0 при возможных отрицательных числах.
# 2. При новом maximum1 забыть сохранить старый maximum1 в maximum2.
# 3. Использовать два независимых if вместо if / elif и сломать логику обновления.
# 4. Не определить, нужны два элемента или два РАЗЛИЧНЫХ значения.
# 5. Обращаться к numbers[1], не проверив, что элементов хотя бы два.
# 6. Сортировать огромный файл, хотя два максимума можно найти за один проход.


# ------------------------------------------------------------
# Универсальный шаблон — два максимума за один проход

# maximum1 = None
# maximum2 = None
#
# for number in numbers:
#     if maximum1 is None or number > maximum1:
#         maximum2 = maximum1
#         maximum1 = number
#     elif maximum2 is None or number > maximum2:
#         maximum2 = number
#
# print(maximum1, maximum2)
