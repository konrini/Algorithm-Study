from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
N = []
start = []
end = []
for _ in range(t):
    N.append(int(input()))
    start.append(tuple(map(int, input().split())))
    end.append(tuple(map(int, input().split())))

dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2, -2, 1, -1, -2, 2, -1, 1]

def bfs(cases):
    queue = deque()
    queue.append(start[cases])
    while queue:
        x, y = queue.popleft()
        if x == end[cases][0] and y == end[cases][1]:
            return graph[end[cases][0]][end[cases][1]]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=N[cases] or ny>=N[cases]:
                continue
            if graph[nx][ny] != 0:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[end[cases][0]][end[cases][1]]

for cases in range(t):
    graph = [[0 for _ in range(N[cases])] for _ in range(N[cases])]
    print(bfs(cases))