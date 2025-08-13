import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

S = {}
answer = N+M

for i in sys.stdin.readline().rstrip().split():
    S[i] = 1
    
for j in sys.stdin.readline().rstrip().split():
    if j in S:
        answer -= 2

print(answer)