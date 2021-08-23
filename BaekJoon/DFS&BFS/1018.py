import sys
input = sys.stdin.readline
from collections import deque
from copy import deepcopy


N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(input().strip()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs_W():
    visited = [[False for _ in range(8)] for _ in range(8)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    new_graph = [graph_temp[a+i][b:b+8] for i in range(8)]
    if new_graph[0][0] == 'W':
        cnt = 0
    elif new_graph[0][0] == 'B':
        new_graph[0][0] = 'W'
        cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= 8 or ny >= 8:
                continue
            if visited[nx][ny] == False:
                if new_graph[nx][ny] == new_graph[x][y]:
                    if new_graph[x][y] == 'B':
                        new_graph[nx][ny] = 'W'
                    elif new_graph[x][y] == 'W':
                        new_graph[nx][ny] = 'B'
                    cnt += 1
                queue.append((nx, ny))
                visited[nx][ny] = True
    return cnt

def bfs_B():
    visited = [[False for _ in range(8)] for _ in range(8)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    new_graph = [graph_temp[a+i][b:b+8] for i in range(8)]
    if new_graph[0][0] == 'B':
        cnt = 0
    elif new_graph[0][0] == 'W':
        new_graph[0][0] = 'B'
        cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= 8 or ny >= 8:
                continue
            if visited[nx][ny] == False:
                if new_graph[nx][ny] == new_graph[x][y]:
                    if new_graph[x][y] == 'B':
                        new_graph[nx][ny] = 'W'
                    elif new_graph[x][y] == 'W':
                        new_graph[nx][ny] = 'B'
                    cnt += 1
                queue.append((nx, ny))
                visited[nx][ny] = True
    return cnt

ans = 32
for a in range(N-8+1):
    for b in range(M-8+1):
        graph_temp = deepcopy(graph)
        ans = min(ans, bfs_B(), bfs_W())
print(ans)
