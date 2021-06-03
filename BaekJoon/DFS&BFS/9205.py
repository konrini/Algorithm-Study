import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

graph = []
visited = []
for i in range(t):
    n = int(input())
    temp1 = []
    temp2 = []
    for j in range(n+2):
        temp1.append(list(map(int, input().split())))
        temp2.append(False)
    graph.append(temp1)
    visited.append(temp2)

def bfs():
    for idx in range(len(graph)):
        queue = deque()
        queue.append((graph[idx][0][0], graph[idx][0][1]))
        visited[idx][0] = True
        while queue:
            x, y = queue.popleft()
            for i in range(len(graph[idx])):
                if visited[idx][i] == False and (abs(x-graph[idx][i][0]) + abs(y-graph[idx][i][1])) <= 1000:
                    queue.append((graph[idx][i][0], graph[idx][i][1]))
                    visited[idx][i] = True
                else:
                    continue
        if False == visited[idx][-1]:
            print('sad')
        else:
            print('happy')
bfs()
