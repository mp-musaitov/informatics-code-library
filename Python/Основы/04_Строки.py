# Строки в Python

# Строка — последовательность символов
text = 'Python'

# 1. Длина строки
print(len(text))  # 6

# 2. Индексы
# Индексация начинается с 0
print(text[0])   # P
print(text[1])   # y
print(text[-1])  # n — последний символ
print(text[-2])  # o — предпоследний символ

# 3. Срезы
print(text[1:4])   # yth
print(text[:3])    # Pyt
print(text[3:])    # hon
print(text[::2])   # Pto
print(text[::-1])  # nohtyP — строка наоборот

# Правая граница среза не включается.

# 4. Перебор символов строки
for symbol in text:
    print(symbol)

# Перебор по индексам
for i in range(len(text)):
    print(i, text[i])

# 5. Проверка наличия подстроки
text = 'информатика'

if 'форма' in text:
    print('Подстрока найдена')

if 'python' not in text:
    print('Такой подстроки нет')

# 6. Основные методы строк
text = '  Python для ЕГЭ  '

print(text.lower())      # перевод в нижний регистр
print(text.upper())      # перевод в верхний регистр
print(text.strip())      # убрать пробелы по краям
print(text.replace('Python', 'Питон'))

# Методы строк не изменяют исходную строку — они возвращают новую.

# 7. count() — количество вхождений
text = 'абракадабра'
print(text.count('а'))   # 5
print(text.count('бра')) # 2

# 8. find() — позиция первого вхождения
text = 'информатика'
print(text.find('форма'))  # 2
print(text.find('python')) # -1, если не найдено

# 9. startswith() и endswith()
filename = 'result.txt'

print(filename.startswith('res'))  # True
print(filename.endswith('.txt'))   # True

# 10. split() — разделить строку
text = '10 20 30 40'
parts = text.split()
print(parts)  # ['10', '20', '30', '40']

# Частый вариант: сразу получить список чисел
numbers = list(map(int, input().split()))

# 11. join() — соединить строки
words = ['ЕГЭ', 'по', 'информатике']
text = ' '.join(words)
print(text)  # ЕГЭ по информатике

# 12. Строки нельзя изменять по символам
word = 'кот'
# word[0] = 'р'  # TypeError

# Нужно создать новую строку:
word = 'р' + word[1:]
print(word)  # рот

# 13. Сравнение строк
# Строки сравниваются посимвольно.
answer = 'да'
if answer == 'да':
    print('Верно')

# 14. Полезные проверки символов
symbol = '7'
print(symbol.isdigit())  # True
print(symbol.isalpha())  # False

# Частые ошибки
# 1. Первый символ имеет индекс 0, а не 1.
# 2. Последний символ удобно получать через [-1].
# 3. Правая граница среза не включается.
# 4. Нельзя изменить отдельный символ строки: строки неизменяемы.
# 5. split() возвращает строки. Для чисел обычно нужен map(int, ...).
# 6. Методы lower(), upper(), replace(), strip() возвращают новую строку.

# Универсальные шаблоны

# Перебор символов:
# for symbol in text:
#     ...

# Перебор по индексам:
# for i in range(len(text)):
#     ...

# Подсчёт символов:
# count = 0
# for symbol in text:
#     if условие:
#         count += 1

# Строка наоборот:
# reversed_text = text[::-1]

# Ввод нескольких чисел через пробел:
# numbers = list(map(int, input().split()))
