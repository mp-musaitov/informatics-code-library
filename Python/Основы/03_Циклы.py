# Циклы в Python

# Цикл for — когда заранее известно, сколько раз повторять действие
for i in range(5):
    print(i)
# 0 1 2 3 4

# range(start, stop)
for i in range(2, 6):
    print(i)
# 2 3 4 5

# range(start, stop, step)
for i in range(10, 0, -2):
    print(i)
# 10 8 6 4 2

# Перебор строки
text = 'python'
for symbol in text:
    print(symbol)

# Перебор списка
numbers = [4, 7, 2, 9]
for x in numbers:
    print(x)

# Сумма элементов
numbers = [4, 7, 2, 9]
total = 0
for x in numbers:
    total += x
print(total)

# Подсчёт количества элементов по условию
numbers = [4, 7, 2, 9, 12, 15]
count = 0
for x in numbers:
    if x % 2 == 0:
        count += 1
print(count)

# Поиск максимума без max()
numbers = [4, 7, 2, 9]
maximum = numbers[0]
for x in numbers:
    if x > maximum:
        maximum = x
print(maximum)

# Цикл while — когда заранее неизвестно, сколько повторений понадобится
x = 1
while x <= 5:
    print(x)
    x += 1

# break — досрочно завершить цикл
for i in range(10):
    if i == 5:
        break
    print(i)

# continue — пропустить текущую итерацию
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Вложенные циклы
for i in range(3):
    for j in range(2):
        print(i, j)

# Частые ошибки
# 1. range(5) даёт числа от 0 до 4, а не от 1 до 5.
# 2. Правая граница range() не включается.
# 3. В while нужно следить, чтобы условие когда-нибудь стало ложным.
# 4. Не забывай менять переменную цикла в while, иначе цикл может стать бесконечным.
# 5. break завершает ближайший цикл, continue пропускает одну итерацию.

# Универсальные шаблоны
# Сумма:
# total = 0
# for x in numbers:
#     total += x

# Счётчик:
# count = 0
# for x in numbers:
#     if условие:
#         count += 1
