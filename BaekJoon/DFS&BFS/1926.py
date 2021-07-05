from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    ans = 0
    cnt = 0
    for a in range(N):
        for b in range(M):
            if graph[a][b] == 0:
                continue
            if graph[a][b] != 0:
                area = 1
                cnt += 1
                queue.append((a, b))
                graph[a][b] = 0
                while queue:
                    x, y = queue.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if nx<0 or ny<0 or nx>=N or ny>=M:
                            continue
                        if graph[nx][ny] == 0:
                            continue
                        if graph[nx][ny] == 1:
                            graph[nx][ny] = 0
                            area += 1
                            queue.append((nx, ny))
                    ans = max(ans, area)
    return cnt, ans

cnt, ans = bfs()
print(cnt)
print(ans)