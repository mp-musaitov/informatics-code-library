# ============================================================
# БЛОК 1. ПОЛНЫЙ ПЕРЕБОР ОКОН ДЛИНЫ K
# ============================================================

numbers = [4, 2, 7, 1, 3, 6, 2]
k = 3

maximum = None

for left in range(len(numbers) - k + 1):
    window_sum = 0

    for i in range(left, left + k):
        window_sum += numbers[i]

    if maximum is None or window_sum > maximum:
        maximum = window_sum

print(maximum)


# ============================================================
# БЛОК 2. МАКСИМАЛЬНАЯ СУММА ФИКСИРОВАННОГО ОКНА
# ============================================================

window_sum = sum(numbers[:k])
maximum = window_sum

for right in range(k, len(numbers)):
    window_sum -= numbers[right - k]
    window_sum += numbers[right]

    if window_sum > maximum:
        maximum = window_sum

print(maximum)


# ============================================================
# БЛОК 3. ГРАНИЦЫ ЛУЧШЕГО ОКНА
# ============================================================

numbers = [1, 4, 2, 7, 3, 6, 2]
k = 3

window_sum = sum(numbers[:k])
maximum = window_sum

best_left = 0

for right in range(k, len(numbers)):
    window_sum -= numbers[right - k]
    window_sum += numbers[right]

    if window_sum > maximum:
        maximum = window_sum
        best_left = right - k + 1

best_right = best_left + k - 1

print(maximum)
print(best_left, best_right)
print(numbers[best_left:best_right + 1])


# ============================================================
# БЛОК 4. СРЕДНЕЕ ЗНАЧЕНИЕ В КАЖДОМ ОКНЕ
# ============================================================

numbers = [4, 2, 7, 1, 3, 6, 2]
k = 3

window_sum = sum(numbers[:k])

print(window_sum / k)

for right in range(k, len(numbers)):
    window_sum -= numbers[right - k]
    window_sum += numbers[right]

    print(window_sum / k)


# ============================================================
# БЛОК 5. КОЛИЧЕСТВО ЧЁТНЫХ ЧИСЕЛ В ОКНЕ
# ============================================================

numbers = [4, 3, 8, 6, 5, 2, 10]
k = 4

even_count = 0

for x in numbers[:k]:
    if x % 2 == 0:
        even_count += 1

maximum = even_count

for right in range(k, len(numbers)):
    left_value = numbers[right - k]
    right_value = numbers[right]

    if left_value % 2 == 0:
        even_count -= 1

    if right_value % 2 == 0:
        even_count += 1

    if even_count > maximum:
        maximum = even_count

print(maximum)


# ============================================================
# БЛОК 6. САМЫЙ ДЛИННЫЙ ОТРЕЗОК С СУММОЙ НЕ БОЛЬШЕ LIMIT
# ============================================================

# Числа должны быть неотрицательными.

numbers = [2, 1, 3, 2, 1, 1, 4]
limit = 7

left = 0
window_sum = 0

best_length = 0
best_left = 0
best_right = -1

for right in range(len(numbers)):
    window_sum += numbers[right]

    while window_sum > limit:
        window_sum -= numbers[left]
        left += 1

    length = right - left + 1

    if length > best_length:
        best_length = length
        best_left = left
        best_right = right

print(best_length)
print(numbers[best_left:best_right + 1])


# ============================================================
# БЛОК 7. САМЫЙ КОРОТКИЙ ОТРЕЗОК С СУММОЙ НЕ МЕНЬШЕ TARGET
# ============================================================

# Числа должны быть неотрицательными.

numbers = [2, 1, 5, 2, 3, 2]
target = 7

left = 0
window_sum = 0

best_length = None

for right in range(len(numbers)):
    window_sum += numbers[right]

    while window_sum >= target:
        length = right - left + 1

        if best_length is None or length < best_length:
            best_length = length

        window_sum -= numbers[left]
        left += 1

print(best_length)


# ============================================================
# БЛОК 8. ДАННЫЕ ИЗ ФАЙЛА
# ============================================================

# Формат файла data.txt:
# первая строка — количество чисел и размер окна;
# вторая строка — числа.
#
# with open('data.txt') as f:
#     n, k = map(int, f.readline().split())
#     numbers = list(map(int, f.readline().split()))
#
# window_sum = sum(numbers[:k])
# maximum = window_sum
#
# for right in range(k, len(numbers)):
#     window_sum -= numbers[right - k]
#     window_sum += numbers[right]
#
#     if window_sum > maximum:
#         maximum = window_sum
#
# print(maximum)
