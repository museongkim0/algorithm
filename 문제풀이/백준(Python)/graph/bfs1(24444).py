import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().strip().split())

graph = {}

for i in range(1, N+1):
   graph[i] = []

for _ in range(0, M):
    from_v, to_v = map(int, sys.stdin.readline().strip().split())
    graph[from_v].append(to_v)
    graph[to_v].append(from_v)

for i in range(1, N+1):
    graph[i].sort() 

visited = [0] * (N+1)
queue = deque()

count = 1
queue.append(R)
visited[R] = count
while queue:
    current = queue.popleft()

    for neighbor in graph[current]:
        if visited[neighbor] == 0:
            count += 1
            visited[neighbor] = count
            queue.append(neighbor)

for i in range(1, N+1):
    print(visited[i])