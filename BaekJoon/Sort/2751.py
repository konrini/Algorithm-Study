import sys
input = sys.stdin.readline

N = int(input())

Numbers = []
for _ in range(N):
    Numbers.append(int(input()))

Numbers = sorted(list(set(Numbers)))

for i in range(len(Numbers)):
    print(Numbers[i])