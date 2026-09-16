# DFS и BFS

DFS и BFS — два основных способа обхода графа.

Граф состоит из:

- вершин — объектов;
- рёбер — связей между объектами.

Обход графа нужен, чтобы определить достижимость вершин, найти компоненты связности, вычислить расстояния или восстановить путь.

---

## 1. Список соседей

Граф удобно хранить в словаре:

```python
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4],
    4: [2, 3, 5],
    5: [4]
}
```

Ключ — вершина, значение — список вершин, в которые можно перейти.

В неориентированном графе каждое ребро записывается в обе стороны:

```python
graph[1].append(2)
graph[2].append(1)
```

В ориентированном графе для ребра `1 → 2` добавляется только переход из `1` в `2`.

Метод `.get(vertex, [])` позволяет безопасно получить соседей даже для вершины, которой нет среди ключей.

---

## 2. Зачем нужен `visited`

В графе могут быть циклы:

```text
1 → 2 → 4 → 3 → 1
```

Без запоминания посещённых вершин обход будет снова возвращаться к тем же вершинам.

```python
visited = set()
```

Перед переходом проверяем:

```python
if neighbour not in visited:
    ...
```

Множество подходит для быстрой проверки наличия элемента.

---

## 3. DFS — обход в глубину

DFS сначала идёт по одной ветви как можно глубже, а затем возвращается к ещё не рассмотренным соседям.

```python
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4],
    4: [2, 3, 5],
    5: [4]
}

visited = set()

def dfs(vertex):
    visited.add(vertex)
    print(vertex)

    for neighbour in graph.get(vertex, []):
        if neighbour not in visited:
            dfs(neighbour)


dfs(1)
```

Порядок обхода зависит от порядка соседей в списках. При другом порядке рёбер DFS может посетить вершины иначе, но все достижимые вершины всё равно будут обработаны.

---

## 4. DFS со стеком

Рекурсию можно заменить обычным списком, используемым как стек.

```python
visited = set()
stack = [1]

while stack:
    vertex = stack.pop()

    if vertex in visited:
        continue

    visited.add(vertex)
    print(vertex)

    for neighbour in graph.get(vertex, []):
        if neighbour not in visited:
            stack.append(neighbour)
```

Метод `.pop()` забирает последний добавленный элемент. Поэтому обход продолжает последнюю открытую ветвь.

Итеративный вариант полезен для больших графов, где глубокая рекурсия может привести к ошибке ограничения глубины.

---

## 5. Проверка достижимости

После DFS множество `visited` содержит все вершины, достижимые из начальной.

```python
start = 1
target = 5

visited = set()

def dfs(vertex):
    visited.add(vertex)

    for neighbour in graph.get(vertex, []):
        if neighbour not in visited:
            dfs(neighbour)


dfs(start)

if target in visited:
    print('Путь существует')
else:
    print('Пути нет')
```

Здесь не требуется находить конкретный маршрут — достаточно проверить посещение конечной вершины.

---

## 6. Компоненты связности

Компонента связности — группа вершин неориентированного графа, между которыми существуют пути.

```python
graph = {
    1: [2],
    2: [1, 3],
    3: [2],
    4: [5],
    5: [4],
    6: []
}

visited = set()

def dfs(vertex):
    visited.add(vertex)

    for neighbour in graph.get(vertex, []):
        if neighbour not in visited:
            dfs(neighbour)


components = 0

for vertex in graph:
    if vertex not in visited:
        dfs(vertex)
        components += 1

print(components)
```

Результат:

```text
3
```

Каждый запуск DFS из непосещённой вершины полностью обходит одну новую компоненту.

---

## 7. BFS — обход в ширину

BFS посещает вершины по слоям:

1. начальная вершина;
2. все вершины на расстоянии одного ребра;
3. все вершины на расстоянии двух рёбер;
4. следующие слои.

Для очереди используется `deque`:

```python
from collections import deque

queue = deque([1])
visited = {1}

while queue:
    vertex = queue.popleft()
    print(vertex)

    for neighbour in graph.get(vertex, []):
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)
```

Вершина отмечается посещённой в момент добавления в очередь. Тогда она не попадёт в очередь повторно через другого соседа.

`deque.popleft()` быстро удаляет первый элемент очереди. Обычный `list.pop(0)` для больших списков работает менее эффективно.

---

## 8. Расстояния в невзвешенном графе

BFS впервые достигает каждой вершины по пути с минимальным количеством рёбер.

```python
from collections import deque

start = 1

queue = deque([start])
distance = {start: 0}

while queue:
    vertex = queue.popleft()

    for neighbour in graph.get(vertex, []):
        if neighbour not in distance:
            distance[neighbour] = distance[vertex] + 1
            queue.append(neighbour)

print(distance)
```

Словарь `distance` одновременно хранит расстояния и показывает, какие вершины уже посещены.

Если вершины нет в `distance`, она недостижима из начальной.

---

## 9. Восстановление кратчайшего пути

Кроме расстояния сохраним родителя каждой вершины — вершину, из которой мы впервые в неё пришли.

```python
from collections import deque

start = 1
target = 5

queue = deque([start])
distance = {start: 0}
parent = {start: None}

while queue:
    vertex = queue.popleft()

    for neighbour in graph.get(vertex, []):
        if neighbour not in distance:
            distance[neighbour] = distance[vertex] + 1
            parent[neighbour] = vertex
            queue.append(neighbour)

if target in parent:
    path = []
    vertex = target

    while vertex is not None:
        path.append(vertex)
        vertex = parent[vertex]

    path.reverse()

    print(path)
else:
    print('Пути нет')
```

Путь восстанавливается от конечной вершины к начальной, поэтому затем список переворачивается.

---

## 10. DFS и поиск с возвратом

Оба подхода могут использовать рекурсию и движение в глубину.

В DFS обходится уже заданный граф. Посещённая вершина обычно остаётся в `visited`, чтобы не обрабатывать её повторно.

В поиске с возвратом строится вариант решения. После возврата сделанный выбор часто отменяется:

```python
current.pop()
```

Нельзя автоматически переносить правила изменения состояния из одного алгоритма в другой.

---

## 11. BFS и алгоритм Дейкстры

BFS находит кратчайший путь по количеству рёбер:

```text
каждое ребро имеет одинаковую стоимость
```

Если рёбра имеют разные веса, путь с меньшим количеством рёбер может оказаться дороже.

Для графов с неотрицательными весами используется алгоритм Дейкстры, который будет рассмотрен в следующем отдельном разделе.

---

## 12. Чтение графа из файла

Пусть файл `data.txt` имеет формат:

```text
5 5
1 2
1 3
2 4
3 4
4 5
```

Первая строка содержит количество вершин и рёбер. Далее записаны рёбра неориентированного графа.

```python
with open('data.txt') as f:
    n, m = map(int, f.readline().split())

    graph = {}

    for vertex in range(1, n + 1):
        graph[vertex] = []

    for _ in range(m):
        first, second = map(int, f.readline().split())

        graph[first].append(second)
        graph[second].append(first)
```

Предварительное создание всех ключей сохраняет в словаре даже изолированные вершины.

Для ориентированного графа строка:

```python
graph[second].append(first)
```

не добавляется.

---

## 13. Частые ошибки

### Ошибка 1. Не использовать `visited`

В графе с циклами обход начнёт повторять одни и те же переходы.

### Ошибка 2. Слишком поздно отмечать вершину в BFS

В BFS вершину лучше отмечать при добавлении в очередь:

```python
visited.add(neighbour)
queue.append(neighbour)
```

### Ошибка 3. Добавить неориентированное ребро только в одну сторону

Нужно добавить оба перехода:

```python
graph[first].append(second)
graph[second].append(first)
```

### Ошибка 4. Искать взвешенный кратчайший путь обычным BFS

BFS учитывает количество рёбер, но не разные веса.

### Ошибка 5. Забыть проверить достижимость перед восстановлением пути

Если `target` отсутствует в `parent`, путь до него не найден.

---

## Краткая памятка

```python
# DFS
visited = set()

def dfs(vertex):
    visited.add(vertex)

    for neighbour in graph.get(vertex, []):
        if neighbour not in visited:
            dfs(neighbour)
```

```python
# BFS и расстояния
from collections import deque

queue = deque([start])
distance = {start: 0}

while queue:
    vertex = queue.popleft()

    for neighbour in graph.get(vertex, []):
        if neighbour not in distance:
            distance[neighbour] = distance[vertex] + 1
            queue.append(neighbour)
```

Главное:

- список соседей хранит переходы из каждой вершины;
- `visited` защищает от повторного обхода;
- DFS идёт в глубину;
- BFS обрабатывает граф по слоям;
- BFS находит кратчайшие расстояния только в невзвешенном графе;
- родительские вершины позволяют восстановить путь.
