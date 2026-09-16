# ============================================================
# БЛОК 1. ОБЫЧНАЯ СУММА НА ОТРЕЗКЕ
# ============================================================

numbers = [8, 3, 12, 5, 17, 2]

left = 1
right = 4

segment_sum = 0

for i in range(left, right + 1):
    segment_sum += numbers[i]

print(segment_sum)


# ============================================================
# БЛОК 2. ПОСТРОЕНИЕ ПРЕФИКСНЫХ СУММ
# ============================================================

numbers = [8, 3, 12, 5, 17, 2]

prefix = [0]

for x in numbers:
    prefix.append(prefix[-1] + x)

print(prefix)


# ============================================================
# БЛОК 3. СУММА ПО ИНДЕКСАМ PYTHON
# ============================================================

left = 1
right = 4

segment_sum = prefix[right + 1] - prefix[left]

print(segment_sum)


# ============================================================
# БЛОК 4. СУММА ПО ПОЗИЦИЯМ С ЕДИНИЦЫ
# ============================================================

left = 2
right = 5

segment_sum = prefix[right] - prefix[left - 1]

print(segment_sum)


# ============================================================
# БЛОК 5. НЕСКОЛЬКО ЗАПРОСОВ
# ============================================================

queries = [
    [1, 4],
    [0, 2],
    [3, 5]
]

for left, right in queries:
    segment_sum = prefix[right + 1] - prefix[left]
    print(segment_sum)


# ============================================================
# БЛОК 6. КОЛИЧЕСТВО ЧЁТНЫХ ЧИСЕЛ НА ОТРЕЗКЕ
# ============================================================

numbers = [8, 3, 12, 5, 17, 2]

prefix_even = [0]

for x in numbers:
    if x % 2 == 0:
        prefix_even.append(prefix_even[-1] + 1)
    else:
        prefix_even.append(prefix_even[-1])

left = 1
right = 5

even_count = prefix_even[right + 1] - prefix_even[left]

print(even_count)


# ============================================================
# БЛОК 7. СРЕДНЕЕ ЗНАЧЕНИЕ НА ОТРЕЗКЕ
# ============================================================

numbers = [8, 3, 12, 5, 17, 2]

prefix = [0]

for x in numbers:
    prefix.append(prefix[-1] + x)

left = 1
right = 4

segment_sum = prefix[right + 1] - prefix[left]
length = right - left + 1

average = segment_sum / length

print(average)


# ============================================================
# БЛОК 8. ДАННЫЕ И ЗАПРОСЫ ИЗ ФАЙЛА
# ============================================================

# Формат файла data.txt:
# первая строка — количество чисел;
# вторая строка — числа;
# третья строка — количество запросов;
# далее записаны границы с нумерацией позиций от единицы.
#
# with open('data.txt') as f:
#     n = int(f.readline())
#     numbers = list(map(int, f.readline().split()))
#     q = int(f.readline())
#
#     prefix = [0]
#
#     for x in numbers:
#         prefix.append(prefix[-1] + x)
#
#     for _ in range(q):
#         left, right = map(int, f.readline().split())
#
#         segment_sum = prefix[right] - prefix[left - 1]
#
#         print(segment_sum)
