import sys

N = int(sys.stdin.readline().rstrip())

unordered_map = {}
for i in list(map(int, sys.stdin.readline().rstrip().split())):
    unordered_map[i] = 1

M = int(sys.stdin.readline().rstrip())

answer_list = []

for j in list(map(int, sys.stdin.readline().rstrip().split())):
    if j in unordered_map:
        answer_list.append('1')
    else:
        answer_list.append('0')
    
print(' '.join(answer_list))