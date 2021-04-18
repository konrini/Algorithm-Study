# s = "[](){}"

def solution(s):
    answer = 0
    for i in range(len(s)):
        t = s[i:] + s[:i]
        if check(t):
            answer += 1
    return answer

def check(s):
    k = {')': '(', '}': '{', ']': '['}
    temp = []
    for j in s:
        if j not in k:
            temp.append(j)
            continue
        if temp and temp[-1] == k[j]:
            temp.pop()
        else:
            return False
    return True

print(solution(s))