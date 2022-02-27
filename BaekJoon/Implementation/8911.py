import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    command = input().strip()
    Left = 0
    Right = 0
    Top = 0
    Bottom = 0
    dir = 0  # 위 : 0, 오 : 1, 아 : 2, 왼 : 3
    curr_r = 0
    curr_c = 0
    for c in command:
        if c == "L":
            dir = (dir-1) % 4
        elif c == "R":
            dir = (dir+1) % 4
        elif c == "F":
            if dir == 0:
                curr_r += 1
            elif dir == 1:
                curr_c += 1
            elif dir == 2:
                curr_r -= 1
            elif dir == 3:
                curr_c -= 1
        elif c == "B":
            if dir == 0:
                curr_r -= 1
            elif dir == 1:
                curr_c -= 1
            elif dir == 2:
                curr_r += 1
            elif dir == 3:
                curr_c += 1
        if curr_c < Left:
            Left = curr_c
        if curr_c > Right:
            Right = curr_c
        if curr_r > Top:
            Top = curr_r
        if curr_r < Bottom:
            Bottom = curr_r
    print((Top-Bottom)*(Right-Left))
