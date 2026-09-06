# Перестановки через itertools.permutations

# permutations() строит все варианты расположения элементов,
# где каждый выбранный элемент используется не более одного раза.

from itertools import permutations

# ------------------------------------------------------------
# 1. Все перестановки списка

values = [1, 2, 3]

for variant in permutations(values):
    print(variant)

# Всего 3! = 6 перестановок.

# ------------------------------------------------------------
# 2. Собрать перестановку в строку

letters = 'ABC'

for variant in permutations(letters):
    word = ''.join(variant)
    print(word)

# ------------------------------------------------------------
# 3. Перестановки длины меньше количества элементов

letters = 'ABCD'

for variant in permutations(letters, 2):
    print(''.join(variant))

# Здесь выбираются любые 2 разных символа с учётом порядка.

# ------------------------------------------------------------
# 4. Подсчитать варианты по условию

letters = 'АБВГ'
count = 0

for variant in permutations(letters):
    word = ''.join(variant)

    if word[0] != 'А':
        count += 1

print(count)

# ------------------------------------------------------------
# 5. Перестановка цифр числа

number = '1234'

for variant in permutations(number):
    value = int(''.join(variant))
    print(value)

# ------------------------------------------------------------
# 6. Ведущий ноль

digits = '0123'

for variant in permutations(digits):
    if variant[0] == '0':
        continue

    number = int(''.join(variant))
    print(number)

# ------------------------------------------------------------
# 7. Найти максимум среди перестановок

number = '5312'
maximum = None

for variant in permutations(number):
    value = int(''.join(variant))

    if maximum is None or value > maximum:
        maximum = value

print(maximum)  # 5321

# ------------------------------------------------------------
# 8. ВАЖНО: одинаковые элементы дают повторяющиеся варианты

letters = 'AAB'

variants = list(permutations(letters))
print(len(variants))  # 6

# Но уникальных строк меньше:
unique_words = {''.join(variant) for variant in permutations(letters)}
print(len(unique_words))  # 3

# ------------------------------------------------------------
# 9. Когда использовать permutations()

# Используйте permutations(), если:
# - важен порядок элементов;
# - один элемент нельзя повторно выбирать;
# - нужно переставить все или часть имеющихся элементов.

# Если повторения разрешены, чаще нужен product().
# Если порядок не важен, чаще нужен combinations().

# ------------------------------------------------------------
# Частые ошибки

# 1. Путать permutations() с product(): permutations не повторяет один и тот же элемент.
# 2. Путать permutations() с combinations(): здесь порядок важен.
# 3. Забывать ''.join(), если нужна строка.
# 4. Не исключать ведущий ноль при построении чисел.
# 5. Не учитывать повторяющиеся результаты, если исходные элементы одинаковые.

# ------------------------------------------------------------
# Универсальный шаблон

# from itertools import permutations
#
# count = 0
#
# for variant in permutations(elements, length):
#     value = ''.join(variant)
#     if условие:
#         count += 1
#
# print(count)
