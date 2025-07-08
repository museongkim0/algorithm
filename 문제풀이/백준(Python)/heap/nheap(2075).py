import sys

import heapq

N = int(sys.stdin.readline().rstrip())
heap = []

for _ in range(N):
    for i in list(map(int,sys.stdin.readline().rstrip().split())):
        if len(heap) < 5:
            heapq.heappush(heap, i)
        else:
            if heap[0] < i:
                heapq.heappop(heap)
                heapq.heappush(heap, i)

print(heap[0])