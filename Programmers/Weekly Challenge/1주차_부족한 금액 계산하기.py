def solution(price, money, count):
    total = price * sum(range(1,count+1))
    if money >= total:
        answer = 0
    else:
        answer = total - money
    return answer