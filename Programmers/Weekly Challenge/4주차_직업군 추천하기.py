def solution(table, languages, preference):
    new_table = []
    for i in range(5):
        new_table.append(list(table[i].split(' ')))
    table = new_table
    cnt = 0
    answer = 'Z'
    for a in range(5):
        temp = 0
        for i in range(len(languages)):
            for b in range(6):
                if languages[i] == table[a][b]:
                    temp += (6-b)*preference[i]
        if temp == cnt and ord(answer[0]) > ord(table[a][0][0]):
            cnt = temp
            answer = table[a][0]
        elif temp > cnt:
            cnt = temp
            answer = table[a][0]
    return answer