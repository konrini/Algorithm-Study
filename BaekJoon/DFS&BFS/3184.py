from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(input().strip()))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False for _ in range(C)] for _ in range(R)]

def bfs():
    queue = deque()
    sheep = 0
    wolf = 0
    for a in range(R):
        for b in range(C):
            if graph[a][b] == '.':
                visited[a][b] = True
                continue
            if graph[a][b] == '#' and visited[a][b] == False:
                v = 0
                o = 0
                queue.append((a, b))
                visited[a][b] = True
                while queue:
                    x, y = queue.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if nx<0 or ny<0 or nx>=R or ny>=C:
                            continue
                        if graph[nx][ny] == '#':
                            continue
                        if graph[nx][ny] == '.' and visited[nx][ny] == False:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                            continue
                        if graph[nx][ny] == 'v':
                            v += 1
                            queue.append((nx, ny))
                            visited[nx][ny] = True
                            graph[nx][ny] = '.'
                            continue
                        if graph[nx][ny] == 'o':
                            o += 1
                            queue.append((nx, ny))
                            visited[nx][ny] = True
                            graph[nx][ny] = '.'
                            continue
                if v >= o:
                    wolf += v
                else:
                    sheep += o
    return sheep, wolf

sheep, wolf = bfs()
print(sheep)
print(wolf)