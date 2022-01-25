import sys
input = sys.stdin.readline

N = int(input().strip())
numbers = list(map(int, input().strip().split()))
line = sorted(set(numbers))
num_dict = {}
for i, val in enumerate(line):
    num_dict[val] = i
for ans in numbers:
    print(num_dict[ans], end=' ')