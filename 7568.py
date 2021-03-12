import sys
input = sys.stdin.readline

N = int(input())

dungchi_list = []
for _ in range(N):
    a, b = map(int, input().split())
    dungchi_list.append((a, b))

result = []
for i in range(len(dungchi_list)):
    count = 1
    for j in range(len(dungchi_list)):
        if dungchi_list[i][0] < dungchi_list[j][0] and dungchi_list[i][1] < dungchi_list[j][1]:
            count += 1
    result.append(count)

for k in range(len(result)):
    print(result[k], end=' ')