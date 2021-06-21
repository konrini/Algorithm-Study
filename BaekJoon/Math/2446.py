import sys
input = sys.stdin.readline


N = int(input())
for i in range(N):
    print(' ' * (i) + '*' * (2*N-2*i-1))
for j in range(N-1, 0, -1):
    print(' ' * (j-1) + '*' * (2*N-2*j+1))