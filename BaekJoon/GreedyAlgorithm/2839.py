import sys
input = sys.stdin.readline

num = int(input())
for i in range(num//5, -1, -1):
    if (num-5*i) % 3 == 0:
        print(i + (num-5*i) // 3)
        break
else:
    print(-1)