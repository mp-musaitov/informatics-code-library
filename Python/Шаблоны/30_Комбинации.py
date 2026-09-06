# Комбинации через itertools.combinations

# combinations() выбирает элементы без повторений и БЕЗ учёта порядка.
# Поэтому пара (A, B) и (B, A) считается одной и той же комбинацией.

from itertools import combinations

# ------------------------------------------------------------
# 1. Все пары из списка

values = [1, 2, 3, 4]

for pair in combinations(values, 2):
    print(pair)

# Получим:
# (1, 2)
# (1, 3)
# (1, 4)
# (2, 3)
# (2, 4)
# (3, 4)

# ------------------------------------------------------------
# 2. Все тройки

letters = 'ABCDE'

for variant in combinations(letters, 3):
    print(''.join(variant))

# ------------------------------------------------------------
# 3. Подсчитать пары по условию

numbers = [10, 15, 20, 25, 30]
count = 0

for a, b in combinations(numbers, 2):
    if (a + b) % 10 == 0:
        count += 1

print(count)

# ------------------------------------------------------------
# 4. Найти максимальную сумму пары

numbers = [7, 12, 4, 20, 15]
maximum = None
best_pair = None

for a, b in combinations(numbers, 2):
    value = a + b

    if maximum is None or value > maximum:
        maximum = value
        best_pair = (a, b)

print(maximum, best_pair)

# ------------------------------------------------------------
# 5. combinations() не использует один и тот же элемент дважды

values = [1, 2, 3]
print(list(combinations(values, 2)))

# Здесь не будет (1, 1), (2, 2), (3, 3).

# ------------------------------------------------------------
# 6. Если повторения нужны — combinations_with_replacement()

from itertools import combinations_with_replacement

values = [1, 2, 3]

for pair in combinations_with_replacement(values, 2):
    print(pair)

# Теперь появятся (1, 1), (2, 2), (3, 3).

# ------------------------------------------------------------
# 7. Все подмножества фиксированного размера

students = ['Адам', 'Али', 'Муса', 'Саид']

for team in combinations(students, 2):
    print(team)

# Полезно для задач выбора команды, группы, набора объектов.

# ------------------------------------------------------------
# 8. Когда использовать combinations()

# Используйте combinations(), если:
# - порядок НЕ важен;
# - один и тот же элемент нельзя выбирать повторно;
# - нужно выбрать k элементов из набора.

# Если порядок важен — permutations().
# Если повторения и порядок разрешены — product().

# ------------------------------------------------------------
# Частые ошибки

# 1. Путать combinations() с permutations().
# 2. Ожидать пары (a, b) и (b, a) одновременно.
# 3. Ожидать повторение одного и того же элемента.
# 4. Не распаковывать кортеж: for a, b in combinations(..., 2).

# ------------------------------------------------------------
# Универсальный шаблон

# from itertools import combinations
#
# count = 0
#
# for a, b in combinations(numbers, 2):
#     if условие:
#         count += 1
#
# print(count)
