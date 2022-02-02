import sys
input = sys.stdin.readline
import heapq


heap = []
N = int(input().strip())
for _ in range(N):
    x = int(input().strip())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -x)