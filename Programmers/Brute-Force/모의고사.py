def solution(answers):
    answer = []
    counts = []
    type = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for i in range(3):
        count = 0
        for j in range(len(answers)):
            if answers[j] == type[i][j%len(type[i])]:
                count += 1
        if len(answer) == 0:
            counts.append(count)
            answer.append(i+1)
        else:
            if counts[-1] > count:
                pass
            elif counts[-1] == count:
                answer.append(i+1)
            else:
                answer = []
                counts.append(count)
                answer.append(i+1)
    return answer