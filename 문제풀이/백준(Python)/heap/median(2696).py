import sys

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    n = int(sys.stdin.readline().rstrip())
    print(int(n/2)+1)
    matrix = []
    for _ in range(n//10+1):
        matrix.extend(list(map(int,sys.stdin.readline().rstrip().split())))
    result=[str(sorted(matrix[:i])[int(i/2)]) for i in range(1,n+1,2)]
    for j in range(len(result)//10+1):
        print(' '.join(result[10*j:10*(j+1)]))
