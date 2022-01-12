import sys
input = sys.stdin.readline

num = int(input())
fibonacci = [0, 1]
if num == 0:
    print(fibonacci[0])
elif num == 1:
    print(fibonacci[1])
else:
    i = 2
    while len(fibonacci) != num+1:
        fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
        i += 1
    print(fibonacci[num])