# Списки в Python

# Список — изменяемая коллекция элементов
numbers = [10, 20, 30, 40]

# 1. Доступ по индексу
print(numbers[0])   # 10
print(numbers[-1])  # 40

# 2. Изменение элемента
numbers[1] = 25
print(numbers)  # [10, 25, 30, 40]

# 3. Длина списка
print(len(numbers))

# 4. Добавление элемента в конец — append()
numbers.append(50)
print(numbers)

# 5. Вставка элемента по индексу — insert()
numbers.insert(1, 15)
print(numbers)

# 6. Добавление нескольких элементов — extend()
numbers.extend([60, 70])
print(numbers)

# 7. Удаление по значению — remove()
numbers.remove(30)
print(numbers)

# 8. Удаление по индексу — pop()
last = numbers.pop()
print(last)
print(numbers)

# Можно удалить элемент по конкретному индексу:
value = numbers.pop(1)
print(value)

# 9. Очистка списка
example = [1, 2, 3]
example.clear()
print(example)  # []

# 10. Проверка наличия элемента
numbers = [5, 10, 15, 20]

if 15 in numbers:
    print('15 есть в списке')

if 100 not in numbers:
    print('100 нет в списке')

# 11. Перебор элементов
for x in numbers:
    print(x)

# Перебор по индексам
for i in range(len(numbers)):
    print(i, numbers[i])

# 12. Срезы списка
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[::2])   # [10, 30, 50]
print(numbers[::-1])  # список наоборот

# 13. Ввод списка чисел одной строкой
numbers = list(map(int, input('Введите числа через пробел: ').split()))
print(numbers)

# 14. Сумма, минимум и максимум
numbers = [7, 2, 9, 4]
print(sum(numbers))  # 22
print(min(numbers))  # 2
print(max(numbers))  # 9

# 15. Сортировка — sort()
numbers = [7, 2, 9, 4]
numbers.sort()
print(numbers)  # [2, 4, 7, 9]

# По убыванию:
numbers.sort(reverse=True)
print(numbers)  # [9, 7, 4, 2]

# sort() изменяет исходный список.

# 16. sorted() — получить новый отсортированный список
numbers = [7, 2, 9, 4]
new_numbers = sorted(numbers)
print(new_numbers)
print(numbers)  # исходный список не изменился

# 17. Количество вхождений — count()
numbers = [1, 2, 2, 3, 2]
print(numbers.count(2))  # 3

# 18. Поиск индекса элемента — index()
print(numbers.index(3))  # 3

# 19. Копирование списка
numbers = [1, 2, 3]
copy_numbers = numbers.copy()
copy_numbers.append(4)

print(numbers)       # [1, 2, 3]
print(copy_numbers)  # [1, 2, 3, 4]

# Важно: если написать copy_numbers = numbers,
# обе переменные будут ссылаться на один и тот же список.

# 20. Список строк
words = ['Python', 'ЕГЭ', 'ОГЭ']
for word in words:
    print(word)

# 21. Список списков
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])     # [1, 2, 3]
print(matrix[1][2])  # 6

# 22. Генератор списка
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# С условием:
even = [x for x in range(1, 11) if x % 2 == 0]
print(even)  # [2, 4, 6, 8, 10]

# Частые ошибки
# 1. Индексация начинается с 0.
# 2. pop() удаляет по индексу, remove() — по значению.
# 3. sort() изменяет исходный список и ничего полезного не возвращает.
# 4. sorted() возвращает новый список.
# 5. list(map(int, input().split())) — стандартный ввод списка целых чисел.
# 6. copy_numbers = numbers не создаёт независимую копию списка.

# Универсальные шаблоны

# Ввод списка чисел:
# numbers = list(map(int, input().split()))

# Перебор элементов:
# for x in numbers:
#     ...

# Перебор по индексам:
# for i in range(len(numbers)):
#     ...

# Фильтрация:
# result = [x for x in numbers if условие]

# Преобразование:
# result = [выражение for x in numbers]
