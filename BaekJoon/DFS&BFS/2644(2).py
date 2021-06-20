import sys
input = sys.stdin.readline
from collections import deque


def bfs(start,goal,total_num):
    visit = [-1] * (total_num + 1)
    q = deque()
    q.append(start)
    visit[start] = 0
    while q :
        now = q.popleft()
        if now == goal :
            return visit[now]
        for i in range(len(relation[now])) :
            next = relation[now][i]
            if visit[next] == -1 :
                q.append(next)
                visit[next] = visit[now] + 1
    return -1

n = int(input())
start, dest = map(int, input().split())
m = int(input())
relation = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)
print(bfs(start,dest,n))