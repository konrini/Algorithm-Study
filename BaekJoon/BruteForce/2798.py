import sys
input = sys.stdin.readline

N, M = map(int, input().split())
CARDS = list(map(int, input().split()))

answer = 0
for i in range(len(CARDS)):
    for j in range(i+1, len(CARDS)):
        for k in range(j+1, len(CARDS)):
            result = CARDS[i] + CARDS[j] + CARDS[k]
            if result == M:
                print(result)
                sys.exit(0)
            if result < M:
                answer = max(result, answer)
print(answer)
