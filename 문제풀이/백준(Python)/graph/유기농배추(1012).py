import sys
from collections import deque

T = int(sys.stdin.readline().strip())
for _ in range(0, T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    ground = [[0]*(N+2) for _ in range(M+2)]
    for _ in range(0, K):
        i, j = map(int, sys.stdin.readline().rstrip().split())
        ground[i+1][j+1] = 1
    
    visited = [[0]*(N+1) for _ in range(M+1)]

    answer = 0
    for i in range(1, M+1):
        for j in range(1, N+1):
            if ground[i][j] == 1 and visited[i][j] == 0:
                queue = deque()
                queue.append([i,j])
                visited[i][j] = 1
                while len(queue) != 0:
                    current = queue.popleft()
                    if ground[current[0]-1][current[1]] == 1 and visited[current[0]-1][current[1]] == 0:
                        visited[current[0]-1][current[1]] = 1
                        queue.append([current[0]-1, current[1]])
                    if ground[current[0]+1][current[1]] == 1 and visited[current[0]+1][current[1]] == 0:
                        visited[current[0]+1][current[1]] = 1
                        queue.append([current[0]+1, current[1]])
                    if ground[current[0]][current[1]+1] == 1 and visited[current[0]][current[1]+1] == 0:
                        visited[current[0]][current[1]+1] = 1
                        queue.append([current[0], current[1]+1])
                    if ground[current[0]][current[1]-1] == 1 and visited[current[0]][current[1]-1] == 0:
                        visited[current[0]][current[1]-1] = 1
                        queue.append([current[0], current[1]-1])
                answer += 1
    print(answer)

