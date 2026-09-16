# ============================================================
# БЛОК 1. СПИСОК СОСЕДЕЙ
# ============================================================

graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4],
    4: [2, 3, 5],
    5: [4]
}

print(graph)


# ============================================================
# БЛОК 2. РЕКУРСИВНЫЙ DFS
# ============================================================

visited = set()

def dfs(vertex):
    visited.add(vertex)
    print(vertex)

    for neighbour in graph.get(vertex, []):
        if neighbour not in visited:
            dfs(neighbour)


dfs(1)


# ============================================================
# БЛОК 3. DFS СО СТЕКОМ
# ============================================================

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


# ============================================================
# БЛОК 4. ПРОВЕРКА ДОСТИЖИМОСТИ
# ============================================================

start = 1
target = 5

visited = set()

def mark_reachable(vertex):
    visited.add(vertex)

    for neighbour in graph.get(vertex, []):
        if neighbour not in visited:
            mark_reachable(neighbour)


mark_reachable(start)

print(target in visited)


# ============================================================
# БЛОК 5. КОМПОНЕНТЫ СВЯЗНОСТИ
# ============================================================

graph_with_components = {
    1: [2],
    2: [1, 3],
    3: [2],
    4: [5],
    5: [4],
    6: []
}

visited = set()

def mark_component(vertex):
    visited.add(vertex)

    for neighbour in graph_with_components.get(vertex, []):
        if neighbour not in visited:
            mark_component(neighbour)


components = 0

for vertex in graph_with_components:
    if vertex not in visited:
        mark_component(vertex)
        components += 1

print(components)


# ============================================================
# БЛОК 6. BFS
# ============================================================

from collections import deque

start = 1

queue = deque([start])
visited = {start}

while queue:
    vertex = queue.popleft()
    print(vertex)

    for neighbour in graph.get(vertex, []):
        if neighbour not in visited:
            visited.add(neighbour)
            queue.append(neighbour)


# ============================================================
# БЛОК 7. РАССТОЯНИЯ ОТ НАЧАЛЬНОЙ ВЕРШИНЫ
# ============================================================

queue = deque([start])
distance = {start: 0}

while queue:
    vertex = queue.popleft()

    for neighbour in graph.get(vertex, []):
        if neighbour not in distance:
            distance[neighbour] = distance[vertex] + 1
            queue.append(neighbour)

print(distance)


# ============================================================
# БЛОК 8. ВОССТАНОВЛЕНИЕ КРАТЧАЙШЕГО ПУТИ
# ============================================================

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


# ============================================================
# БЛОК 9. ЧТЕНИЕ ГРАФА ИЗ ФАЙЛА
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
#         first, second = map(int, f.readline().split())
#
#         graph[first].append(second)
#         graph[second].append(first)
#
# print(graph)
