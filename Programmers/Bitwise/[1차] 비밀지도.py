def solution(n, arr1, arr2):
    map1 = []
    map2 = []
    for i in range(n):
        if len(bin(arr1[i])[2:])== n:
            map1.append(list(bin(arr1[i])[2:]))
        else:
            map1.append(list(bin(arr1[i])[2:].zfill(n)))
        if len(bin(arr2[i])[2:])== n:
            map2.append(list(bin(arr2[i])[2:]))
        else:
            map2.append(list(bin(arr2[i])[2:].zfill(n)))

    answer = []
    for a in range(n):
        temp = ''
        for b in range(n):
            if map1[a][b] == '1' or map2[a][b] == '1':
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
    return answer
