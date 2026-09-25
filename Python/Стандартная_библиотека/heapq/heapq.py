# heapq: практическая шпаргалка
# Независимые блоки: копируйте нужный вместе с импортами и данными.
# Для работы используйте solution.py в отдельной папке.
# Запуск этого файла: python -I heapq.py (подробнее в README).

# БЛОК 1. Построение кучи и минимум
from heapq import heapify

heap = [7, 2, 9, 4]
heapify(heap)
print(heap[0])  # 2

# БЛОК 2. Добавление и извлечение
from heapq import heappush, heappop

heap = []
for number in [7, 2, 9]:
    heappush(heap, number)
print(heappop(heap))  # 2
heappush(heap, 1)
print(heappop(heap))  # 1

# БЛОК 3. Извлечение всех значений
from heapq import heapify, heappop

heap = [5, 1, 5, 3]
heapify(heap)
result = []
while heap:
    result.append(heappop(heap))
print(result)  # [1, 3, 5, 5]

# БЛОК 4. Несколько наименьших и наибольших
from heapq import nsmallest, nlargest

scores = [7, 2, 9, 4, 9]
print(nsmallest(3, scores))  # [2, 4, 7]
print(nlargest(2, scores))   # [9, 9]

# БЛОК 5. Сначала короткая заявка
from heapq import heapify, heappop

# Пара содержит длительность и имя.
# При равной длительности имена сравниваются как строки.
heap = [(5, 'Муса'), (2, 'Адам'), (3, 'Амина')]
heapify(heap)
while heap:
    duration, name = heappop(heap)
    print(name, duration)
# Адам 2
# Амина 3
# Муса 5

# БЛОК 6. Объединение двух самых коротких отрезков
from heapq import heapify, heappop, heappush

heap = [2, 3, 7]
heapify(heap)
total = 0
while len(heap) > 1:
    first = heappop(heap)
    second = heappop(heap)
    joined = first + second
    total += joined
    heappush(heap, joined)
print(total)  # 17: сначала 2 + 3 = 5, затем 5 + 7 = 12

# Частые ошибки
# 1. Считать, что весь список после heapify отсортирован.
# 2. Писать heap = heapify(numbers) и получать None.
# 3. Вызывать heappop для пустой кучи.
# 4. Добавлять через append после построения кучи.
# 5. Ожидать, что nlargest удалит выбранные элементы из исходного списка.
