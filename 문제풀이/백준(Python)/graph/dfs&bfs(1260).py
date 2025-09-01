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
dfs_answer = []

def dfs(v):
    visited[v] = 1
    dfs_answer.append(str(v))
    
    for neighbor in graph[v]:
        if visited[neighbor] == 0:
            dfs(neighbor)

dfs(R)

def bfs(v):
    visited = [0] * (N+1)
    bfs_answer = []
    queue = deque()
    queue.append(v)
    visited[v] = 1
    bfs_answer.append(str(v))
    while queue:
        current = queue.popleft()

        for neighbor in graph[current]:
            if visited[neighbor] == 0:
                visited[neighbor] = 1
                bfs_answer.append(str(neighbor))
                queue.append(neighbor)
    
    return bfs_answer

bfs_answer = bfs(R)

print(' '.join(dfs_answer))
print(' '.join(bfs_answer))