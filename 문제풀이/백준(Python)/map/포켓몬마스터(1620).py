import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

dict1 = {}
dict2 = {}

for i in range(1, N+1):
    name = sys.stdin.readline().rstrip()
    dict1[name] = i
    dict2[i] = name

for _ in range(M):
    out = sys.stdin.readline().rstrip()
    if out in dict1:
        print(dict1[out])
    else:
        print(dict2[int(out)])