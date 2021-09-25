def solution(number, k):
    stack = []
    for num in number:
        while stack and stack[-1] < num and k>0:
            k -= 1
            stack.pop()
        stack.append(num)
    return ''.join(stack)[:len(number)-k]