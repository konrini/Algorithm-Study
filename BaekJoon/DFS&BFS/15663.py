import sys
input = sys.stdin.readline


N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))

visited = [False] * N
out = []

def solve(depth, N, M):
    temp = 0
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(len(visited)):
        if temp == numbers[i]:
            continue
        if not visited[i]:
            visited[i] = True
            out.append(numbers[i])
            solve(depth+1, N, M)
            visited[i] = False
            temp = out.pop()

solve(0, N, M)