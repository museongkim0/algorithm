import sys

N = int(sys.stdin.readline().rstrip())

map = {}

for _ in range(N):
    out = sys.stdin.readline().rstrip().split()
    if out[1] == 'enter':
        map[out[0]] = 1
    else:
        map.pop(out[0])
        
for i in sorted(list(map.keys()), reverse=True):
    print(i)

