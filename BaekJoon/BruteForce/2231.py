import sys
input = sys.stdin.readline


a = input().strip()
if int(a)-len(a)*9 < 0:
    ranges = 0
else:
    ranges = int(a)-len(a)*9
for i in range(ranges, int(a)+1):
    ans = i
    for j in list(str(i)):
        ans += int(j)
    if ans == int(a):
        print(i)
        break
else:
    print(0)