import sys
input = sys.stdin.readline


for i in range(int(input())):
    H, W, N = map(int, input().split())
    if N % H == 0:
        hh = H
    else:
        hh = N % H
    if N // H < 1:
        ww = 1
    elif N // H == 1 and N % H == 0:
        ww = 1
    elif N // H > 1 and N % H == 0:
        ww = N // H
    else:
        ww = N // H + 1
    print(str(hh) + str(ww).zfill(2))