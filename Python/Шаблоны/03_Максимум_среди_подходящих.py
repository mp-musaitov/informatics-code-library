# Максимум среди элементов, удовлетворяющих условию

# Задача:
# найти максимальный элемент не среди всех чисел,
# а только среди тех, которые подходят под заданное условие.

# ------------------------------------------------------------
# 1. Самый понятный вариант — сначала отобрать подходящие

numbers = [15, 8, 27, 12, 40, 19, 24]

suitable = []

for number in numbers:
    if number % 2 == 0:
        suitable.append(number)

if suitable:
    print(max(suitable))  # 40
else:
    print('Подходящих элементов нет')

# Когда применять:
# когда список небольшой и важнее всего понятность решения.


# ------------------------------------------------------------
# 2. Короткий вариант через генератор списка

numbers = [15, 8, 27, 12, 40, 19, 24]

suitable = [number for number in numbers if number % 2 == 0]

if suitable:
    print(max(suitable))  # 40


# ------------------------------------------------------------
# 3. Поиск максимума без создания дополнительного списка

numbers = [15, 8, 27, 12, 40, 19, 24]

maximum = None

for number in numbers:
    if number % 2 == 0:
        if maximum is None or number > maximum:
            maximum = number

print(maximum)  # 40

# None означает: подходящий элемент пока ещё не найден.
# Первый подходящий элемент автоматически становится максимумом.


# ------------------------------------------------------------
# 4. Почему нельзя бездумно начинать с maximum = 0

numbers = [-15, -8, -27, -12]

maximum = 0

for number in numbers:
    if number % 2 == 0 and number > maximum:
        maximum = number

print(maximum)  # 0 — ОШИБОЧНЫЙ результат!

# Среди подходящих чисел были -8 и -12.
# Правильный максимум равен -8, но ни одно отрицательное число
# не оказалось больше начального значения 0.


# ------------------------------------------------------------
# 5. Правильный вариант для любых чисел

numbers = [-15, -8, -27, -12]

maximum = None

for number in numbers:
    if number % 2 == 0:
        if maximum is None or number > maximum:
            maximum = number

print(maximum)  # -8


# ------------------------------------------------------------
# 6. Максимум среди чисел по нескольким условиям

numbers = [12, 25, 30, 42, 55, 60, 72]

maximum = None

for number in numbers:
    # число должно быть чётным и делиться на 3
    if number % 2 == 0 and number % 3 == 0:
        if maximum is None or number > maximum:
            maximum = number

print(maximum)  # 72


# ------------------------------------------------------------
# 7. Одновременно количество и максимум подходящих элементов

numbers = [11, 20, 35, 40, 55, 60, 75]

count = 0
maximum = None

for number in numbers:
    if number % 5 == 0:
        count += 1

        if maximum is None or number > maximum:
            maximum = number

print(count, maximum)  # 6 75

# Такой шаблон очень часто встречается в задачах:
# «Определите количество элементов ... и максимальный из них».


# ------------------------------------------------------------
# 8. Минимум среди подходящих элементов

numbers = [15, 8, 27, 12, 40, 19, 24]

minimum = None

for number in numbers:
    if number % 2 == 0:
        if minimum is None or number < minimum:
            minimum = number

print(minimum)  # 8


# ------------------------------------------------------------
# 9. Что делать, если подходящих элементов нет

numbers = [1, 3, 5, 7, 9]

maximum = None

for number in numbers:
    if number % 2 == 0:
        if maximum is None or number > maximum:
            maximum = number

if maximum is None:
    print('Подходящих элементов нет')
else:
    print(maximum)

# В этом примере будет выведено:
# Подходящих элементов нет


# ------------------------------------------------------------
# 10. Шаблон для файла

maximum = None
count = 0

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        number = int(line)

        if number % 2 == 0:  # заменить на условие задачи
            count += 1

            if maximum is None or number > maximum:
                maximum = number

print(count, maximum)

# Преимущество этого варианта:
# весь файл не нужно загружать в список.


# ------------------------------------------------------------
# 11. Короткий вариант через max() и генератор

numbers = [15, 8, 27, 12, 40, 19, 24]

maximum = max(number for number in numbers if number % 2 == 0)
print(maximum)  # 40

# ВАЖНО:
# если ни один элемент не подходит, такой max() вызовет ValueError.


# ------------------------------------------------------------
# 12. Безопасный короткий вариант через default=None

numbers = [1, 3, 5, 7]

maximum = max(
    (number for number in numbers if number % 2 == 0),
    default=None
)

print(maximum)  # None

# default=None говорит функции max():
# если подходящих элементов нет, вернуть None вместо ошибки.


# ------------------------------------------------------------
# Частые ошибки

# 1. Начать с maximum = 0, хотя подходящие числа могут быть отрицательными.
# 2. Вызвать max() для пустого списка подходящих элементов.
# 3. Обновлять maximum вне условия отбора.
# 4. Перепутать > и < при поиске максимума или минимума.
# 5. Посчитать количество всех элементов вместо количества подходящих.
# 6. Забыть проверить случай, когда подходящих элементов нет.


# ------------------------------------------------------------
# Универсальный шаблон

# maximum = None
# count = 0
#
# for number in numbers:
#     if условие:
#         count += 1
#
#         if maximum is None or number > maximum:
#             maximum = number
#
# if maximum is None:
#     print('Подходящих элементов нет')
# else:
#     print(count, maximum)
