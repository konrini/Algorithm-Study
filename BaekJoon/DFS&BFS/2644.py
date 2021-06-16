import sys
input = sys.stdin.readline
from collections import deque


n = int(input())

target1, target2 = map(int, input().split())

temp = int(input())
graph = {}
for _ in range(temp):
    a, b = map(int, input().split())
    if graph.get(a):
        graph[a].append(b)
        if graph.get(b):
            graph[b].append(a)
        else:
            graph[b] = []
            graph[b].append(a)
    else:
        graph[a] = []
        graph[a].append(b)
        if graph.get(b):
            graph[b].append(a)
        else:
            graph[b] = []
            graph[b].append(a)

visited = [False] * (n+1)

def bfs():
    queue = deque()
    queue.append((target1,0))
    visited[target1] = True
    while queue:
        x,count = queue.popleft()
        if x == target2:
            return count
        else:
            for i in range(len(graph[x])):
                if visited[graph[x][i]] == False:
                    queue.append((graph[x][i],count+1))
                    visited[graph[x][i]] = True
                else:
                    continue
    return -1

print(bfs())