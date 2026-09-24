# Циклы в Python

Циклы позволяют повторять действия несколько раз.

## Цикл for

`for` удобно использовать, когда заранее известно количество повторений.

```python
for i in range(5):
    print(i)
```

Получим числа от 0 до 4. Правая граница `range()` не включается.

```python
for i in range(2, 6):
    print(i)
```

Получим числа от 2 до 5.

Шаг задаётся третьим аргументом:

```python
for i in range(10, 0, -2):
    print(i)
```

## Перебор строки и списка

```python
for symbol in 'python':
    print(symbol)
```

```python
numbers = [4, 7, 2, 9]

for x in numbers:
    print(x)
```

## Сумма и количество

```python
total = 0

for x in numbers:
    total += x
```

```python
count = 0

for x in numbers:
    if x % 2 == 0:
        count += 1
```

## Поиск максимума

```python
maximum = numbers[0]

for x in numbers:
    if x > maximum:
        maximum = x
```

## Цикл while

`while` удобен, когда заранее неизвестно количество повторений.

```python
x = 1

while x <= 5:
    print(x)
    x += 1
```

Нужно следить, чтобы условие когда-нибудь стало ложным.

## break и continue

`break` завершает ближайший цикл:

```python
for i in range(10):
    if i == 5:
        break
```

`continue` пропускает текущую итерацию:

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

## Вложенные циклы

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

## Частые ошибки

- считать, что `range(5)` даёт числа от 1 до 5;
- забывать, что правая граница не включается;
- получить бесконечный `while`;
- путать `break` и `continue`;
- ошибаться с отступами.

## Памятка

```python
for x in последовательность:
    ...

while условие:
    ...
```

Готовые примеры для быстрого копирования находятся в файле [`03_Циклы.py`](03_Циклы.py).
