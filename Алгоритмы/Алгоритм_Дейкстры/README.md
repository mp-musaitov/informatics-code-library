# Алгоритм Дейкстры

Алгоритм Дейкстры находит кратчайшие расстояния от одной начальной вершины до остальных вершин взвешенного графа.

Взвешенный граф отличается тем, что каждому ребру назначена стоимость: длина, время, цена или другое числовое значение.

Алгоритм работает, если веса рёбер неотрицательны.

---

## 1. Представление взвешенного графа

Для каждого соседа нужно хранить не только номер вершины, но и вес перехода.

```python
graph = {
    1: [[2, 4], [3, 2]],
    2: [[1, 4], [3, 1], [4, 5]],
    3: [[1, 2], [2, 1], [4, 8], [5, 10]],
    4: [[2, 5], [3, 8], [5, 2]],
    5: [[3, 10], [4, 2]]
}
```

Запись:

```python
[2, 4]
```

означает переход в вершину `2` с весом `4`.

Перебор соседей:

```python
for neighbour, weight in graph.get(vertex, []):
    ...
```

В неориентированном графе каждое ребро записывается в обе стороны. В ориентированном — только в направлении перехода.

---

## 2. Почему BFS недостаточно

BFS находит путь с минимальным количеством рёбер.

Но во взвешенном графе два ребра могут оказаться дешевле одного:

```text
1 → 2        стоимость 10

1 → 3 → 2    стоимость 2 + 1 = 3
```

Поэтому нужно сравнивать не количество переходов, а их общую стоимость.

Дейкстра каждый раз продолжает работу из вершины с наименьшим известным расстоянием.

---

## 3. Словарь расстояний

В начале известно только расстояние до стартовой вершины:

```python
start = 1

dist = {
    start: 0
}
```

Для остальных вершин расстояние пока считается бесконечным:

```python
dist.get(vertex, float('inf'))
```

Если ключа нет, метод `.get()` возвращает бесконечность. Любой найденный конечный путь будет короче неё.

---

## 4. Очередь с приоритетом

Для быстрого выбора ближайшей вершины используется модуль `heapq`.

```python
from heapq import heappush, heappop

queue = []

heappush(queue, (7, 3))
heappush(queue, (2, 5))
heappush(queue, (4, 1))

print(heappop(queue))
```

Результат:

```text
(2, 5)
```

В очередь помещаются пары:

```text
(расстояние, вершина)
```

Наименьшее расстояние извлекается первым.

Начальное состояние:

```python
queue = [(0, start)]
```

---

## 5. Улучшение расстояния

Пусть до текущей вершины уже найден путь длины `current_distance`, а ребро до соседа имеет вес `weight`.

```python
new_distance = current_distance + weight
```

Если новый путь короче известного, значение обновляется:

```python
if new_distance < dist.get(neighbour, float('inf')):
    dist[neighbour] = new_distance
    heappush(queue, (new_distance, neighbour))
```

Этот шаг часто называют пересчётом или ослаблением ребра. Для ученика достаточно понимать: мы нашли более короткий путь и сохраняем его.

---

## 6. Полный алгоритм

```python
from heapq import heappush, heappop

graph = {
    1: [[2, 4], [3, 2]],
    2: [[1, 4], [3, 1], [4, 5]],
    3: [[1, 2], [2, 1], [4, 8], [5, 10]],
    4: [[2, 5], [3, 8], [5, 2]],
    5: [[3, 10], [4, 2]]
}

start = 1

dist = {start: 0}
queue = [(0, start)]

while queue:
    current_distance, vertex = heappop(queue)

    if current_distance != dist[vertex]:
        continue

    for neighbour, weight in graph.get(vertex, []):
        new_distance = current_distance + weight

        if new_distance < dist.get(neighbour, float('inf')):
            dist[neighbour] = new_distance
            heappush(queue, (new_distance, neighbour))

print(dist)
```

Кратчайшее расстояние до вершины `5`:

```python
print(dist[5])
```

Результат:

```text
10
```

---

## 7. Устаревшие записи

Одна вершина может попасть в очередь несколько раз.

Например, сначала найден путь длины `10`, а затем — длины `7`. В словаре останется `7`, но старая пара `(10, vertex)` всё ещё находится в очереди.

Удалять её вручную не нужно.

```python
while queue:
    current_distance, vertex = heappop(queue)

    if current_distance != dist[vertex]:
        continue
```

Когда устаревшая запись будет извлечена, её расстояние не совпадёт с актуальным и обработка сразу продолжится со следующего элемента.

---

## 8. Поиск пути до одной вершины

Если нужна только одна конечная вершина, алгоритм можно остановить после её извлечения из очереди.

```python
target = 5

while queue:
    current_distance, vertex = heappop(queue)

    if current_distance != dist[vertex]:
        continue

    if vertex == target:
        break

    for neighbour, weight in graph.get(vertex, []):
        new_distance = current_distance + weight

        if new_distance < dist.get(neighbour, float('inf')):
            dist[neighbour] = new_distance
            heappush(queue, (new_distance, neighbour))
```

Важно останавливаться не при первом добавлении цели в очередь, а после её извлечения с актуальным расстоянием. До этого может найтись более короткий маршрут.

---

## 9. Недостижимая вершина

Если вершина не появилась в `dist`, пути до неё нет.

```python
target = 6

if target in dist:
    print(dist[target])
else:
    print('Пути нет')
```

Не следует обращаться к `dist[target]` без проверки, если достижимость не гарантирована условием.

---

## 10. Восстановление кратчайшего пути

Сохраним родителя вершины каждый раз, когда улучшаем расстояние.

```python
from heapq import heappush, heappop

start = 1
target = 5

dist = {start: 0}
parent = {start: None}

queue = [(0, start)]

while queue:
    current_distance, vertex = heappop(queue)

    if current_distance != dist[vertex]:
        continue

    for neighbour, weight in graph.get(vertex, []):
        new_distance = current_distance + weight

        if new_distance < dist.get(neighbour, float('inf')):
            dist[neighbour] = new_distance
            parent[neighbour] = vertex
            heappush(queue, (new_distance, neighbour))

if target in dist:
    path = []
    vertex = target

    while vertex is not None:
        path.append(vertex)
        vertex = parent[vertex]

    path.reverse()

    print(dist[target])
    print(path)
else:
    print('Пути нет')
```

Для примера будет восстановлен путь:

```text
1 → 3 → 2 → 4 → 5
```

---

## 11. Ориентированный и неориентированный граф

Для неориентированного ребра между `first` и `second`:

```python
graph[first].append([second, weight])
graph[second].append([first, weight])
```

Для ориентированного ребра `first → second`:

```python
graph[first].append([second, weight])
```

Второй переход автоматически не существует.

Перед построением графа нужно внимательно прочитать условие.

---

## 12. Чтение графа из файла

Пусть файл `data.txt` имеет формат:

```text
5 7
1 2 4
1 3 2
2 3 1
2 4 5
3 4 8
3 5 10
4 5 2
```

Первая строка содержит количество вершин и рёбер. Далее записаны начало, конец и вес каждого неориентированного ребра.

```python
with open('data.txt') as f:
    n, m = map(int, f.readline().split())

    graph = {}

    for vertex in range(1, n + 1):
        graph[vertex] = []

    for _ in range(m):
        first, second, weight = map(int, f.readline().split())

        graph[first].append([second, weight])
        graph[second].append([first, weight])
```

Если веса вещественные:

```python
first, second, weight = f.readline().split()

first = int(first)
second = int(second)
weight = float(weight)
```

Не преобразовывайте результат в `int`, если по условию требуется сохранить дробную часть.

---

## 13. Отрицательные веса

Алгоритм Дейкстры нельзя применять к графу с отрицательными весами.

Его логика основана на том, что продолжение пути не может уменьшить уже извлечённое минимальное расстояние.

При отрицательном ребре это свойство нарушается.

Нулевые веса допустимы, отрицательные — нет.

---

## 14. Частые ошибки

### Ошибка 1. Перепутать вершину и расстояние в очереди

Правильный порядок:

```python
heappush(queue, (distance, vertex))
```

### Ошибка 2. Не проверить улучшение

Добавлять новый путь нужно только тогда, когда он короче:

```python
if new_distance < dist.get(neighbour, float('inf')):
    ...
```

### Ошибка 3. Не пропускать устаревшие записи

Используйте:

```python
while queue:
    current_distance, vertex = heappop(queue)

    if current_distance != dist[vertex]:
        continue
```

### Ошибка 4. Остановиться при добавлении цели в очередь

Окончательное кратчайшее расстояние известно после извлечения цели с актуальным значением.

### Ошибка 5. Применить алгоритм к отрицательным рёбрам

Перед запуском убедитесь, что все веса неотрицательны.

### Ошибка 6. Неправильно записать направление рёбер

Для неориентированного графа нужны обе стороны, для ориентированного — только указанная.

---

## Краткая памятка

```python
from heapq import heappush, heappop

dist = {start: 0}
queue = [(0, start)]

while queue:
    current_distance, vertex = heappop(queue)

    if current_distance != dist[vertex]:
        continue

    for neighbour, weight in graph.get(vertex, []):
        new_distance = current_distance + weight

        if new_distance < dist.get(neighbour, float('inf')):
            dist[neighbour] = new_distance
            heappush(queue, (new_distance, neighbour))
```

Главное:

- граф хранит соседнюю вершину и вес ребра;
- очередь с приоритетом первой выдаёт ближайшую вершину;
- расстояние обновляется только при улучшении;
- устаревшие записи пропускаются;
- для восстановления пути сохраняются родители;
- Дейкстра работает только с неотрицательными весами.

---

[↑ Все алгоритмы](../README.md) · [← DFS и BFS](../DFS_и_BFS/) · [Динамическое программирование →](../Динамическое_программирование/)
