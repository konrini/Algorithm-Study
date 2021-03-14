import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coin_list = []
for _ in range(N):
    a = int(input())
    if a <= K:
        coin_list.append(a)
coin_list = sorted(coin_list, reverse=True)

result = 0
for i in range(len(coin_list)):
    result += K // coin_list[i]
    K = K % coin_list[i]
print(result)