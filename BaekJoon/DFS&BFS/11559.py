from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

graph = []
mark = 12
for m in range(12):
    graph.append(list(input().strip()))
    if graph[-1] != ['.', '.', '.', '.', '.', '.']:
        mark = min(mark, m)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    queue = deque()
    for a in range(mark, 12):
        for b in range(6):
            if graph[a][b] == '.':
                continue
            else:
                queue.append((a, b))
                color = graph[a][b]
                temp = []
                temp.append((a, b))
                graph[a][b] = '.'
                while queue:
                    x, y = queue.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if nx<0 or ny<0 or nx>=12 or ny>=6:
                            continue
                        if graph[nx][ny] != color:
                            continue
                        if graph[nx][ny] == color:
                            queue.append((nx, ny))
                            temp.append((nx, ny))
                            graph[nx][ny] = '.'
                if len(temp) >= 4:
                    for puyo in temp:
                        graph[puyo[0]][puyo[1]] = '.'
                else:
                    for puyo in temp:
                        graph[puyo[0]][puyo[1]] = color

def gravity():
    for a in range(11, mark-1, -1):
        for b in range(6):
            if graph[a][b] == '.':
                if a == 0:
                    continue
                i = 1
                if graph[a-i][b] == '.':
                    while i < a:
                        i += 1
                        if graph[a-i][b] != '.':
                            break
                graph[a][b] = graph[a-i][b]
                graph[a-i][b] = '.'
            else:
                continue

cnt = 0
while True:
    b_g = deepcopy(graph)
    bfs()
    a_g = graph
    if b_g == a_g:
        print(cnt)
        break
    cnt += 1
    gravity()