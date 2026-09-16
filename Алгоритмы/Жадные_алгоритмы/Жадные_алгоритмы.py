# ============================================================
# БЛОК 1. МАКСИМАЛЬНОЕ КОЛИЧЕСТВО ОБЪЕКТОВ
# ============================================================

durations = [40, 15, 25, 10, 30]
limit = 70

durations.sort()

total_time = 0
count = 0

for duration in durations:
    if total_time + duration <= limit:
        total_time += duration
        count += 1

print(count)
print(total_time)


# ============================================================
# БЛОК 2. СОХРАНЕНИЕ ВЫБРАННЫХ ОБЪЕКТОВ
# ============================================================

tasks = [
    ['задача 1', 40],
    ['задача 2', 15],
    ['задача 3', 25],
    ['задача 4', 10],
    ['задача 5', 30]
]

limit = 70

tasks.sort(key=lambda task: task[1])

selected = []
total_time = 0

for name, duration in tasks:
    if total_time + duration <= limit:
        selected.append(name)
        total_time += duration

print(selected)
print(total_time)


# ============================================================
# БЛОК 3. НЕПЕРЕСЕКАЮЩИЕСЯ МЕРОПРИЯТИЯ
# ============================================================

events = [
    [1, 4],
    [3, 5],
    [0, 6],
    [5, 7],
    [8, 9],
    [5, 9]
]

events.sort(key=lambda event: event[1])

selected = []
last_end = None

for start, end in events:
    if last_end is None or start >= last_end:
        selected.append([start, end])
        last_end = end

print(selected)


# ============================================================
# БЛОК 4. ЖАДНЫЙ РАЗМЕН МОНЕТ
# ============================================================

coins = [10, 5, 2, 1]
amount = 28

coins.sort(reverse=True)

selected = []
remainder = amount

for coin in coins:
    while coin <= remainder:
        selected.append(coin)
        remainder -= coin

print(selected)
print(len(selected))


# ============================================================
# БЛОК 5. КОНТРПРИМЕР ДЛЯ ЖАДНОГО РАЗМЕНА
# ============================================================

coins = [4, 3, 1]
amount = 6

coins.sort(reverse=True)

selected = []
remainder = amount

for coin in coins:
    while coin <= remainder:
        selected.append(coin)
        remainder -= coin

print(selected)
print('Жадный ответ:', len(selected))
print('Лучший вариант:', [3, 3])


# ============================================================
# БЛОК 6. ПРОВЕРКА ПОЛНЫМ ПЕРЕБОРОМ
# ============================================================

from itertools import combinations

durations = [40, 15, 25, 10, 30]
limit = 70

best_count = 0

for size in range(len(durations) + 1):
    for selected in combinations(durations, size):
        if sum(selected) <= limit:
            if size > best_count:
                best_count = size

print(best_count)


# ============================================================
# БЛОК 7. ДАННЫЕ ИЗ ФАЙЛА
# ============================================================

# Формат файла data.txt:
# первая строка — количество объектов и ограничение;
# вторая строка — размеры или длительности объектов.
#
# with open('data.txt') as f:
#     n, limit = map(int, f.readline().split())
#     durations = list(map(int, f.readline().split()))
#
# durations.sort()
#
# total = 0
# count = 0
#
# for duration in durations:
#     if total + duration <= limit:
#         total += duration
#         count += 1
#
# print(count)
# print(total)
