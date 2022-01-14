import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().strip().split())
graph = []
ice = deque()
for i in range(N):
    graph.append(list(map(int, input().strip().split())))
    for j in range(M):
        if graph[-1][j] != 0:
            ice.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

year = -1
def bfs():
    global year
    year += 1
    melt = {}  # 녹을 개수
    # 덩어리 체크
    queue = deque()
    queue.append(ice[0])
    melt[ice[0]] = 0
    visited_cnt = 1
    while queue:
        x, y = queue.popleft()
        # 주위에 바다 개수
        water = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if graph[nx][ny] == 0:
                water += 1
                continue
            if (nx, ny) not in melt:
                queue.append((nx, ny))
                melt[(nx, ny)] = 0
                visited_cnt += 1
        melt[(x, y)] = water
    if visited_cnt < len(ice):
        return year
    # 빙산 녹기
    for _ in range(len(ice)):
        a, b = ice.popleft()
        if melt[(a, b)] >= graph[a][b]:
            graph[a][b] = 0
        else:
            graph[a][b] -= melt[(a, b)]
            ice.append((a, b))

while True:
    if len(ice) == 0:
        print(0)
        break
    ans = bfs()
    if ans:
        print(ans)
        break
