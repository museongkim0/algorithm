import sys
from collections import deque

N = int(sys.stdin.readline().strip())

map = []
map.append(['0']*(N+2))
for _ in range(0, N):
    map.append(['0']+list(sys.stdin.readline().strip())+['0'])
map.append(['0']*(N+2))

visited = [[0]*(N+1) for _ in range(N+1)]

answer = []
for i in range(1, N+1):
    for j in range(1, N+1):
        if map[i][j] == '1' and visited[i][j] == 0:
            queue = deque()
            queue.append([i,j])
            visited[i][j] = 1
            count = 1
            while len(queue) != 0:
                current = queue.popleft()
                if map[current[0]-1][current[1]] == '1' and visited[current[0]-1][current[1]] == 0:
                    count += 1
                    visited[current[0]-1][current[1]] = 1
                    queue.append([current[0]-1, current[1]])
                if map[current[0]+1][current[1]] == '1' and visited[current[0]+1][current[1]] == 0:
                    count += 1
                    visited[current[0]+1][current[1]] = 1
                    queue.append([current[0]+1, current[1]])
                if map[current[0]][current[1]+1] == '1' and visited[current[0]][current[1]+1] == 0:
                    count += 1
                    visited[current[0]][current[1]+1] = 1
                    queue.append([current[0], current[1]+1])
                if map[current[0]][current[1]-1] == '1' and visited[current[0]][current[1]-1] == 0:
                    count += 1
                    visited[current[0]][current[1]-1] = 1
                    queue.append([current[0], current[1]-1])
            answer.append(count)
            
print(len(answer))
for i in sorted(answer):
    print(i)