import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    if n > 0:
        nums = list(map(int, input()[1:-2].split(",")))
    elif n == 0:
        input()
        nums = []
    point = 0
    for command in p:
        if command == "R":
            point = -(point + 1)
        elif command == "D":
            if len(nums) > 0:
                del nums[point]
            else:
                print("error")
                point = 1
                break
    if point == 1:
        continue
    if point == -1:
        nums.reverse()
    print("[", end="")
    for i in range(len(nums)):
        if i == len(nums)-1:
            print(nums[i], end="")
        else:
            print(nums[i], end=",")
    print("]")