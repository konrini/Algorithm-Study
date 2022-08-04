import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
table = deque()
virus = []
for i in range(N):
    table.append(list(map(int, input().split())))
    for j in range(N):
        if table[-1][j] != 0:
            virus.append([table[-1][j], i, j])

virus.sort()
virus = deque(virus)
S, X, Y = map(int, input().split())

dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

while S != 0:
    S -= 1
    for i in range(len(virus)):
        l, r, c = virus.popleft()
        for j in range(4):
            nr = r + dir[j][0]
            nc = c + dir[j][1]
            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue
            if table[nr][nc] == 0:
                table[nr][nc] = l
                virus.append([l, nr, nc])
print(table[X-1][Y-1])
