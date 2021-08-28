def solution(s):
    lst = s.split(' ')
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    answer = str(min(lst)) + ' ' + str(max(lst))
    return answer