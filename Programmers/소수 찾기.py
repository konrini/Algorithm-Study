from itertools import permutations


def solution(numbers):
    numbers = list(numbers)
    test = []
    for i in range(len(numbers)):
        temp = list(permutations(numbers, i+1))
        for j in range(len(temp)):
            test.append(int(''.join(temp[j])))
        test = list(set(test))
    
    answer = 0
    for i in range(len(test)):
        if test[i] == 0 or test[i] == 1:
            continue
        for j in range(2, int(test[i]/2)+1):
            if test[i] % j == 0:
                break
        else:
            answer += 1
            
    return answer
