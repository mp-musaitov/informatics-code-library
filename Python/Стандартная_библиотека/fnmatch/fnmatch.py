# fnmatch: практическая шпаргалка
# Независимые блоки: копируйте нужный вместе с импортами и данными.
# Для работы используйте solution.py в отдельной папке.
# Запуск этого файла: python -I fnmatch.py (подробнее в README).

# БЛОК 1. Один обязательный символ
from fnmatch import fnmatchcase

print(fnmatchcase('1235', '12?5'))  # True
print(fnmatchcase('125', '12?5'))   # False

# БЛОК 2. Звёздочка может быть пустой
from fnmatch import fnmatchcase

print(fnmatchcase('125', '12*5'))    # True
print(fnmatchcase('12005', '12*5'))  # True

# БЛОК 3. Перебор кратных по маске
from fnmatch import fnmatchcase

# Положительные числа не больше 2000, кратные 25.
for number in range(25, 2000 + 1, 25):
    if fnmatchcase(str(number), '12?5'):
        print(number, number // 25)
# 1225 49
# 1275 51

# БЛОК 4. Выбор файлов с учётом регистра
from fnmatch import fnmatchcase

names = ['task.txt', 'photo.png', 'DATA.TXT', 'notes.txt']
selected = [name for name in names if fnmatchcase(name, '*.txt')]
print(selected)  # ['task.txt', 'notes.txt']

# БЛОК 5. Набор допустимых цифр
from fnmatch import fnmatchcase

for text in ['120', '130', '140', '150']:
    if fnmatchcase(text, '1[35]0'):
        print(text)
# 130, затем 150

# БЛОК 6. Обычная проверка и отбор списка
from fnmatch import fnmatch, filter

# Имена в одном регистре: результат одинаков в Windows и Linux.
names = ['a.txt', 'b.csv', 'c.txt']
print(fnmatch('a.txt', '*.txt'))  # True
print(filter(names, '*.txt'))  # ['a.txt', 'c.txt']

# Частые ошибки
# 1. Передавать число вместо строки.
# 2. Считать, что * обязательно заменяет хотя бы один символ.
# 3. Ожидать от ? только цифру при проверке произвольного текста.
# 4. Путать шаблоны re и fnmatch.
# 5. Перебирать все числа до огромной границы, не используя делимость и ограничения длины.
