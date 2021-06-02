import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

start = [(i, j) for i in range(N) for j in range(M) if graph[i][j] == 1]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    for idx in start:
        x, y = idx
        queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

bfs()

answer = 0
end = False
for a in range(N):
    for b in range(M):
        if graph[a][b] == 0:
            print(-1)
            end = True
            break
        else:
            answer = max(graph[a][b], answer)
    if end == True:
        break
else:
    print(answer-1)