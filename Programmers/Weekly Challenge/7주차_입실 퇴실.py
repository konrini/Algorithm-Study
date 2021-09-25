def solution(enter, leave):
    room = []
    meet = {}
    while enter:
        if leave[0] not in room:
            while leave[0] not in room:
                person = enter.pop(0)
                room.append(person)
            for i in range(len(room)):
                if room[i] not in meet:
                    meet[room[i]] = set()
                for j in range(len(room)):
                    if i == j:
                        continue
                    else:
                        meet[room[i]].add(room[j])
        left = leave.pop(0)
        room.remove(left)
    temp = sorted(list(meet.items()))
    answer = []
    for i in temp:
        answer.append(len(i[1]))
    return answer