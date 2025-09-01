import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())

map = []
map.append(['0']*(M+2))
for _ in range(0, N):
    map.append(['0']+list(sys.stdin.readline().strip())+['0'])
map.append(['0']*(M+2))

visited = [[0]*(M+1) for _ in range(N+1)]

queue = deque()
queue.append([1, [1, 1]])
visited[1][1] = 1
while len(queue) != 0:
    pop_val = queue.popleft()
    level = pop_val[0]
    current = pop_val[1]
    if current == [N, M]:
        print(level)
        break
    if map[current[0]-1][current[1]] == '1' and visited[current[0]-1][current[1]] == 0:
        visited[current[0]-1][current[1]] = 1
        queue.append([level+1, [current[0]-1, current[1]]])
    if map[current[0]+1][current[1]] == '1' and visited[current[0]+1][current[1]] == 0:
        visited[current[0]+1][current[1]] = 1
        queue.append([level+1, [current[0]+1, current[1]]])
    if map[current[0]][current[1]+1] == '1' and visited[current[0]][current[1]+1] == 0:
        visited[current[0]][current[1]+1] = 1
        queue.append([level+1, [current[0], current[1]+1]])
    if map[current[0]][current[1]-1] == '1' and visited[current[0]][current[1]-1] == 0:
        visited[current[0]][current[1]-1] = 1
        queue.append([level+1, [current[0], current[1]-1]])
