import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

S = {}
answer = []

for _ in range(N):
    S[sys.stdin.readline().rstrip()] = 1
    
for _ in range(M):
    out = sys.stdin.readline().rstrip()
    if out in S:
        answer.append(out)

print(len(answer))
for i in sorted(answer):
    print(i)