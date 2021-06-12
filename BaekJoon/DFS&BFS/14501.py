import sys
input = sys.stdin.readline


N = int(input())
TP = []
for i in range(N):
    TP.append(tuple(map(int, input().split())))
    if N-i < TP[-1][0]:
        TP.pop()
        TP.append((1, 0))

ans = 0
def dfs(idx, cost):
    global ans
    if idx >= N:
        if ans < cost:
            ans = cost
        return
    dfs(idx+1, cost)
    dfs(idx+TP[idx][0], cost+TP[idx][1])

dfs(0, 0)
print(ans)