import sys
input = sys.stdin.readline

N = int(input())

schedule = []
for _ in range(N):
    start, end = map(int, input().split())
    schedule.append((start, end))
schedule = sorted(schedule, key=lambda x: (x[1], x[0]))

count = 1
end_time = schedule[0][1]
for a in range(1, len(schedule)):
    if end_time <= schedule[a][0]:
        count += 1
        end_time = schedule[a][1]
print(count)