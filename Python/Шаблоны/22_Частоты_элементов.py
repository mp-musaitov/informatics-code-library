# Частоты элементов

# Частота элемента — сколько раз он встречается в последовательности.
# Для этого чаще всего используют словарь.

# ------------------------------------------------------------
# 1. Понятный подсчёт через обычный словарь
numbers = [5, 2, 5, 7, 2, 5, 9]
frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

print(frequency)  # {5: 3, 2: 2, 7: 1, 9: 1}

# ------------------------------------------------------------
# 2. Короткий вариант через get()
numbers = [5, 2, 5, 7, 2, 5, 9]
frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

print(frequency)

# get(number, 0) означает:
# если ключ уже есть — взять его значение,
# если ключа нет — считать, что его частота пока равна 0.

# ------------------------------------------------------------
# 3. Частоты символов строки
text = 'информатика'
frequency = {}

for symbol in text:
    frequency[symbol] = frequency.get(symbol, 0) + 1

print(frequency)

# ------------------------------------------------------------
# 4. Найти самый частый элемент
numbers = [5, 2, 5, 7, 2, 5, 9]
frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

most_common = max(frequency, key=frequency.get)
print(most_common)             # 5
print(frequency[most_common])  # 3

# ------------------------------------------------------------
# 5. Вывести элементы и их частоты
for element, count in frequency.items():
    print(element, count)

# ------------------------------------------------------------
# 6. Найти элементы, встретившиеся ровно один раз
numbers = [5, 2, 5, 7, 2, 5, 9]
frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

for number in numbers:
    if frequency[number] == 1:
        print(number)

# Будут выведены 7 и 9.

# ------------------------------------------------------------
# 7. Найти все элементы максимальной частоты
numbers = [1, 2, 2, 3, 3, 4]
frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

maximum_frequency = max(frequency.values())

result = []
for element, count in frequency.items():
    if count == maximum_frequency:
        result.append(element)

print(result)  # [2, 3]

# ------------------------------------------------------------
# 8. Частоты через Counter
from collections import Counter

numbers = [5, 2, 5, 7, 2, 5, 9]
frequency = Counter(numbers)

print(frequency)
print(frequency[5])  # 3

# Counter удобен, когда нужно быстро считать частоты,
# но базовый словарь важно уметь писать самостоятельно.

# ------------------------------------------------------------
# 9. Самые частые элементы через Counter
frequency = Counter(numbers)
print(frequency.most_common(2))
# Например: [(5, 3), (2, 2)]

# ------------------------------------------------------------
# 10. Частоты слов
text = 'кот пёс кот птица пёс кот'
words = text.split()

frequency = {}
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)

# ------------------------------------------------------------
# Частые ошибки

# 1. Пытаться увеличить frequency[element], когда такого ключа ещё нет.
# 2. Путать ключ словаря и его значение.
# 3. Использовать max(frequency) и ожидать самый частый элемент.
#    max(frequency) сравнивает сами ключи.
# 4. Забыть, что frequency.items() даёт пары (ключ, значение).
# 5. Использовать list.count() в большом цикле вместо одного словаря частот.

# ------------------------------------------------------------
# Универсальный шаблон

# frequency = {}
# for element in data:
#     frequency[element] = frequency.get(element, 0) + 1
#
# for element, count in frequency.items():
#     print(element, count)
