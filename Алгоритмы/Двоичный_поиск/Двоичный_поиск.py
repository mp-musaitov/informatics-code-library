# ============================================================
# БЛОК 1. ПОСЛЕДОВАТЕЛЬНЫЙ ПОИСК
# ============================================================

numbers = [2, 4, 7, 9, 12, 15, 18]
target = 12

answer = None

for i in range(len(numbers)):
    if numbers[i] == target:
        answer = i
        break

print(answer)


# ============================================================
# БЛОК 2. РУЧНОЙ ДВОИЧНЫЙ ПОИСК
# ============================================================

left = 0
right = len(numbers) - 1

answer = None

while left <= right:
    middle = (left + right) // 2

    if numbers[middle] == target:
        answer = middle
        break
    elif numbers[middle] < target:
        left = middle + 1
    else:
        right = middle - 1

print(answer)


# ============================================================
# БЛОК 3. ФУНКЦИЯ ДВОИЧНОГО ПОИСКА
# ============================================================

def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle
        elif numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return None


print(binary_search(numbers, 12))
print(binary_search(numbers, 10))


# ============================================================
# БЛОК 4. ПЕРВОЕ ВХОЖДЕНИЕ
# ============================================================

numbers = [2, 4, 4, 4, 7, 9]
target = 4

left = 0
right = len(numbers) - 1

answer = None

while left <= right:
    middle = (left + right) // 2

    if numbers[middle] >= target:
        if numbers[middle] == target:
            answer = middle

        right = middle - 1
    else:
        left = middle + 1

print(answer)


# ============================================================
# БЛОК 5. ПОСЛЕДНЕЕ ВХОЖДЕНИЕ
# ============================================================

left = 0
right = len(numbers) - 1

answer = None

while left <= right:
    middle = (left + right) // 2

    if numbers[middle] <= target:
        if numbers[middle] == target:
            answer = middle

        left = middle + 1
    else:
        right = middle - 1

print(answer)


# ============================================================
# БЛОК 6. BISECT_LEFT() И BISECT_RIGHT()
# ============================================================

from bisect import bisect_left, bisect_right

left_position = bisect_left(numbers, target)
right_position = bisect_right(numbers, target)

print(left_position)
print(right_position)


# ============================================================
# БЛОК 7. КОЛИЧЕСТВО ВХОЖДЕНИЙ
# ============================================================

count = bisect_right(numbers, target) - bisect_left(numbers, target)

print(count)


# ============================================================
# БЛОК 8. ДВОИЧНЫЙ ПОИСК ПО ОТВЕТУ
# ============================================================

number = 30

left = 0
right = number

while left < right:
    middle = (left + right) // 2

    if middle * middle >= number:
        right = middle
    else:
        left = middle + 1

print(left)


# ============================================================
# БЛОК 9. ПОИСК ЗНАЧЕНИЙ ИЗ ФАЙЛА
# ============================================================

# Формат файла data.txt:
# первая строка — количество элементов;
# вторая строка — отсортированный список;
# третья строка — количество запросов;
# далее записаны искомые значения.
#
# from bisect import bisect_left
#
# with open('data.txt') as f:
#     n = int(f.readline())
#     numbers = list(map(int, f.readline().split()))
#     q = int(f.readline())
#
#     for _ in range(q):
#         target = int(f.readline())
#
#         position = bisect_left(numbers, target)
#
#         if position < len(numbers) and numbers[position] == target:
#             print(position)
#         else:
#             print('Не найдено')
