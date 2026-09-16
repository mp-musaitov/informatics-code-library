# ============================================================
# БЛОК 1. ОСНОВЫ СЛОВАРЯ
# ============================================================

scores = {
    'Антон': 91,
    'Борис': 84
}

scores['Вера'] = 78
scores['Борис'] = 87

print(scores)
print(scores['Антон'])


# ============================================================
# БЛОК 2. ПРОВЕРКА КЛЮЧА И МЕТОД GET()
# ============================================================

if 'Вера' in scores:
    print(scores['Вера'])

print(scores.get('Галина'))
print(scores.get('Галина', 0))


# ============================================================
# БЛОК 3. ПОДСЧЁТ ЧАСТОТ ЧЕРЕЗ IF
# ============================================================

numbers = [3, 5, 3, 2, 5, 3]

frequency = {}

for x in numbers:
    if x in frequency:
        frequency[x] += 1
    else:
        frequency[x] = 1

print(frequency)


# ============================================================
# БЛОК 4. ПОДСЧЁТ ЧАСТОТ ЧЕРЕЗ GET()
# ============================================================

numbers = [3, 5, 3, 2, 5, 3]

frequency = {}

for x in numbers:
    frequency[x] = frequency.get(x, 0) + 1

print(frequency)


# ============================================================
# БЛОК 5. ЧАСТОТЫ СИМВОЛОВ
# ============================================================

text = 'мама мыла раму'

frequency = {}

for symbol in text:
    if symbol != ' ':
        frequency[symbol] = frequency.get(symbol, 0) + 1

print(frequency)


# ============================================================
# БЛОК 6. ЧАСТОТЫ СЛОВ
# ============================================================

text = 'кот пёс кот лиса пёс кот'

words = text.lower().split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)


# ============================================================
# БЛОК 7. САМЫЙ ЧАСТЫЙ ЭЛЕМЕНТ
# ============================================================

numbers = [3, 5, 3, 2, 5, 3]

frequency = {}

for x in numbers:
    frequency[x] = frequency.get(x, 0) + 1

if frequency:
    most_frequent = max(frequency, key=frequency.get)

    print(most_frequent)
    print(frequency[most_frequent])


# ============================================================
# БЛОК 8. ВСЕ ЭЛЕМЕНТЫ С МАКСИМАЛЬНОЙ ЧАСТОТОЙ
# ============================================================

numbers = [4, 2, 4, 3, 2, 5]

frequency = {}

for x in numbers:
    frequency[x] = frequency.get(x, 0) + 1

maximum = max(frequency.values())

most_frequent = []

for x, count in frequency.items():
    if count == maximum:
        most_frequent.append(x)

print(most_frequent)


# ============================================================
# БЛОК 9. ТАБЛИЦА ЧАСТОТ
# ============================================================

frequency = {
    3: 3,
    5: 2,
    2: 1
}

for x in sorted(frequency):
    print(x, frequency[x])


# ============================================================
# БЛОК 10. ПОДСЧЁТ ЧАСТОТ В ФАЙЛЕ
# ============================================================

# В каждой строке файла data.txt записано одно число.
#
# frequency = {}
#
# with open('data.txt') as f:
#     for s in f:
#         x = int(s)
#         frequency[x] = frequency.get(x, 0) + 1
#
# print(frequency)


# ============================================================
# БЛОК 11. COUNTER — ГОТОВЫЙ ПОДСЧЁТ ЧАСТОТ
# ============================================================

from collections import Counter

numbers = [3, 5, 3, 2, 5, 3]

frequency = Counter(numbers)

print(frequency)
print(frequency.most_common(2))
