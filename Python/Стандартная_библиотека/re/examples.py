# re: практическая шпаргалка
# Независимые блоки: копируйте нужный вместе с импортами и данными.

# БЛОК 1. Извлечение целых чисел
from re import findall

text = 'Температуры: -12, 7 и 0'
numbers = list(map(int, findall(r'-?[0-9]+', text)))
print(numbers)  # [-12, 7, 0]
print(sum(numbers))  # -5

# БЛОК 2. Проверка всего кода
from re import fullmatch

code = 'AB123'
print(fullmatch(r'[A-Z]{2}[0-9]{3}', code) is not None)  # True
print(fullmatch(r'[A-Z]{2}[0-9]{3}', 'AB123x') is not None)  # False

# БЛОК 3. Первое найденное число
from re import search

text = 'Задача 24, вариант 3'
match = search(r'[0-9]+', text)
if match is not None:
    print(match.group())  # 24
else:
    print('Чисел нет')

# БЛОК 4. Самая длинная серия из A и B
from re import findall

text = 'CAABBCABX'
parts = findall(r'[AB]+', text)
if parts:
    print(len(max(parts, key=len)))  # 4
else:
    print(0)

# БЛОК 5. Замена нескольких пробелов
from re import sub

text = 'кот   и  дом'
print(sub(r' +', ' ', text))  # кот и дом

# БЛОК 6. Разные разделители
from re import split

line = '10,20;30 40'
parts = split(r'[,; ]+', line.strip())
numbers = [int(part) for part in parts if part]
print(numbers)  # [10, 20, 30, 40]

# Частые ошибки
# 1. Считать search проверкой всей строки: для этого нужен fullmatch.
# 2. Вызывать .group() у None, когда совпадения нет.
# 3. Путать маску * из fnmatch и повторение предыдущего элемента в re.
# 4. Забывать знак минус при извлечении отрицательных чисел.
# 5. Применять max к пустому списку найденных серий.
