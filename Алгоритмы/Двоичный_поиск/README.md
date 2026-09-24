# Двоичный поиск

Двоичный поиск позволяет быстро найти элемент в отсортированной последовательности.

Вместо последовательной проверки всех элементов алгоритм каждый раз сравнивает искомое значение со средним элементом и отбрасывает половину оставшегося диапазона.

Главное условие:

> Данные должны быть отсортированы по тому же признаку, по которому выполняется поиск.

---

## 1. Последовательный поиск

Обычный поиск проверяет элементы по очереди:

```python
numbers = [2, 4, 7, 9, 12, 15, 18]
target = 12

answer = None

for i in range(len(numbers)):
    if numbers[i] == target:
        answer = i
        break

print(answer)
```

Результат:

```text
4
```

Такой способ работает и для неотсортированного списка, но в худшем случае просматривает все элементы.

---

## 2. Левая, правая и средняя позиции

В двоичном поиске используются три индекса:

```python
left = 0
right = len(numbers) - 1
middle = (left + right) // 2
```

- `left` — левая граница области поиска;
- `right` — правая граница;
- `middle` — середина этой области.

Если средний элемент меньше искомого, вся левая часть уже не подходит. Если средний элемент больше искомого, не подходит правая часть.

---

## 3. Ручной двоичный поиск

```python
numbers = [2, 4, 7, 9, 12, 15, 18]
target = 12

left = 0
right = len(numbers) - 1

answer = None

while left <= right:
    middle = (left + right) // 2

    if numbers[middle] == target:
        answer = middle
        break
    elif numbers[middle] < target:
        left = middle + 1
    else:
        right = middle - 1

print(answer)
```

Результат:

```text
4
```

Почему границы изменяются на `middle + 1` и `middle - 1`:

- элемент с индексом `middle` уже проверен;
- оставлять его внутри диапазона больше не нужно;
- граница обязательно должна сдвигаться, иначе цикл может не завершиться.

Условие `left <= right` позволяет проверить последний оставшийся элемент, когда обе границы совпали.

---

## 4. Функция двоичного поиска

Готовый алгоритм удобно оформить в виде функции:

```python
def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle
        elif numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return None


numbers = [2, 4, 7, 9, 12, 15, 18]

print(binary_search(numbers, 12))
print(binary_search(numbers, 10))
```

Результат:

```text
4
None
```

Если значение найдено, функция сразу возвращает индекс. Если цикл закончился, искомого элемента в списке нет.

---

## 5. Повторяющиеся элементы

Рассмотрим список:

```python
numbers = [2, 4, 4, 4, 7, 9]
```

Обычный двоичный поиск может вернуть индекс любого элемента `4`. Он не обязан находить первое или последнее вхождение.

Если условие требует конкретную границу группы одинаковых элементов, после совпадения поиск нельзя сразу завершать.

---

## 6. Первое вхождение

После нахождения `target` сохраним индекс и продолжим поиск левее:

```python
numbers = [2, 4, 4, 4, 7, 9]
target = 4

left = 0
right = len(numbers) - 1

answer = None

while left <= right:
    middle = (left + right) // 2

    if numbers[middle] >= target:
        if numbers[middle] == target:
            answer = middle

        right = middle - 1
    else:
        left = middle + 1

print(answer)
```

Результат:

```text
1
```

Даже после совпадения правая граница сдвигается влево: возможно, такое же значение находится раньше.

---

## 7. Последнее вхождение

Для последнего вхождения после совпадения продолжаем поиск правее:

```python
numbers = [2, 4, 4, 4, 7, 9]
target = 4

left = 0
right = len(numbers) - 1

answer = None

while left <= right:
    middle = (left + right) // 2

    if numbers[middle] <= target:
        if numbers[middle] == target:
            answer = middle

        left = middle + 1
    else:
        right = middle - 1

print(answer)
```

Результат:

```text
3
```

---

## 8. Модуль `bisect`

В стандартном модуле `bisect` есть готовые функции для отсортированных списков.

```python
from bisect import bisect_left, bisect_right

numbers = [2, 4, 4, 4, 7, 9]
target = 4

left_position = bisect_left(numbers, target)
right_position = bisect_right(numbers, target)

print(left_position)
print(right_position)
```

Результат:

```text
1
4
```

`bisect_left()` возвращает позицию, перед которой можно вставить значение.

`bisect_right()` возвращает позицию после всех равных элементов.

Функции возвращают допустимую позицию вставки, даже если элемента в списке нет. Поэтому наличие значения проверяется отдельно:

```python
position = bisect_left(numbers, target)

if position < len(numbers) and numbers[position] == target:
    print('Найдено')
else:
    print('Не найдено')
```

---

## 9. Количество вхождений

Разность правой и левой позиций равна количеству повторений:

```python
from bisect import bisect_left, bisect_right

numbers = [2, 4, 4, 4, 7, 9]
target = 4

count = bisect_right(numbers, target) - bisect_left(numbers, target)

print(count)
```

Результат:

```text
3
```

Если элемента нет, обе функции вернут одну и ту же позицию, поэтому результат будет равен нулю.

---

## 10. Первый элемент, не меньший заданного

`bisect_left()` можно использовать не только для точного совпадения.

```python
from bisect import bisect_left

numbers = [2, 4, 7, 9, 12, 15]
target = 8

position = bisect_left(numbers, target)

if position < len(numbers):
    print(numbers[position])
else:
    print('Подходящего элемента нет')
```

Результат:

```text
9
```

Число `9` — первый элемент, который не меньше `8`.

Обязательно проверяйте `position < len(numbers)`: позиция может оказаться сразу после последнего элемента.

---

## 11. Двоичный поиск по ответу

Иногда готового списка нет, но возможные ответы образуют упорядоченный диапазон.

Найдём минимальное целое неотрицательное число, квадрат которого не меньше `number`.

```python
number = 30

left = 0
right = number

while left < right:
    middle = (left + right) // 2

    if middle * middle >= number:
        right = middle
    else:
        left = middle + 1

print(left)
```

Результат:

```text
6
```

Для числа `5` условие ещё не выполняется, а для `6` уже выполняется:

```text
5² = 25 < 30
6² = 36 >= 30
```

Здесь ищется граница между неподходящими и подходящими значениями.

Такой приём можно использовать, когда:

- существует диапазон возможных ответов;
- для каждого значения можно проверить условие;
- после некоторой границы все значения становятся подходящими.

---

## 12. Работа с файлом

Пусть файл `data.txt` имеет формат:

```text
7
2 4 7 9 12 15 18
3
12
10
2
```

Здесь записаны количество элементов, отсортированный список, количество запросов и искомые значения.

```python
from bisect import bisect_left

with open('data.txt') as f:
    n = int(f.readline())
    numbers = list(map(int, f.readline().split()))
    q = int(f.readline())

    for _ in range(q):
        target = int(f.readline())

        position = bisect_left(numbers, target)

        if position < len(numbers) and numbers[position] == target:
            print(position)
        else:
            print('Не найдено')
```

Переменная `n` показывает ожидаемое количество элементов. В конкретной задаче сначала нужно проверить формат файла и способ нумерации позиций.

---

## 13. Частые ошибки

### Ошибка 1. Искать в неотсортированном списке

Двоичный поиск делает вывод о целой половине данных по среднему элементу. Для неотсортированного списка этот вывод неверен.

### Ошибка 2. Не сдвинуть границу за середину

Неправильно:

```python
left = middle
```

Правильно для слишком маленького среднего элемента:

```python
left = middle + 1
```

### Ошибка 3. Перепутать условие цикла

В классическом поиске с включёнными границами используются:

```python
left = 0
right = len(numbers) - 1

while left <= right:
    ...
```

В показанном поиске минимального ответа используется другой шаблон:

```python
while left < right:
    ...
```

Нельзя смешивать части разных шаблонов без изменения всей логики.

### Ошибка 4. Считать результат `bisect_left()` доказательством наличия элемента

Функция возвращает позицию вставки. После неё нужна проверка значения.

### Ошибка 5. Не проверить выход за список

Перед обращением к `numbers[position]`:

```python
if position < len(numbers):
    ...
```

---

## Краткая памятка

```python
# Точный поиск
left = 0
right = len(numbers) - 1

answer = None

while left <= right:
    middle = (left + right) // 2

    if numbers[middle] == target:
        answer = middle
        break
    elif numbers[middle] < target:
        left = middle + 1
    else:
        right = middle - 1
```

```python
# Готовые функции
from bisect import bisect_left, bisect_right

first = bisect_left(numbers, target)
after_last = bisect_right(numbers, target)
count = after_last - first
```

Главное:

- двоичный поиск требует упорядоченных данных;
- границы должны обязательно сдвигаться;
- обычный поиск может вернуть любое из одинаковых значений;
- `bisect_left()` и `bisect_right()` возвращают позиции вставки;
- двоичный поиск применим и к диапазону возможных ответов.

--- · [↑ Все алгоритмы](../README.md) · [← Скользящее окно](../Скользящее_окно/) · [Жадные алгоритмы →](../Жадные_алгоритмы/)
