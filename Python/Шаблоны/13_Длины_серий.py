# Длины серий

# Серия — непрерывная последовательность элементов, удовлетворяющих условию.
# Например: максимальное количество положительных чисел подряд.

numbers = [1, 2, -3, 4, 5, 6, -1, 7, 8]

# 1. Максимальная длина серии положительных чисел
current = 0
maximum = 0

for number in numbers:
    if number > 0:
        current += 1
        maximum = max(maximum, current)
    else:
        current = 0

print(maximum)  # 3

# current — длина текущей серии.
# maximum — самая длинная серия, найденная к этому моменту.

# 2. Максимальная серия чётных чисел
current = 0
maximum = 0

for number in numbers:
    if number % 2 == 0:
        current += 1
        maximum = max(maximum, current)
    else:
        current = 0

print(maximum)

# 3. Количество серий
numbers = [2, 4, 1, 6, 8, 3, 10]

series_count = 0
inside_series = False

for number in numbers:
    if number % 2 == 0:
        if not inside_series:
            series_count += 1
            inside_series = True
    else:
        inside_series = False

print(series_count)  # 3

# 4. Длина серии одинаковых соседних элементов
numbers = [5, 5, 5, 2, 2, 7, 7, 7, 7, 1]

current = 1
maximum = 1

for i in range(1, len(numbers)):
    if numbers[i] == numbers[i - 1]:
        current += 1
        maximum = max(maximum, current)
    else:
        current = 1

print(maximum)  # 4

# 5. Самая длинная серия одинаковых символов в строке
text = 'AAABBCCCCDAA'

current = 1
maximum = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        current += 1
        maximum = max(maximum, current)
    else:
        current = 1

print(maximum)  # 4

# 6. Самая длинная серия символов, удовлетворяющих условию
text = 'AA12BBB3456CC'

current = 0
maximum = 0

for symbol in text:
    if symbol.isdigit():
        current += 1
        maximum = max(maximum, current)
    else:
        current = 0

print(maximum)  # 4

# 7. Запомнить не только длину, но и конец самой длинной серии
text = 'ABBCCCCDDA'

current = 1
maximum = 1
end_index = 0

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        current += 1
    else:
        current = 1

    if current > maximum:
        maximum = current
        end_index = i

start_index = end_index - maximum + 1
print(text[start_index:end_index + 1])  # CCCC

# Частые ошибки:
# 1. Не сбрасывать current в 0 или 1 после разрыва серии.
# 2. Обновлять maximum только после окончания серии и забыть про серию в конце списка.
# 3. Путать количество подходящих элементов вообще и длину серии подряд.
# 4. Для одинаковых элементов начинать current с 0 вместо 1.

# Универсальный шаблон по условию:
# current = 0
# maximum = 0
#
# for element in sequence:
#     if условие:
#         current += 1
#         maximum = max(maximum, current)
#     else:
#         current = 0
