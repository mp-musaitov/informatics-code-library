# Генераторы списков в Python
# Независимые практические блоки: копируйте нужный вместе с его данными.
# Примеры можно запускать целиком; шаблон ввода оставлен в комментарии.

# БЛОК 1. Квадраты чисел
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# БЛОК 2. Та же задача через обычный цикл
squares = []
for x in range(1, 6):
    squares.append(x ** 2)
print(squares)  # [1, 4, 9, 16, 25]

# БЛОК 3. Отбор чётных чисел
numbers = [-3, 0, 4, 7, 10]
even = [x for x in numbers if x % 2 == 0]
print(even)  # [0, 4, 10]

# БЛОК 4. Отбор и преобразование
numbers = [-3, 0, 4, 7, 10]
squares = [x ** 2 for x in numbers if x > 0]
print(squares)  # [16, 49, 100]

# БЛОК 5. Числа из строки
line = '12 -5 0 8'
numbers = [int(x) for x in line.split()]
print(numbers)  # [12, -5, 0, 8]
# Для ввода с клавиатуры:
# numbers = [int(x) for x in input().split()]

# БЛОК 6. Длины слов
words = ['кот', 'информатика', 'код']
lengths = [len(word) for word in words]
print(lengths)  # [3, 11, 3]

# БЛОК 7. Заменить отрицательные числа нулями
numbers = [-3, 0, 4, -1]
result = [x if x >= 0 else 0 for x in numbers]
print(result)   # [0, 0, 4, 0]
print(numbers)  # [-3, 0, 4, -1] — исходный список не изменился

# БЛОК 8. Максимум среди подходящих
numbers = [-3, 0, -1]
positive = [x for x in numbers if x > 0]
if positive:
    print(max(positive))
else:
    print('Подходящих чисел нет')

# БЛОК 9. Таблица с независимыми строками
rows = 2
cols = 3
matrix = [[0] * cols for i in range(rows)]
matrix[0][0] = 5
print(matrix)  # [[5, 0, 0], [0, 0, 0]]

# Частые ошибки
# 1. Фильтр пишется после for, выбор if/else — перед for.
# 2. Генератор списка создаёт новый список.
# 3. После фильтрации список может оказаться пустым.
# 4. [[0] * cols] * rows повторяет ссылку на одну строку.

# Универсальные шаблоны
# result = [выражение for x in numbers]
# result = [x for x in numbers if условие]
# result = [значение_1 if условие else значение_2 for x in numbers]
