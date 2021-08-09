def solution(scores):
    answer = ''
    for i in range(len(scores)):
        my_score = scores[i][i]
        score = []
        for j in range(len(scores[i])):
            score.append(scores[j][i])
        score.sort()
        if my_score == score[0]:
            if my_score == score[1]:
                scr = sum(score) / len(score)
            else:
                scr = sum(score[1:]) / len(score[1:])
        elif my_score == score[-1]:
            if my_score == score[-2]:
                scr = sum(score) / len(score)
            else:
                scr = sum(score[:-1]) / len(score[:-1])
        else:
            scr = sum(score) / len(score)
        if scr >= 90:
            answer += 'A'
        elif scr >= 80:
            answer += 'B'
        elif scr >= 70:
            answer += 'C'
        elif scr >= 50:
            answer += 'D'
        else:
            answer += 'F'
    return answer