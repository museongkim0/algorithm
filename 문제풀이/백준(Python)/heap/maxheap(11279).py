import sys

import heapq

N = int(sys.stdin.readline().rstrip())
heap = []

for i in range(N):
    n = int(sys.stdin.readline().rstrip())
    if n > 0:
        heapq.heappush(heap, -n)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))