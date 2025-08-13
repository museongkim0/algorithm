import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

S = {}
count = 0

for _ in range(N):
    S[sys.stdin.readline().rstrip()] = 1
    
for _ in range(M):
    if sys.stdin.readline().rstrip() in S:
        count += 1

print(count)