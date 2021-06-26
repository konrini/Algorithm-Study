def solution(new_id):
    new_id = list(new_id.lower())
    step = []
    for i in range(len(new_id)):
        if step and step[-1] == '.' and new_id[i] == '.':
            continue
        if new_id[i] in 'abcdefghijklmnopqrstuvwxyz0123456789-_.':
            step.append(new_id[i])
    if step and step[0] == '.':
        del step[0]
    if step and step[-1] == '.':
        del step[-1]
    if len(step) == 0:
        step = ['a', 'a', 'a']
    if len(step) >= 16:
        step = step[:15]
        if step[-1] == '.':
            del step[-1]
    if len(step) <= 2:
        if len(step) == 1:
            step = step*3
        elif len(step) == 2:
            step.append(step[-1])
    return ''.join(step)