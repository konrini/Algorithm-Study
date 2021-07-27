def solution(a, b):
    days = [31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
    if a == 1:
        ans = b
    else:
        ans = days[a-2] + b
    week = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    answer = week[ans % 7]
    return answer