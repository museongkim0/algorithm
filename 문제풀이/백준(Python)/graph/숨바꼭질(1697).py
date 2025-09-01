import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())

visited = {}
queue = deque()
queue.append([0, N])
visited[N] = 1
while len(queue) != 0:
    pop_val = queue.popleft()
    level = pop_val[0]
    current = pop_val[1]
    if current == K:
        print(level)
        break
    if 0 <= current-1 <= 100000 and visited.get(current-1) is None:
        visited[current-1] = 1
        queue.append([level+1, current-1])
    if 0 <= current+1 <= 100000 and visited.get(current+1) is None:
        visited[current+1] = 1
        queue.append([level+1, current+1])
    if 0 <= 2*current <= 100000 and visited.get(2*current) is None:
        visited[2*current] = 1
        queue.append([level+1, 2*current])