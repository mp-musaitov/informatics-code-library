# ============================================================
# 1. MIN() И MAX() ДЛЯ ГОТОВОГО СПИСКА
# ============================================================

numbers = [8, 3, 12, 5, 17, 2]

print(min(numbers))
print(max(numbers))


# ============================================================
# 2. ПОИСК МИНИМУМА ВРУЧНУЮ
# ============================================================

numbers = [8, 3, 12, 5, 17, 2]

minimum = numbers[0]

for x in numbers:
    if x < minimum:
        minimum = x

print(minimum)


# ============================================================
# 3. ПОИСК МАКСИМУМА ВРУЧНУЮ
# ============================================================

maximum = numbers[0]

for x in numbers:
    if x > maximum:
        maximum = x

print(maximum)


# ============================================================
# 4. МИНИМУМ С УСЛОВИЕМ И NONE
# ============================================================

numbers = [9, 7, 12, 5, 8, 21, 4]

minimum = None

for x in numbers:
    if x % 2 == 0:
        if minimum is None or x < minimum:
            minimum = x

if minimum is None:
    print('Подходящих значений нет')
else:
    print(minimum)


# ============================================================
# 5. ОДНОВРЕМЕННЫЙ ПОИСК МИНИМУМА И МАКСИМУМА
# ============================================================

numbers = [8, 3, 12, 5, 17, 2]

minimum = numbers[0]
maximum = numbers[0]

for x in numbers:
    if x < minimum:
        minimum = x

    if x > maximum:
        maximum = x

print(minimum)
print(maximum)


# ============================================================
# 6. ЗНАЧЕНИЕ ВМЕСТЕ СО СВЯЗАННЫМ ОБЪЕКТОМ
# ============================================================

students = [
    ['Али', 72],
    ['Марьям', 91],
    ['Умар', 84],
]

best_name = None
best_score = None

for name, score in students:
    if best_score is None or score > best_score:
        best_score = score
        best_name = name

print(best_name)
print(best_score)


# ============================================================
# 7. ДВА НАИБОЛЬШИХ ЭЛЕМЕНТА
# ============================================================

numbers = [8, 3, 12, 5, 17, 12]

maximum1 = None
maximum2 = None

for x in numbers:
    if maximum1 is None or x > maximum1:
        maximum2 = maximum1
        maximum1 = x
    elif maximum2 is None or x > maximum2:
        maximum2 = x

print(maximum1)
print(maximum2)


# ============================================================
# 8. МАКСИМУМ С УСЛОВИЕМ ИЗ ФАЙЛА
# ============================================================

# Шаблон закомментирован, чтобы файл можно было запустить
# без заранее созданного data.txt.

# maximum = None
#
# with open('data.txt') as f:
#     for s in f:
#         x = int(s)
#
#         if x % 7 == 0:
#             if maximum is None or x > maximum:
#                 maximum = x
#
# print(maximum)


# ============================================================
# ПАМЯТКА
# ============================================================

# Готовый непустой список без условий:
# min(numbers), max(numbers)
#
# Непустой список, все элементы подходят:
# minimum = numbers[0]
#
# Диапазон неизвестен или есть условие:
# minimum = None
# if minimum is None or x < minimum:
#     minimum = x
#
# Для максимума меняем < на >.
