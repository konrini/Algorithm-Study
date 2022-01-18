import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())


def bfs():
    queue = deque()
    queue.append(N)
    visited = {}
    visited[N] = 0
    while queue:
        loc = queue.popleft()
        if loc == K:
            break
        if (0<=loc+1<=100000) and loc+1 not in visited:
            visited[loc+1] = visited[loc]+1
            queue.append(loc+1)
        if (0<=loc-1<=100000) and loc-1 not in visited:
            visited[loc-1] = visited[loc]+1
            queue.append(loc-1)
        if (0<=loc*2<=100000) and loc*2 not in visited:
            visited[loc*2] = visited[loc]+1
            queue.append(loc*2)
    return visited[loc]

print(bfs())