# Максимум и минимум

# Шаблоны поиска наибольшего и наименьшего значения.

# 1. Самый короткий способ — max() и min()
numbers = [12, 5, 27, 3, 18]

print(max(numbers))  # 27
print(min(numbers))  # 3

# Когда использовать:
# если все данные уже находятся в списке.


# 2. Поиск максимума вручную
numbers = [12, 5, 27, 3, 18]

maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

print(maximum)  # 27

# Идея:
# сначала считаем максимумом первый элемент,
# затем сравниваем с ним остальные.


# 3. Поиск минимума вручную
numbers = [12, 5, 27, 3, 18]

minimum = numbers[0]

for number in numbers:
    if number < minimum:
        minimum = number

print(minimum)  # 3


# 4. Максимум и минимум одновременно
numbers = [12, 5, 27, 3, 18]

maximum = numbers[0]
minimum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

    if number < minimum:
        minimum = number

print(maximum, minimum)  # 27 3


# 5. Индекс максимального элемента
numbers = [12, 5, 27, 3, 18]

maximum = numbers[0]
maximum_index = 0

for i in range(len(numbers)):
    if numbers[i] > maximum:
        maximum = numbers[i]
        maximum_index = i

print(maximum)        # 27
print(maximum_index)  # 2

# Если нужно только положение максимума,
# удобно хранить и значение, и его индекс.


# 6. Индекс минимального элемента
numbers = [12, 5, 27, 3, 18]

minimum = numbers[0]
minimum_index = 0

for i in range(len(numbers)):
    if numbers[i] < minimum:
        minimum = numbers[i]
        minimum_index = i

print(minimum)        # 3
print(minimum_index)  # 3


# 7. Что будет, если максимум встречается несколько раз
numbers = [10, 25, 7, 25, 3]

maximum = numbers[0]
maximum_index = 0

for i in range(len(numbers)):
    if numbers[i] > maximum:
        maximum = numbers[i]
        maximum_index = i

print(maximum_index)  # 1

# Такой вариант запомнит индекс ПЕРВОГО максимума.


# 8. Индекс последнего максимума
numbers = [10, 25, 7, 25, 3]

maximum = numbers[0]
maximum_index = 0

for i in range(len(numbers)):
    if numbers[i] >= maximum:
        maximum = numbers[i]
        maximum_index = i

print(maximum_index)  # 3

# Отличие только в >= вместо >.


# 9. Максимум без сохранения всего списка
# Полезно, если числа поступают по одному.

n = int(input())
first = int(input())
maximum = first

for _ in range(n - 1):
    number = int(input())

    if number > maximum:
        maximum = number

print(maximum)

# Здесь список вообще не нужен.


# 10. Максимум из файла без загрузки всего файла
with open('input.txt', 'r', encoding='utf-8') as file:
    first = int(file.readline())
    maximum = first

    for line in file:
        number = int(line)

        if number > maximum:
            maximum = number

print(maximum)


# 11. Важная ошибка: maximum = 0
numbers = [-8, -3, -12, -5]

# Неправильно:
# maximum = 0
# Тогда ответ останется 0, хотя такого числа в списке нет.

# Правильно:
maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

print(maximum)  # -3


# 12. Если список может быть пустым
numbers = []

if numbers:
    print(max(numbers))
else:
    print('Список пуст')


# Типичные ошибки
# 1. Инициализировать максимум нулём, когда данные могут быть отрицательными.
# 2. Инициализировать минимум слишком маленьким числом.
# 3. Использовать numbers[0], не проверив, что список не пуст.
# 4. Путать > и >=, если нужен первый или последний максимум.
# 5. Искать индекс через numbers.index(max(numbers)), если важно понять сам алгоритм.


# Универсальные шаблоны

# Максимум:
# maximum = numbers[0]
# for number in numbers:
#     if number > maximum:
#         maximum = number

# Минимум:
# minimum = numbers[0]
# for number in numbers:
#     if number < minimum:
#         minimum = number

# Максимум с индексом:
# maximum = numbers[0]
# maximum_index = 0
# for i in range(len(numbers)):
#     if numbers[i] > maximum:
#         maximum = numbers[i]
#         maximum_index = i
