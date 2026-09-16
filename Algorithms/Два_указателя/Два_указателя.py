# ============================================================
# БЛОК 1. ПОЛНЫЙ ПЕРЕБОР ПАР
# ============================================================

numbers = [2, 4, 7, 9, 12, 15]
target = 19

found = False

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], numbers[j])
            found = True
            break

    if found:
        break


# ============================================================
# БЛОК 2. ПАРА С ЗАДАННОЙ СУММОЙ
# ============================================================

numbers = [2, 4, 7, 9, 12, 15]
target = 19

left = 0
right = len(numbers) - 1

answer = None

while left < right:
    current_sum = numbers[left] + numbers[right]

    if current_sum == target:
        answer = [numbers[left], numbers[right]]
        break
    elif current_sum < target:
        left += 1
    else:
        right -= 1

print(answer)


# ============================================================
# БЛОК 3. СОХРАНЕНИЕ ИСХОДНЫХ ИНДЕКСОВ
# ============================================================

numbers = [12, 4, 15, 2, 9, 7]
target = 19

pairs = []

for index, value in enumerate(numbers):
    pairs.append([value, index])

pairs.sort()

left = 0
right = len(pairs) - 1

answer = None

while left < right:
    current_sum = pairs[left][0] + pairs[right][0]

    if current_sum == target:
        answer = [pairs[left][1], pairs[right][1]]
        break
    elif current_sum < target:
        left += 1
    else:
        right -= 1

print(answer)


# ============================================================
# БЛОК 4. БЛИЖАЙШАЯ К ЦЕЛИ СУММА
# ============================================================

numbers = [2, 4, 7, 9, 12, 15]
target = 20

left = 0
right = len(numbers) - 1

best_pair = None
best_difference = None

while left < right:
    current_sum = numbers[left] + numbers[right]
    difference = abs(current_sum - target)

    if best_difference is None or difference < best_difference:
        best_difference = difference
        best_pair = [numbers[left], numbers[right]]

    if current_sum < target:
        left += 1
    elif current_sum > target:
        right -= 1
    else:
        break

print(best_pair)
print(sum(best_pair))


# ============================================================
# БЛОК 5. ПРОВЕРКА ПАЛИНДРОМА
# ============================================================

text = 'А роза упала на лапу Азора'

clean_text = text.lower().replace(' ', '')

left = 0
right = len(clean_text) - 1

is_palindrome = True

while left < right:
    if clean_text[left] != clean_text[right]:
        is_palindrome = False
        break

    left += 1
    right -= 1

print(is_palindrome)


# ============================================================
# БЛОК 6. СЛИЯНИЕ ОТСОРТИРОВАННЫХ СПИСКОВ
# ============================================================

first = [1, 4, 7, 10]
second = [2, 3, 8, 12]

i = 0
j = 0

result = []

while i < len(first) and j < len(second):
    if first[i] < second[j]:
        result.append(first[i])
        i += 1
    else:
        result.append(second[j])
        j += 1

while i < len(first):
    result.append(first[i])
    i += 1

while j < len(second):
    result.append(second[j])
    j += 1

print(result)


# ============================================================
# БЛОК 7. ОБЩИЕ ЭЛЕМЕНТЫ ДВУХ СПИСКОВ
# ============================================================

first = [1, 2, 2, 4, 6, 8]
second = [2, 2, 3, 4, 7, 8]

i = 0
j = 0

common = []

while i < len(first) and j < len(second):
    if first[i] == second[j]:
        if not common or common[-1] != first[i]:
            common.append(first[i])

        i += 1
        j += 1
    elif first[i] < second[j]:
        i += 1
    else:
        j += 1

print(common)


# ============================================================
# БЛОК 8. ПОИСК ПАРЫ В ДАННЫХ ИЗ ФАЙЛА
# ============================================================

# Формат файла data.txt:
# первая строка — количество чисел и целевая сумма;
# вторая строка — числа.
#
# with open('data.txt') as f:
#     n, target = map(int, f.readline().split())
#     numbers = list(map(int, f.readline().split()))
#
# numbers.sort()
#
# left = 0
# right = len(numbers) - 1
#
# answer = None
#
# while left < right:
#     current_sum = numbers[left] + numbers[right]
#
#     if current_sum == target:
#         answer = [numbers[left], numbers[right]]
#         break
#     elif current_sum < target:
#         left += 1
#     else:
#         right -= 1
#
# print(answer)
