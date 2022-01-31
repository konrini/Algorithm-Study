from itertools import combinations

def solution(n, info):
    answer = []
    max_diff = 0
    lower_score = 0
    for i in range(1, 12):
        for j in list(combinations(range(11), i)):
            ryan = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            shoot = n
            for k in j:
                if info[k] < shoot:
                    ryan[k] = info[k] + 1
                    shoot -= ryan[k]
            if shoot > 0:
                ryan[-1] = shoot
            score_ryan = 0
            score_appeach = 0
            score_cnt = 0
            if sum(ryan) == n:
                for l in range(11):
                    if ryan[l] == 0 and info[l] == 0:
                        continue
                    elif ryan[l] > info[l]:
                        score_ryan += 10-l
                        score_cnt += l
                    else:
                        score_appeach += 10-l
            if (score_ryan - score_appeach) == max_diff:
                if score_cnt > lower_score:
                    answer = ryan
                    lower_score = score_cnt
            elif (score_ryan - score_appeach) > max_diff:
                max_diff = score_ryan - score_appeach
                answer = ryan
                lower_score = score_cnt
    if max_diff == 0:
        return [-1]
    return answer