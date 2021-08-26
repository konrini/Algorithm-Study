from itertools import combinations


def solution(orders, course):
    answer = []
    for num in course:
        temp_list = []
        for i in range(len(orders)):
            temp = list(combinations(orders[i], num))
            for j in temp:
                t = ''.join(j)
                temp_list.append(tuple(sorted(t)))
        menu = list(set(temp_list))
        ord = []
        for i in range(len(menu)):
            cnt = 0
            for j in range(len(orders)):
                for k in range(num):
                    if menu[i][k] not in orders[j]:
                        break
                else:
                    cnt += 1
            ord.append((''.join(sorted(menu[i])), cnt))
        ord = sorted(ord, key = lambda x:(-x[1], x[0]))
        if ord:
            count = ord[0][1]
        if count >= 2:
            check = True
        while check:
            for i in range(len(ord)):
                if ord[i][1] == count:
                    answer.append(ord[i][0])
                else:
                    check = False
                    break
    return sorted(answer)