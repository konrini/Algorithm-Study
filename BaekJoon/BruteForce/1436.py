import sys
input = sys.stdin.readline


num = int(input())
cnt = 0
temp = 0
for i in range(1, 2666800):
    temp += 1
    if '666' in str(temp):
        cnt += 1
    if cnt == num:
        print(temp)
        break