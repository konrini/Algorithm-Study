import sys
input = sys.stdin.readline

N = int(input())
V = int(input())

computers = []
for i in range(V):
    a, b = map(int, input().split())
    computers.append([a, b])

graph = [[] for _ in range(N+1)]
for j in range(N+1):
    for i in range(len(computers)):
        if computers[i][0] == j:
            graph[j].append(computers[i][1])
        if computers[i][1] == j:
            graph[j].append(computers[i][0])

visited = [False] * (N + 1)

count = []
def dfs(graph, v, visited):
    visited[v] = True
    count.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)
ans = len(count)-1
print(ans)
