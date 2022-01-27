def solution(id_list, report, k):

    rep_dict = {}
    for i in range(len(report)):
        rep_from, rep_to = report[i].split()
        if rep_from in rep_dict:
            rep_dict[rep_from].add(rep_to)
        else:
            rep_dict[rep_from] = {rep_to}
    
    reported = {}
    for value in rep_dict.values():
        for name in value:
            if name in reported:
                reported[name] += 1;
            else:
                reported[name] = 1;
    
    prohibited = []
    for item in reported.items():
        if item[1] >= k:
            prohibited.append(item[0])

    answer = [0] * len(id_list)
    if len(prohibited) == 0:
        return answer
    else:
        idx = 0
        for id_ in id_list:
            for prh in prohibited:
                if id_ in rep_dict and prh in rep_dict[id_]:
                    answer[idx] += 1
            idx += 1
    return answer