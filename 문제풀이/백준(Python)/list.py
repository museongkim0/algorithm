import sys
# 입력 처리
n = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
v = int(sys.stdin.readline().strip())

count = 0
for i in range(n):
    if A[i] == v:
        count += 1
        
print(count)