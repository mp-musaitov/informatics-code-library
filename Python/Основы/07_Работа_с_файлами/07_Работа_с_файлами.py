# Работа с файлами в Python

# В задачах по информатике данные часто находятся не в input(),
# а в текстовом файле.

# 1. Открытие файла для чтения
file = open('input.txt', 'r', encoding='utf-8')
text = file.read()
file.close()

print(text)

# 'r' — режим чтения (read).

# 2. Более удобный и безопасный способ — with
# После выхода из блока with файл закроется автоматически.
with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read()

print(text)

# 3. Чтение одной строки — readline()
with open('input.txt', 'r', encoding='utf-8') as file:
    line = file.readline()

print(line)

# 4. Чтение всех строк — readlines()
with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

print(lines)

# Важно: символ перевода строки \n обычно остаётся в конце строки.
# Его удобно убрать методом strip().

# 5. Перебор файла построчно
with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        print(line)

# Для больших файлов этот способ удобнее, чем readlines(),
# потому что не нужно сразу загружать весь файл в память.

# 6. Если в каждой строке находится одно число
with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        number = int(line)
        print(number)

# 7. Если в строке несколько чисел через пробел
# Например, строка файла: 10 20 30
with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        numbers = list(map(int, line.split()))
        print(numbers)

# 8. Считать все числа из файла в список
with open('input.txt', 'r', encoding='utf-8') as file:
    numbers = [int(line) for line in file]

print(numbers)

# 9. Частый формат задач: первая строка — количество элементов
# Например:
# 5
# 10
# 20
# 30
# 40
# 50
with open('input.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())

    numbers = []
    for _ in range(n):
        numbers.append(int(file.readline()))

print(numbers)

# 10. Запись в файл — режим 'w'
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write('Привет!')

# Внимание: режим 'w' создаёт новый файл или очищает существующий.

# 11. Запись нескольких строк
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write('Первая строка\n')
    file.write('Вторая строка\n')

# \n — символ перехода на новую строку.

# 12. Добавление данных в конец файла — режим 'a'
with open('output.txt', 'a', encoding='utf-8') as file:
    file.write('Новая строка\n')

# 'a' — append: существующее содержимое не удаляется.

# 13. Запись числа
number = 100
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(str(number))

# write() принимает строку, поэтому число преобразуем через str().

# 14. Пример: найти максимальное число в файле
with open('input.txt', 'r', encoding='utf-8') as file:
    numbers = [int(line) for line in file]

maximum = max(numbers)
print(maximum)

# 15. Пример: посчитать числа, удовлетворяющие условию
count = 0

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        number = int(line)
        if number % 2 == 0:
            count += 1

print(count)

# 16. Очень частый шаблон для задач ЕГЭ
count = 0
maximum = None

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        number = int(line)

        if number % 2 == 0:  # здесь нужное условие задачи
            count += 1

            if maximum is None or number > maximum:
                maximum = number

print(count, maximum)

# Частые ошибки
# 1. Неправильный путь или имя файла -> FileNotFoundError.
# 2. Забыть, что readline() возвращает строку.
# 3. Забыть int(), если нужны числа.
# 4. Забыть strip(), когда мешает символ \n.
# 5. Открыть существующий файл в режиме 'w' и случайно стереть его.
# 6. Передать число напрямую в write(): нужен str(number).
# 7. Забыть закрыть файл при обычном open(). С with это делается автоматически.

# Универсальные шаблоны

# Прочитать файл построчно:
# with open('input.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         ...

# Прочитать числа в список:
# with open('input.txt', 'r', encoding='utf-8') as file:
#     numbers = [int(line) for line in file]

# Обработать числа без хранения всего списка:
# with open('input.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         number = int(line)
#         if условие:
#             ...

# Записать результат:
# with open('output.txt', 'w', encoding='utf-8') as file:
#     file.write(str(result))
