import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())

n_list = [str(i) for i in range(1, N+1)]

stack = deque()

answer_list = []

if M != 1:
    cycle_list = n_list[:-M+1]
else:
    cycle_list = n_list.copy()

for i in cycle_list:
    stack.append([i])
    while len(stack) != 0:
        pop_val = stack.pop()
        if len(pop_val) == M and sorted(pop_val) not in answer_list:
            answer_list.append(sorted(pop_val))
            print(' '.join(sorted(pop_val)))
            continue
        for j in sorted(n_list, reverse=True):
            if j not in pop_val:
                copy_pop_val = pop_val.copy()
                copy_pop_val.append(j)
                stack.append(copy_pop_val)