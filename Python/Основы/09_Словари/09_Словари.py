# Словари в Python
# Независимые практические блоки: копируйте нужный вместе с его данными.

# БЛОК 1. Создание, добавление и изменение
scores = {'Адам': 85}
scores['Амина'] = 92
scores['Адам'] = 90
print(scores)  # {'Адам': 90, 'Амина': 92}
print(len(scores))  # 2

# БЛОК 2. Безопасное получение значения
scores = {'Адам': 85, 'Амина': 92}
if 'Адам' in scores:
    print(scores['Адам'])  # 85
print(scores.get('Муса', 0))  # 0
print('Муса' in scores)  # False — get() не добавил ключ
print(85 in scores.values())  # True

# БЛОК 3. Ключи, значения и пары
scores = {'Адам': 85, 'Амина': 92}
for name in scores:
    print(name)
for score in scores.values():
    print(score)
for name, score in scores.items():
    print(name, score)

# БЛОК 4. Вывод по алфавиту
scores = {'Муса': 78, 'Адам': 85, 'Амина': 92}
for name in sorted(scores):
    print(name, scores[name])

# БЛОК 5. Частоты чисел
numbers = [5, 2, 5, 3, 2, 5]
counts = {}
for x in numbers:
    counts[x] = counts.get(x, 0) + 1
print(counts)  # {5: 3, 2: 2, 3: 1}
print(counts.get(7, 0))  # 0

# БЛОК 6. Частоты символов
text = 'мама'
counts = {}
for char in text:
    counts[char] = counts.get(char, 0) + 1
print(counts)  # {'м': 2, 'а': 2}

# БЛОК 7. Частоты слов
# В примере слова уже записаны в нижнем регистре без знаков препинания.
text = 'кот и пёс и кот'
counts = {}
for word in text.split():
    counts[word] = counts.get(word, 0) + 1
print(counts)  # {'кот': 2, 'и': 2, 'пёс': 1}

# БЛОК 8. Удаление
scores = {'Адам': 85, 'Амина': 92}
del scores['Адам']
score = scores.pop('Амина')
print(score)  # 92
print(scores.pop('Муса', 0))  # 0 — ключ может отсутствовать
print(scores)  # {}

# БЛОК 9. Копирование словаря с числами
scores = {'Адам': 85}
copy_scores = scores.copy()
copy_scores['Адам'] = 90
print(scores)       # {'Адам': 85}
print(copy_scores)  # {'Адам': 90}

# Частые ошибки
# 1. d[key] требует существующего ключа при чтении.
# 2. key in d проверяет ключи, а не значения.
# 3. Повторная запись по ключу заменяет значение.
# 4. Не добавляйте и не удаляйте ключи при переборе самого словаря.
# 5. copy_scores = scores не создаёт копию.

# Универсальные шаблоны
# counts = {}
# for x in numbers:
#     counts[x] = counts.get(x, 0) + 1
#
# for key, value in counts.items():
#     print(key, value)
