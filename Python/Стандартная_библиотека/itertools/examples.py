# itertools: практическая шпаргалка
# Независимые блоки: копируйте нужный вместе с импортами и данными.
# Для работы используйте solution.py в отдельной папке.
# Запуск этого файла: python -I itertools.py (подробнее в README).

# БЛОК 1. Все двубуквенные слова
from itertools import product

for letters in product('АБ', repeat=2):
    print(''.join(letters))
# АА, АБ, БА, ББ — каждое слово с новой строки

# БЛОК 2. Слова с одной буквой А
from itertools import product

count = 0
for letters in product('АБВ', repeat=3):
    word = ''.join(letters)
    if word.count('А') == 1:
        count += 1
print(count)  # 12

# БЛОК 3. Номер слова
from itertools import product

for number, letters in enumerate(product('АБВ', repeat=3), start=1):
    if ''.join(letters) == 'БАВ':
        print(number)  # 12
        break

# БЛОК 4. Перестановки без повторения позиций
from itertools import permutations

words = []
for letters in permutations('АБВ', 2):
    words.append(''.join(letters))
print(words)  # ['АБ', 'АВ', 'БА', 'БВ', 'ВА', 'ВБ']

# БЛОК 5. Пары с чётной суммой
from itertools import combinations

numbers = [1, 2, 3, 4]
count = 0
for a, b in combinations(numbers, 2):
    if (a + b) % 2 == 0:
        count += 1
print(count)  # 2

# БЛОК 6. Таблица истинности
from itertools import product

for x, y in product([0, 1], repeat=2):
    result = x and not y
    print(x, y, int(result))
# 0 0 0
# 0 1 0
# 1 0 1
# 1 1 0

# Частые ошибки
# 1. Путать перестановки с сочетаниями: пары AB и BA различны только при важном порядке.
# 2. Считать, что одинаковые значения автоматически удаляются: в permutations('ААБ') возможны одинаковые слова, потому что выбираются позиции.
# 3. Считать элементы результата строками: для слова нужен join.
# 4. Создавать список всех длинных слов вместо подсчёта в цикле.
# 5. Забывать запрет ведущего нуля при составлении чисел.
