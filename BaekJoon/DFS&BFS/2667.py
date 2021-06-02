import sys
input = sys.stdin.readline

N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int, input().strip())))

count = 0
def dfs(x,y):
    if x<0 or y<0 or x>=N or y>=N:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 2
        global count
        count += 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
answer = []
for i in range(N):
    for j in range(N):
        if dfs(i,j) == True:
            result += 1
            answer.append(count)
            count = 0

print(result)
answer.sort()
for i in answer:
    print(i)