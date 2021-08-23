from collections import deque 


def solution(priorities, location):
    answer = 0
    seq = deque()
    for i in range(len(priorities)):
        seq.append((i, priorities[i]))
    printer = []
    while seq:
        x, y = seq.popleft()
        for i in range(len(seq)):
            if y < seq[i][1]:
                seq.append((x, y))
                break
        else:
            printer.append((x, y))
    for i in range(len(printer)):
        if printer[i][0] == location:
            answer = i+1
            break
    return answer