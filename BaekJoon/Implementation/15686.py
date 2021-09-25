import sys
input = sys.stdin.readline
from itertools import combinations


N, M = map(int, input().split())
chicken = []
home = []
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        if temp[j] == 1:
            home.append((i+1, j+1))
        elif temp[j] == 2:
            chicken.append((i+1, j+1))
cases = list(combinations(chicken, M))

answer = 100000000
for i in range(len(cases)):
    city = 0
    for j in range(len(home)):
        dist = 100
        for k in range(M):
            dist = min(dist, abs(cases[i][k][0]-home[j][0]) + abs(cases[i][k][1]-home[j][1]))
        city += dist
    answer = min(answer, city)
print(answer)