import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph_numbers = []
for _ in range(M):
    a, b = map(int, input().split())
    graph_numbers.append([a, b])

graph = [[] for _ in range(0, N+1)]

for i in range(len(graph)):
    for j in range(len(graph_numbers)):
        if i == graph_numbers[j][0]:
            graph[i].append(graph_numbers[j][1])
        if i == graph_numbers[j][1]:
            graph[i].append(graph_numbers[j][0])
    graph[i] = sorted(graph[i])

visited = [False] * (N + 1)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, V, visited)
print()

visited = [False] * (N + 1)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, V, visited)