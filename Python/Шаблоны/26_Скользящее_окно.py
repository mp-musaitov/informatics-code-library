# Скользящее окно

# Скользящее окно — способ обрабатывать фрагменты фиксированной длины:
# пары, тройки, пятёрки и любые другие подряд идущие элементы.

# ------------------------------------------------------------
# 1. Все окна длины 3

numbers = [10, 20, 30, 40, 50]
window_size = 3

for i in range(len(numbers) - window_size + 1):
    window = numbers[i:i + window_size]
    print(window)

# Получим:
# [10, 20, 30]
# [20, 30, 40]
# [30, 40, 50]

# ------------------------------------------------------------
# 2. Сумма каждого окна

numbers = [10, 20, 30, 40, 50]
window_size = 3

for i in range(len(numbers) - window_size + 1):
    current_sum = sum(numbers[i:i + window_size])
    print(current_sum)

# ------------------------------------------------------------
# 3. Максимальная сумма окна

numbers = [5, 1, 7, 3, 9, 2]
window_size = 3
maximum_sum = None

for i in range(len(numbers) - window_size + 1):
    current_sum = sum(numbers[i:i + window_size])

    if maximum_sum is None or current_sum > maximum_sum:
        maximum_sum = current_sum

print(maximum_sum)

# ------------------------------------------------------------
# 4. Быстрое скользящее окно без повторного sum()

numbers = [5, 1, 7, 3, 9, 2]
window_size = 3

current_sum = sum(numbers[:window_size])
maximum_sum = current_sum

for i in range(window_size, len(numbers)):
    current_sum += numbers[i]
    current_sum -= numbers[i - window_size]

    if current_sum > maximum_sum:
        maximum_sum = current_sum

print(maximum_sum)

# Здесь при каждом сдвиге:
# 1) добавляется новый элемент справа;
# 2) удаляется старый элемент слева.

# ------------------------------------------------------------
# 5. Посчитать окна, удовлетворяющие условию

numbers = [10, 15, 20, 25, 30, 35]
window_size = 2
count = 0

for i in range(len(numbers) - window_size + 1):
    window = numbers[i:i + window_size]

    if sum(window) % 10 == 0:
        count += 1

print(count)

# ------------------------------------------------------------
# 6. Максимум среди окон, подходящих по условию

numbers = [12, 7, 18, 5, 21, 9]
window_size = 3
maximum_sum = None

for i in range(len(numbers) - window_size + 1):
    window = numbers[i:i + window_size]

    # пример: хотя бы один элемент окна кратен 7
    if any(number % 7 == 0 for number in window):
        current_sum = sum(window)

        if maximum_sum is None or current_sum > maximum_sum:
            maximum_sum = current_sum

print(maximum_sum)

# ------------------------------------------------------------
# 7. Окна в строке

text = 'ABCDEFG'
window_size = 3

for i in range(len(text) - window_size + 1):
    fragment = text[i:i + window_size]
    print(fragment)

# Получим ABC, BCD, CDE, DEF, EFG.

# ------------------------------------------------------------
# 8. Подсчёт строковых фрагментов по условию

text = 'ABACABA'
window_size = 3
count = 0

for i in range(len(text) - window_size + 1):
    fragment = text[i:i + window_size]

    if fragment.count('A') == 2:
        count += 1

print(count)

# ------------------------------------------------------------
# 9. Окно с индексами

numbers = [4, 8, 15, 16, 23, 42]
window_size = 3

for i in range(len(numbers) - window_size + 1):
    left = i
    right = i + window_size - 1
    print(left, right, numbers[i:i + window_size])

# ------------------------------------------------------------
# 10. Проверка длины

numbers = [1, 2]
window_size = 3

if len(numbers) < window_size:
    print('Недостаточно элементов')
else:
    for i in range(len(numbers) - window_size + 1):
        print(numbers[i:i + window_size])

# ------------------------------------------------------------
# Частые ошибки

# 1. Писать range(len(numbers) - window_size) и потерять последнее окно.
#    Правильно: range(len(numbers) - window_size + 1).
# 2. Перепутать длину окна и последний индекс.
# 3. Каждый раз вызывать sum() для огромного окна, хотя сумму можно обновлять за O(1).
# 4. Не проверить, что последовательность хотя бы не короче окна.
# 5. Путать скользящее окно с перебором всех возможных пар: здесь элементы идут подряд.

# ------------------------------------------------------------
# Универсальный шаблон

# window_size = k
#
# for i in range(len(data) - window_size + 1):
#     window = data[i:i + window_size]
#     if условие:
#         ...

# Быстрая сумма окна:
# current_sum = sum(numbers[:k])
# for i in range(k, len(numbers)):
#     current_sum += numbers[i]
#     current_sum -= numbers[i - k]
#     ...
