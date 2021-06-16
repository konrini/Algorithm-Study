import sys
input = sys.stdin.readline
from collections import deque


N, M = map(int, input().split())

graph = []
start = []
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(M):
        if graph[-1][j] == 1:
            start.append((i, j))

dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [-1, 0, 1, 1, -1, -1, 0, 1]

def bfs():
    queue = deque()
    dist = 0
    for points in start:
        queue.append(points)
    while queue:
        x, y = queue.popleft()
        for a in range(8):
            nx = x + dx[a]
            ny = y + dy[a]
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            if graph[nx][ny] >= graph[x][y]:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
            dist = max(dist, graph[nx][ny])
    return dist-1

print(bfs())