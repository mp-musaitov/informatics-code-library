# collections: практическая шпаргалка
# Независимые блоки: копируйте нужный вместе с импортами и данными.

# БЛОК 1. Частоты оценок
from collections import Counter

marks = [5, 4, 5, 3, 4, 5]
counts = Counter(marks)
print(counts[5])  # 3
print(counts[2])  # 0
print(len(counts))  # 3 разные оценки

# БЛОК 2. Два самых частых символа
from collections import Counter

counts = Counter('АБАВБА')
print(counts.most_common(2))  # [('А', 3), ('Б', 2)]

# БЛОК 3. Элементы, встретившиеся один раз
from collections import Counter

numbers = [4, 2, 4, 7, 2, 9]
counts = Counter(numbers)
unique = []
for number, count in counts.items():
    if count == 1:
        unique.append(number)
print(sorted(unique))  # [7, 9]

# БЛОК 4. Одинаковый набор букв
from collections import Counter

first = 'ток'
second = 'кот'
print(Counter(first) == Counter(second))  # True

# БЛОК 5. Группировка по остатку
from collections import defaultdict

numbers = [4, 7, 6, 2, 5]
groups = defaultdict(list)
for number in numbers:
    groups[number % 3].append(number)
print(groups[1])  # [4, 7]
print(groups[0])  # [6]

# БЛОК 6. Очередь заявок
from collections import deque

queue = deque(['Адам', 'Амина'])
queue.append('Муса')
while queue:
    print(queue.popleft())
# Адам, Амина, Муса — каждый с новой строки
queue.appendleft('Первый')
print(queue.pop())  # Первый

# Частые ошибки
# 1. Путать число разных ключей len(counter) с суммой частот.
# 2. Ожидать алфавитный порядок при равных частотах в most_common.
# 3. Писать defaultdict(list()) вместо defaultdict(list).
# 4. Удалять элемент из пустой очереди.
# 5. Считать, что сравнение Counter игнорирует регистр или пробелы: сначала нужно обработать строки.
