import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    queue = deque(cabbage)
    cnt = 0
    while queue:
        x, y = queue.popleft()
        if graph[y][x] == 1:
            graph[y][x] = 0
            cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny <0 or nx >= M or ny >= N:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 2
                queue.remove((nx, ny))
                queue.insert(0, (nx, ny))
    return cnt


for i in range(int(input())):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    cabbage = []
    for j in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
        cabbage.append((x, y))
    print(bfs())
    