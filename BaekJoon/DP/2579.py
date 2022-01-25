import sys
input = sys.stdin.readline

N = int(input().strip())
stairs, dp = [0], [0]*(N+1)
for _ in range(N):
    stairs.append(int(input().strip()))

try:
    dp[1] = stairs[1]
    dp[2] = max(dp[1] + stairs[2], stairs[2])
    dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])
    for i in range(4, N+1):
        dp[i] = max(stairs[i-1] + dp[i-3] + stairs[i], dp[i-2] + stairs[i])
    print(dp[N])
except IndexError:
    print(dp[N])