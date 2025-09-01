import sys
from collections import deque

N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
operators = list(map(int, sys.stdin.readline().strip().split()))

stack = deque()

max_val = float('-inf')
min_val = float('inf')

stack.append([numbers[0], 1, operators[:]])

while stack:
    current_result, idx, remaining_ops = stack.pop()
    
    if idx == N:
        max_val = max(max_val, current_result)
        min_val = min(min_val, current_result)
        continue
    
    next_number = numbers[idx]
    
    for op_type in range(4):
        if remaining_ops[op_type] > 0:
            new_remaining = remaining_ops[:]
            new_remaining[op_type] -= 1
            
            if op_type == 0:
                new_result = current_result + next_number
            elif op_type == 1:
                new_result = current_result - next_number
            elif op_type == 2:
                new_result = current_result * next_number
            elif op_type == 3:
                new_result = int(current_result / next_number)
            
            stack.append([new_result, idx + 1, new_remaining])

print(max_val)
print(min_val)