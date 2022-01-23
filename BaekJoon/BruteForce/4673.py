import sys
input = sys.stdin.readline

numbers = set(range(1, 10001))
not_selfnum = set()
for i in range(1, 10001):
    temp = i
    for j in range(len(str(i))):
        temp += int(str(i)[j])
    not_selfnum.add(temp)
for num in sorted(list(numbers-not_selfnum)):
    print(num)