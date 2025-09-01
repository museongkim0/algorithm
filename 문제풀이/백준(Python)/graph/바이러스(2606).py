import sys
from collections import deque

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

graph = {}

for i in range(1, N+1):
   graph[i] = []

for _ in range(0, M):
    from_v, to_v = map(int, sys.stdin.readline().strip().split())
    graph[from_v].append(to_v)
    graph[to_v].append(from_v)

visited = [0] * (N+1)
queue = deque()

queue.append(1)
visited[1] = 1
count = 0
while queue:
    current = queue.popleft()

    for neighbor in graph[current]:
        if visited[neighbor] == 0:
            visited[neighbor] = 1
            count += 1
            queue.append(neighbor)

print(count)