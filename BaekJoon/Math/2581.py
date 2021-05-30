M = int(input())
N = int(input())
count = []
for i in range(M, N+1):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        count.append(i)
if count == []:
    print(-1)
else:
    print(sum(count))
    print(count[0])