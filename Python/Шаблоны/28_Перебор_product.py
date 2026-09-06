# Перебор через itertools.product

# product() строит декартово произведение — все комбинации значений.
# Это удобная замена нескольким вложенным циклам.

from itertools import product

# ------------------------------------------------------------
# 1. Все пары из набора значений

values = [1, 2, 3]

for a, b in product(values, repeat=2):
    print(a, b)

# Эквивалентно:
# for a in values:
#     for b in values:
#         print(a, b)

# ------------------------------------------------------------
# 2. Все тройки

for a, b, c in product([0, 1], repeat=3):
    print(a, b, c)

# Всего будет 2 ** 3 = 8 комбинаций.

# ------------------------------------------------------------
# 3. Перебор строк фиксированной длины

alphabet = 'ABC'

for symbols in product(alphabet, repeat=3):
    word = ''.join(symbols)
    print(word)

# ------------------------------------------------------------
# 4. Подсчитать слова по условию

alphabet = 'АБВГ'
count = 0

for symbols in product(alphabet, repeat=4):
    word = ''.join(symbols)

    if word.count('А') == 2:
        count += 1

print(count)

# ------------------------------------------------------------
# 5. Ограничение на соседние символы

alphabet = 'ABC'
count = 0

for symbols in product(alphabet, repeat=4):
    word = ''.join(symbols)

    if 'AA' not in word:
        count += 1

print(count)

# ------------------------------------------------------------
# 6. Перебор цифр числа

count = 0

for digits in product('0123456789', repeat=3):
    if digits[0] == '0':
        continue

    number = int(''.join(digits))

    if number % 7 == 0:
        count += 1

print(count)

# ------------------------------------------------------------
# 7. Разные наборы значений для разных позиций

for letter, digit in product('AB', '123'):
    print(letter, digit)

# Получим:
# A 1
# A 2
# A 3
# B 1
# B 2
# B 3

# ------------------------------------------------------------
# 8. Проверка логических выражений

for a, b, c in product([False, True], repeat=3):
    f = (a or b) and (not c)
    print(a, b, c, f)

# ------------------------------------------------------------
# 9. Когда product() особенно удобен

# - задания на слова и коды;
# - перебор небольших наборов символов;
# - таблицы истинности;
# - перебор цифр;
# - замена большого количества вложенных циклов.

# ------------------------------------------------------------
# Частые ошибки

# 1. Забыть import: from itertools import product.
# 2. Не указать repeat, когда все позиции используют один набор значений.
# 3. Забыть ''.join(...), если нужна строка.
# 4. Не исключить ведущий ноль при переборе чисел.
# 5. Не оценить количество вариантов: len(alphabet) ** length.

# ------------------------------------------------------------
# Универсальный шаблон

# from itertools import product
#
# count = 0
#
# for symbols in product(alphabet, repeat=length):
#     word = ''.join(symbols)
#     if условие:
#         count += 1
#
# print(count)
