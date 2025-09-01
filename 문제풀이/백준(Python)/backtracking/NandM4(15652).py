import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())

n_list = [str(i) for i in range(1, N+1)]

stack = deque()

for i in n_list:
    stack.append([i])
    while len(stack) != 0:
        pop_val = stack.pop()
        if len(pop_val) == M:
            print(' '.join(pop_val))
            continue
        for j in sorted(n_list, reverse=True):
            copy_pop_val = pop_val.copy()
            if copy_pop_val[-1] <= j:
                copy_pop_val.append(j)
                stack.append(copy_pop_val)