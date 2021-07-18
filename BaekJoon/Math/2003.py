import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = 0
for i in range(N):
    sums = numbers[i]
    while sums < M:
        i += 1
        if i == N:
            break
        sums += numbers[i]
    if sums == M:
        cnt += 1
        continue
print(cnt)