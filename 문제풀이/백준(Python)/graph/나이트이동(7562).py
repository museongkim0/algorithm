import sys
from collections import deque

N = int(sys.stdin.readline().strip())

for _ in range(0, N):
    I = int(sys.stdin.readline().strip())
    start = list(map(int, sys.stdin.readline().rstrip().split()))
    end = list(map(int, sys.stdin.readline().rstrip().split()))
    visited = [[0]*(I) for _ in range(I)]
    queue = deque()
    queue.append([0, start])
    visited[start[0]][start[1]] = 1
    while len(queue) != 0:
        pop_val = queue.popleft()
        level = pop_val[0]
        current = pop_val[1]
        if current == end:
            print(level)
            break
        
        next_pos = [[current[0]+2, current[1]-1], [current[0]-2, current[1]-1], [current[0]+1, current[1]-2], [current[0]-1, current[1]-2],
                    [current[0]+2, current[1]+1], [current[0]-2, current[1]+1], [current[0]+1, current[1]+2], [current[0]-1, current[1]+2],]
        
        for i, j in next_pos:
            if 0 <= i <= I-1 and 0 <= j <= I-1 and visited[i][j] == 0:
                visited[i][j] = 1
                queue.append([level+1, [i, j]])