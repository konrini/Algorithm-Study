import itertools

T = int(input())
for test_case in range(1, T + 1):
    D, W, K = map(int, input().split())
    info = []
    for _ in range(D):
        info.append(list(map(int, input().split())))
    for i in range(0, D+1):
        lst = list(itertools.combinations(range(D), i))
        color = list(itertools.product([0, 1], repeat=i))
        for j in range(len(lst)):
            temp = info[:]
            for l in range(len(color)):
                for k in range(len(lst[j])):
                    temp[lst[j][k]] = [color[l][k]] * W
                for w in range(W):
                    cnt_A = 0
                    cnt_B = 0
                    check = False
                    for d in range(D):
                        if temp[d][w] == 0:
                            cnt_A += 1
                            cnt_B = 0
                        elif temp[d][w] == 1:
                            cnt_B += 1
                            cnt_A = 0
                        if cnt_A >= K or cnt_B >= K:
                            check = True
                            break
                    if not check:
                        break
                if check:
                    break
            if check:
                break
        if check:
            break
    print(f'#{test_case} {i}')
