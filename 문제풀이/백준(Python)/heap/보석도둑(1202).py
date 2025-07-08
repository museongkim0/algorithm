import sys
import heapq

N, K = map(int,sys.stdin.readline().rstrip().split())

n_list = []
for _ in range(N):
    n_list.append(list(map(int, sys.stdin.readline().rstrip().split())))
n_list.sort()

k_list = []
for _ in range(K):
    k_list.append(int(sys.stdin.readline().rstrip()))
k_list.sort()

heap = []

idx = 0
result = 0
for i in k_list:
    while idx < N and i >= n_list[idx][0]:
        heapq.heappush(heap, -n_list[idx][1])
        idx +=1
    if heap:
        result += -heapq.heappop(heap)
        
print(result)