def solution(n, arr1, arr2):
    answer = []
    for v1, v2 in zip(arr1, arr2):
        s = '{0:b}'.format(v1|v2).zfill(n)
        temp = ''
        for ch in s:
            if ch == '0':
                temp += ' '
            else:
                temp += '#'
        answer.append(temp)
    return answer