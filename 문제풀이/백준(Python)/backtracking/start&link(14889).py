import sys
from collections import deque

N  = int(sys.stdin.readline().strip())
M = int(N/2)

arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

stat = {}
for x in range(0, N-1):
    for y in range(x+1, N):
        stat[(x,y)] = arr[x][y] + arr[y][x]

stack = deque()

n_list = [i for i in range(N)]

answer = []

stack.append([0])
while len(stack) != 0:
    pop_val = stack.pop()
    if len(pop_val) == M:
        pop_val_reverse = n_list.copy()
        for k in range(0, M):
            pop_val_reverse.remove(pop_val[k])
        stat1 = 0
        stat2 = 0
        for x in range(0, M-1):
            for y in range(x+1, M):
                stat1 += stat[(pop_val[x], pop_val[y])]
                stat2 += stat[(pop_val_reverse[x], pop_val_reverse[y])]
        answer.append(abs(stat1-stat2))
        continue
    for j in n_list[pop_val[-1]:]:
        if j > pop_val[-1]:
            copy_pop_val = pop_val.copy()
            copy_pop_val.append(j)
            stack.append(copy_pop_val)

print(min(answer))