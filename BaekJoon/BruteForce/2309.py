import sys
input = sys.stdin.readline


heights = []
for _ in range(9):
    heights.append(int(input()))

for i in range(9):
    lst = heights.copy()
    del lst[i]
    for j in range(8):
        lst2 = lst.copy()
        del lst2[j]
        if sum(lst2) == 100:
            break
    if sum(lst2) == 100:
        for a in sorted(lst2):
            print(a)
        break
