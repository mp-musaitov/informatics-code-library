# Полезные встроенные функции в Python
# Независимые практические блоки: копируйте нужный вместе с его данными.
# Примеры можно запускать целиком; шаблон ввода оставлен в комментарии.

# БЛОК 1. Сумма и среднее арифметическое
numbers = [4, 7, 2]
print(sum(numbers))  # 13
if numbers:
    print(sum(numbers) / len(numbers))  # 4.333333333333333
else:
    print('Чисел нет')

# БЛОК 2. Минимум, максимум и размах
numbers = [4, 7, 2]
if numbers:
    print(min(numbers))  # 2
    print(max(numbers))  # 7
    print(max(numbers) - min(numbers))  # 5
else:
    print('Чисел нет')

# БЛОК 3. Максимум среди подходящих
numbers = [-3, 0, -1]
positive = [x for x in numbers if x > 0]
if positive:
    print(max(positive))
else:
    print('Подходящих чисел нет')

# БЛОК 4. Сортировка по возрастанию и убыванию
numbers = [5, 2, 5, 1]
print(sorted(numbers))                # [1, 2, 5, 5]
print(sorted(numbers, reverse=True))  # [5, 5, 2, 1]
print(numbers)                       # [5, 2, 5, 1]

# БЛОК 5. Слова по длине, самое короткое и длинное слово
words = ['кот', 'информатика', 'дом', 'я']
print(sorted(words, key=len))  # ['я', 'кот', 'дом', 'информатика']
if words:
    print(min(words, key=len))  # я
    print(max(words, key=len))  # информатика
else:
    print('Слов нет')

# БЛОК 6. Сравнение по модулю
numbers = [-8, 3, -2, 5]
print(sorted(numbers, key=abs))  # [-2, 3, 5, -8]
if numbers:
    print(min(numbers, key=abs))  # -2 — ближайшее к нулю
    print(max(numbers, key=abs))  # -8 — самое далёкое от нуля
else:
    print('Чисел нет')

# БЛОК 7. Нумерованный список
names = ['Адам', 'Амина', 'Муса']
for number, name in enumerate(names, start=1):
    print(number, name)
# 1 Адам
# 2 Амина
# 3 Муса

# БЛОК 8. Индексы отрицательных элементов
numbers = [5, -2, 0, -7]
for i, x in enumerate(numbers):
    if x < 0:
        print(i)  # 1, затем 3 — индексы начинаются с 0

# БЛОК 9. Имена и баллы из двух списков
names = ['Адам', 'Амина', 'Муса']
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(name, score)
# Адам 85
# Амина 92
# Муса 78

# БЛОК 10. Стоимость покупки по ценам и количествам
prices = [50, 30, 80]
counts = [2, 3, 1]
if len(prices) == len(counts):
    total = 0
    for price, count in zip(prices, counts):
        total += price * count
    print(total)  # 270
else:
    print('Длины списков не совпадают')

# БЛОК 11. Есть ли подходящее число и все ли подходят
numbers = [-3, 0, 4, 7]
print(any([x < 0 for x in numbers]))   # True
print(all([x > 0 for x in numbers]))   # False
print(all([x >= 0 for x in numbers]))  # False

# БЛОК 12. Пустые данные и проверка непустого списка
numbers = []
print(sum(numbers))  # 0
print(any(numbers))  # False
print(all(numbers))  # True
all_positive = len(numbers) > 0 and all([x > 0 for x in numbers])
print(all_positive)  # False — требуется хотя бы одно число

# БЛОК 13. Числа из строки через map()
line = '12 -5 0 8'
numbers = list(map(int, line.split()))
print(numbers)  # [12, -5, 0, 8]
# Для ввода с клавиатуры:
# numbers = list(map(int, input().split()))

# БЛОК 14. Длины слов через map()
words = ['кот', 'информатика', 'код']
lengths = list(map(len, words))
print(lengths)  # [3, 11, 3]

# БЛОК 15. Сумма чётных чисел
numbers = [3, 4, -2, 7, 6]
even = [x for x in numbers if x % 2 == 0]
print(sum(even))  # 8; если подходящих чисел нет, сумма равна 0

# Частые ошибки
# 1. Не называйте переменные sum, min, max, sorted или list.
# 2. min() и max() требуют непустых данных.
# 3. sorted() создаёт список; .sort() меняет список и возвращает None.
# 4. Передавайте key=len и map(int, ...), без скобок после имени функции.
# 5. Номера enumerate(..., start=1) не совпадают с индексами списка.
# 6. zip() останавливается на самом коротком списке.
# 7. all(numbers) проверяет ненулевые числа, а не положительные.
# 8. Для хранения результата map(), zip(), enumerate() используйте list().

# Универсальные шаблоны
# total = sum(numbers)
# ordered = sorted(numbers, reverse=True)
# longest = max(words, key=len)  # words не пуст
# for i, x in enumerate(numbers):
#     print(i, x)
# for a, b in zip(first, second):
#     print(a, b)
# has_negative = any([x < 0 for x in numbers])
# all_positive = all([x > 0 for x in numbers])
# numbers = list(map(int, input().split()))
