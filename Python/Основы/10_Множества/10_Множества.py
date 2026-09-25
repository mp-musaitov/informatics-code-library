# Множества в Python
# Независимые практические блоки: копируйте нужный вместе с его данными.
# Для предсказуемого порядка вывода используется sorted().

# БЛОК 1. Создание и проверка наличия
numbers = set()
numbers.add(4)
numbers.add(4)
print(len(numbers))  # 1
print(4 in numbers)  # True
print(5 not in numbers)  # True

# БЛОК 2. Различные числа
numbers = [5, 2, 5, 3, 2]
unique = set(numbers)
print(len(unique))     # 3
print(sorted(unique))  # [2, 3, 5]

# БЛОК 3. Различные символы
text = 'мама'
letters = set(text)
print(len(letters))     # 2
print(sorted(letters))  # ['а', 'м']

# БЛОК 4. Добавление и удаление
numbers = {2, 4}
numbers.add(6)
numbers.update([8, 10])
numbers.remove(2)  # значение точно есть
numbers.discard(100)  # ошибки нет, даже если значения нет
print(sorted(numbers))  # [4, 6, 8, 10]

# БЛОК 5. Операции над множествами
a = {1, 2, 3}
b = {3, 4}
print(sorted(a | b))  # [1, 2, 3, 4] — объединение
print(sorted(a & b))  # [3] — пересечение
print(sorted(a - b))  # [1, 2] — разность
print(sorted(b - a))  # [4] — обратная разность
print(sorted(a ^ b))  # [1, 2, 4] — ровно в одном множестве

# БЛОК 6. Все ли нужные символы присутствуют
required = {'a', 'b'}
letters = set('abac')
print(required <= letters)  # True

# БЛОК 7. Общие значения двух списков
first = [2, 5, 2, 7]
second = [5, 5, 8, 7]
common = set(first) & set(second)
print(len(common))     # 2
print(sorted(common))  # [5, 7]

# БЛОК 8. Есть ли повторы
numbers = [2, 5, 2, 7]
has_duplicates = len(set(numbers)) < len(numbers)
print(has_duplicates)  # True

# Проверка, все ли элементы различны
all_unique = len(set(numbers)) == len(numbers)
print(all_unique)  # False

# БЛОК 9. Перебор по возрастанию
numbers = {6, 2, 4}
for x in sorted(numbers):
    print(x)  # 2, затем 4, затем 6

# Частые ошибки
# 1. {} — словарь, set() — пустое множество.
# 2. У множества нет индексов, срезов и метода append().
# 3. Множество не сохраняет порядок исходного списка и повторы.
# 4. remove() требует наличия элемента; discard() — нет.
# 5. Не меняйте размер множества при его переборе.
# 6. Для пересечения и объединения нужны & и |, а не and и or.

# Универсальные шаблоны
# unique = set(numbers)
# common = set(first) & set(second)
# only_first = set(first) - set(second)
# ordered = sorted(unique)  # результат — список
