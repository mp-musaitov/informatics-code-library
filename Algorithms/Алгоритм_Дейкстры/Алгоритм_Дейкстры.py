# ============================================================
# БЛОК 1. ВЗВЕШЕННЫЙ ГРАФ
# ============================================================

graph = {
    1: [[2, 4], [3, 2]],
    2: [[1, 4], [3, 1], [4, 5]],
    3: [[1, 2], [2, 1], [4, 8], [5, 10]],
    4: [[2, 5], [3, 8], [5, 2]],
    5: [[3, 10], [4, 2]]
}

print(graph)


# ============================================================
# БЛОК 2. ОЧЕРЕДЬ С ПРИОРИТЕТОМ
# ============================================================

from heapq import heappush, heappop

queue = []

heappush(queue, (7, 3))
heappush(queue, (2, 5))
heappush(queue, (4, 1))

print(heappop(queue))


# ============================================================
# БЛОК 3. РАССТОЯНИЯ ОТ НАЧАЛЬНОЙ ВЕРШИНЫ
# ============================================================

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


# ============================================================
# БЛОК 4. РАССТОЯНИЕ ДО ВЫБРАННОЙ ЦЕЛИ
# ============================================================

target = 5

if target in dist:
    print(dist[target])
else:
    print('Пути нет')


# ============================================================
# БЛОК 5. ДОСРОЧНАЯ ОСТАНОВКА
# ============================================================

start = 1
target = 5

dist = {start: 0}
queue = [(0, start)]

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

print(dist[target])


# ============================================================
# БЛОК 6. ВОССТАНОВЛЕНИЕ КРАТЧАЙШЕГО ПУТИ
# ============================================================

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


# ============================================================
# БЛОК 7. НЕДОСТИЖИМАЯ ВЕРШИНА
# ============================================================

target = 6

if target in dist:
    print(dist[target])
else:
    print('Пути нет')


# ============================================================
# БЛОК 8. ЧТЕНИЕ ГРАФА ИЗ ФАЙЛА
# ============================================================

# Формат файла data.txt:
# первая строка — количество вершин и рёбер;
# далее записаны рёбра неориентированного графа.
#
# with open('data.txt') as f:
#     n, m = map(int, f.readline().split())
#
#     graph = {}
#
#     for vertex in range(1, n + 1):
#         graph[vertex] = []
#
#     for _ in range(m):
#         first, second, weight = map(int, f.readline().split())
#
#         graph[first].append([second, weight])
#         graph[second].append([first, weight])
#
# start = 1
#
# dist = {start: 0}
# queue = [(0, start)]
#
# while queue:
#     current_distance, vertex = heappop(queue)
#
#     if current_distance != dist[vertex]:
#         continue
#
#     for neighbour, weight in graph.get(vertex, []):
#         new_distance = current_distance + weight
#
#         if new_distance < dist.get(neighbour, float('inf')):
#             dist[neighbour] = new_distance
#             heappush(queue, (new_distance, neighbour))
#
# print(dist)
