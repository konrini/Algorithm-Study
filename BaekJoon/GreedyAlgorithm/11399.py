import sys
input = sys.stdin.readline

num = int(input())
time = list(map(int, input().split()))
time.sort()
ans = 0
for i in range(1, num+1):
    ans += sum(time[:i])
print(ans)