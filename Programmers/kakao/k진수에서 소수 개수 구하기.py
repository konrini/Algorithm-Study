from math import sqrt

def solution(n, k):
    answer = 0
    changed = ''
    while n >= 1:
        changed = str(n % k) + changed
        n = int(n / k)
    splited = list(changed.split('0'))
    for i in splited:
        if i == '' or i == '1':
            continue
        for j in range(2, int(sqrt(int(i)))+1):
            if int(i) % j == 0:
                break
        else:
            answer += 1
    return answer