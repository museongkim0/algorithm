from collections import deque


def bfs(graph, data):
    visited = set()
    level = []
    queue = deque()

    queue.append(data)
    while len(queue) != 0:
        roof_count = len(queue)
        for _ in range(roof_count):
            pop_var = queue.popleft()
            visited.add(pop_var)
            for i in graph.graph[pop_var]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
        level.append(list(queue))

    return list(level[-2])