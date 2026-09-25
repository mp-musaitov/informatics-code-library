# Списки в Python

Список — изменяемая коллекция элементов.

```python
numbers = [10, 20, 30, 40]
```

## Индексы и изменение

```python
print(numbers[0])   # 10
print(numbers[-1])  # 40

numbers[1] = 25
```

В отличие от строки, элемент списка можно изменить.

## Добавление и удаление

```python
numbers.append(50)
numbers.insert(1, 15)
numbers.extend([60, 70])
```

Удаление по значению и по индексу:

```python
numbers.remove(30)
value = numbers.pop(1)
```

`remove()` ищет значение, `pop()` работает с индексом.

## Перебор

```python
for x in numbers:
    print(x)

for i in range(len(numbers)):
    print(i, numbers[i])
```

## Срезы

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])
print(numbers[:3])
print(numbers[::2])
print(numbers[::-1])
```

## Ввод списка чисел

```python
numbers = list(map(int, input().split()))
```

## Сумма, минимум и максимум

```python
print(sum(numbers))
print(min(numbers))
print(max(numbers))
```

## Сортировка

`sort()` изменяет исходный список:

```python
numbers.sort()
numbers.sort(reverse=True)
```

`sorted()` возвращает новый:

```python
new_numbers = sorted(numbers)
```

## count() и index()

```python
numbers = [1, 2, 2, 3, 2]

print(numbers.count(2))  # 3
print(numbers.index(3))  # 3
```

## Копирование

```python
copy_numbers = numbers.copy()
```

`copy_numbers = numbers` не создаёт независимую копию.

## Список списков

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])  # 6
```

## Генераторы списков

```python
squares = [x ** 2 for x in range(1, 6)]
even = [x for x in range(1, 11) if x % 2 == 0]
```

## Частые ошибки

- забывать, что индексация начинается с нуля;
- путать `pop()` и `remove()`;
- ожидать новый список от `sort()`;
- забывать `list()` при вводе через `map()`;
- считать, что обычное присваивание создаёт копию.

## Памятка

```python
numbers = list(map(int, input().split()))
numbers.append(x)
numbers.sort()
sum(numbers)
min(numbers)
max(numbers)
```

Готовые примеры для быстрого копирования находятся в файле [`05_Списки.py`](05_Списки.py).

## Практика

[Практические задания по теме](PRACTICE.md) — разминка, основной и повышенный уровни, мини-задача в стиле ЕГЭ/ОГЭ.
