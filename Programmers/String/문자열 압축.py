from collections import deque


def solution(s):
    ans = 1000
    for steps in range(1, len(s)+1):
        answer = []
        lst = [s[i:i+steps] for i in range(0, len(s), steps)]
        lst = deque(lst)
        count = 1
        while lst:
            temp = lst.popleft()
            while len(lst)>=1 and temp == lst[0]:
                lst.popleft()
                count += 1
            else:
                if count == 1:
                    answer.append(temp)
                    count = 1
                else:
                    answer.append(str(count))
                    answer.append(temp)
                    count = 1
        ans = min(len(''.join(answer)), ans)
    return ans