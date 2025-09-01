import sys
sys.setrecursionlimit(150000)

N, M, R = map(int, sys.stdin.readline().strip().split())

graph = {}

for i in range(1, N+1):
   graph[i] = []

for _ in range(0, M):
    from_v, to_v = map(int, sys.stdin.readline().strip().split())
    graph[from_v].append(to_v)
    graph[to_v].append(from_v)

for i in range(1, N+1):
    graph[i].sort(reverse=True) 

visited = [0] * (N+1)
count = 0

def dfs(v):
    global count
    count += 1
    visited[v] = count
    
    for neighbor in graph[v]:
        if visited[neighbor] == 0:
            dfs(neighbor)

dfs(R)

for i in range(1, N+1):
    print(visited[i])