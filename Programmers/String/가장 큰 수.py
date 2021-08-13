def solution(numbers):
    
    num = list(map(str, numbers))
    num.sort(key = lambda x:x*3, reverse=True)

    return str(int(''.join(num)))