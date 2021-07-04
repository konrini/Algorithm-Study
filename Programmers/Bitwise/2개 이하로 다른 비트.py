def solution(numbers):
    answers = []
    for num in numbers:
        target = bin(num)[2:]
        check = True
        i = 0
        if target[-2:] == '11':
            i += 1
        while check:
            while target[-(2+i):-i] == '11':
                i += 1
            if i == 0:
                answers.append(num+1)
                check = False
            else:
                answers.append(num+2**i)
                check = False
    return answers