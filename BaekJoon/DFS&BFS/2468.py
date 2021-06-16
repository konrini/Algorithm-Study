import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

mountain = []
num = set()
for _ in range(N):
    temp = list(map(int, input().split()))
    mountain.append(temp)
    for i in temp:
        num.add(i)
num = list(num)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    max_area = 1
    for number in num:
        cnt = 0
        graph = [[0 if mountain[b][a] > number else 1 for a in range(N)] for b in range(N)]
        queue = deque()
        for i in range(N):
            for j in range(N):
                if graph[i][j] == 1:
                    continue
                queue.append((i, j))
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx<0 or ny<0 or nx>=N or ny>=N:
                            continue
                        if graph[nx][ny] == 1:
                            continue
                        if graph[nx][ny] == 0:
                            graph[nx][ny] = 1
                            queue.append((nx, ny))
                cnt += 1
        max_area = max(cnt, max_area)
    print(max_area)

bfs()