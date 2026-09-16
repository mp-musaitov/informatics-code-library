# ============================================================
# БЛОК 1. ВСЕ ДВОИЧНЫЕ ПОСЛЕДОВАТЕЛЬНОСТИ
# ============================================================

n = 3

def generate_binary(sequence):
    if len(sequence) == n:
        print(sequence)
        return

    generate_binary(sequence + '0')
    generate_binary(sequence + '1')


generate_binary('')


# ============================================================
# БЛОК 2. ПОСЛЕДОВАТЕЛЬНОСТИ БЕЗ ДВУХ ЕДИНИЦ ПОДРЯД
# ============================================================

n = 4

def generate_without_two_ones(sequence):
    if len(sequence) == n:
        print(sequence)
        return

    generate_without_two_ones(sequence + '0')

    if not sequence or sequence[-1] != '1':
        generate_without_two_ones(sequence + '1')


generate_without_two_ones('')


# ============================================================
# БЛОК 3. ПЕРЕСТАНОВКИ ЧЕРЕЗ USED
# ============================================================

numbers = [1, 2, 3]

current = []
used = [False] * len(numbers)

def generate_permutations():
    if len(current) == len(numbers):
        print(current)
        return

    for i in range(len(numbers)):
        if not used[i]:
            used[i] = True
            current.append(numbers[i])

            generate_permutations()

            current.pop()
            used[i] = False


generate_permutations()


# ============================================================
# БЛОК 4. СОХРАНЕНИЕ ВСЕХ РЕШЕНИЙ
# ============================================================

current = []
used = [False] * len(numbers)
answers = []

def save_permutations():
    if len(current) == len(numbers):
        answers.append(current.copy())
        return

    for i in range(len(numbers)):
        if not used[i]:
            used[i] = True
            current.append(numbers[i])

            save_permutations()

            current.pop()
            used[i] = False


save_permutations()

print(answers)


# ============================================================
# БЛОК 5. ПОИСК ПЕРВОГО РЕШЕНИЯ
# ============================================================

numbers = [3, 5, 7, 9]
target = 12

selected = []

def search(index, total):
    if total == target:
        return True

    if index == len(numbers) or total > target:
        return False

    selected.append(numbers[index])

    if search(index + 1, total + numbers[index]):
        return True

    selected.pop()

    if search(index + 1, total):
        return True

    return False


if search(0, 0):
    print(selected)
else:
    print('Решение не найдено')


# ============================================================
# БЛОК 6. ВСЕ НАБОРЫ С ЗАДАННОЙ СУММОЙ
# ============================================================

numbers = [2, 3, 5, 7]
target = 10

selected = []
answers = []

def find_all(index, total):
    if total == target:
        answers.append(selected.copy())
        return

    if index == len(numbers) or total > target:
        return

    selected.append(numbers[index])
    find_all(index + 1, total + numbers[index])
    selected.pop()

    find_all(index + 1, total)


find_all(0, 0)

print(answers)


# ============================================================
# БЛОК 7. ПОДСЧЁТ КОЛИЧЕСТВА РЕШЕНИЙ
# ============================================================

n = 5

def count_sequences(sequence):
    if len(sequence) == n:
        return 1

    count = count_sequences(sequence + '0')

    if not sequence or sequence[-1] != '1':
        count += count_sequences(sequence + '1')

    return count


print(count_sequences(''))


# ============================================================
# БЛОК 8. ДАННЫЕ ИЗ ФАЙЛА
# ============================================================

# Формат файла data.txt:
# первая строка — количество чисел и целевая сумма;
# вторая строка — положительные числа.
#
# with open('data.txt') as f:
#     n, target = map(int, f.readline().split())
#     numbers = list(map(int, f.readline().split()))
#
# selected = []
#
# def search(index, total):
#     if total == target:
#         return True
#
#     if index == len(numbers) or total > target:
#         return False
#
#     selected.append(numbers[index])
#
#     if search(index + 1, total + numbers[index]):
#         return True
#
#     selected.pop()
#
#     return search(index + 1, total)
#
#
# if search(0, 0):
#     print(selected)
# else:
#     print('Решение не найдено')
