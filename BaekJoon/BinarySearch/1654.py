import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())

numbers = []
for _ in range(N):
    numbers.append(int(input()))
numbers = sorted(numbers)

start = 0
end = numbers[-1]
while start <= end:    
    mid = (start + end)//2
    answer = 0
    for i in numbers:
        answer += i // mid
    if answer < K:
        end = mid - 1
    elif answer >= K:
        start = mid + 1
print(end)
print(start)