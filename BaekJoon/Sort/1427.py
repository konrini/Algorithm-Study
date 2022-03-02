import sys
input = sys.stdin.readline

num = list(input().strip())
num.sort(reverse=True)
for i in num:
    print(i, end="")