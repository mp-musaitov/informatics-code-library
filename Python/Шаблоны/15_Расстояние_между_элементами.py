# Расстояние между элементами

# Этот шаблон полезен для задач, где важны позиции элементов:
# «не менее K позиций между ними», «минимальное расстояние»,
# «максимальное расстояние», а также для строковых задач.

numbers = [5, 12, 7, 20, 3, 18, 9]

# 1. Расстояние между элементами по индексам
# Для элементов с индексами i и j расстояние по индексам: j - i.
i = 1
j = 5
print(j - i)  # 4

# Если нужно количество элементов МЕЖДУ ними:
print(j - i - 1)  # 3

# Это важное различие!

# 2. Перебрать пары, между которыми не менее K позиций
k = 3

for i in range(len(numbers)):
    for j in range(i + k, len(numbers)):
        print(numbers[i], numbers[j])

# Здесь j - i >= k.

# 3. Посчитать пары с расстоянием не менее K и условием на значения
k = 3
count = 0

for i in range(len(numbers)):
    for j in range(i + k, len(numbers)):
        if numbers[i] + numbers[j] > 25:
            count += 1

print(count)

# 4. Максимальная сумма пары при ограничении на расстояние
maximum = None

for i in range(len(numbers)):
    for j in range(i + k, len(numbers)):
        pair_sum = numbers[i] + numbers[j]

        if maximum is None or pair_sum > maximum:
            maximum = pair_sum

print(maximum)

# 5. Минимальное расстояние между двумя заданными значениями
numbers = [7, 2, 5, 7, 9, 2, 4]

positions_7 = []
positions_2 = []

for i in range(len(numbers)):
    if numbers[i] == 7:
        positions_7.append(i)
    if numbers[i] == 2:
        positions_2.append(i)

minimum = None

for i in positions_7:
    for j in positions_2:
        distance = abs(i - j)

        if minimum is None or distance < minimum:
            minimum = distance

print(minimum)

# 6. Максимальное расстояние между одинаковыми элементами
numbers = [5, 1, 7, 5, 3, 5]

positions = []
for i in range(len(numbers)):
    if numbers[i] == 5:
        positions.append(i)

if len(positions) >= 2:
    print(positions[-1] - positions[0])  # 5

# 7. Расстояние между символами в строке
text = 'AxxBxxxAxxB'

positions_a = []
positions_b = []

for i in range(len(text)):
    if text[i] == 'A':
        positions_a.append(i)
    if text[i] == 'B':
        positions_b.append(i)

minimum = None

for i in positions_a:
    for j in positions_b:
        distance = abs(i - j)

        if minimum is None or distance < minimum:
            minimum = distance

print(minimum)

# 8. Количество символов МЕЖДУ двумя позициями
text = 'A123B'
i = text.index('A')
j = text.index('B')

between = j - i - 1
print(between)  # 3

# 9. Найти максимальный фрагмент между двумя одинаковыми символами
text = 'A12A34567A9'
positions = []

for i in range(len(text)):
    if text[i] == 'A':
        positions.append(i)

maximum = 0

for i in range(len(positions)):
    for j in range(i + 1, len(positions)):
        length_between = positions[j] - positions[i] - 1
        maximum = max(maximum, length_between)

print(maximum)

# 10. Частый шаблон для задач со строками:
# расстояние между двумя вхождениями заданного символа

text = 'XABCXXDEFX'
positions = []

for i in range(len(text)):
    if text[i] == 'X':
        positions.append(i)

for i in range(len(positions) - 1):
    distance = positions[i + 1] - positions[i]
    print(distance)

# Частые ошибки:
# 1. Путать расстояние j - i и количество элементов между ними j - i - 1.
# 2. Использовать range(i + k + 1, ...), когда условие требует j - i >= k.
# 3. Забыть abs(), если порядок двух позиций заранее неизвестен.
# 4. Путать расстояние между индексами и длину подстроки между символами.
# 5. Применять полный перебор O(n^2) к огромной последовательности без необходимости.

# Универсальный шаблон «не менее K позиций»:
# for i in range(len(sequence)):
#     for j in range(i + k, len(sequence)):
#         if условие:
#             ...

# Универсальный шаблон для строки:
# positions = []
# for i in range(len(text)):
#     if text[i] == нужный_символ:
#         positions.append(i)
