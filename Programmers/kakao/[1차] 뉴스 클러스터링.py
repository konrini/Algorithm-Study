def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1_two = []
    for i in range(len(str1)-1):
        if str1[i] not in 'abcdefghijklmnopqrstuvwxyz':
            continue
        if str1[i+1] not in 'abcdefghijklmnopqrstuvwxyz':
            continue
        else:
            str1_two.append(str1[i:i+2])
    
    str2_two = []
    for i in range(len(str2)-1):
        if str2[i] not in 'abcdefghijklmnopqrstuvwxyz':
            continue
        if str2[i+1] not in 'abcdefghijklmnopqrstuvwxyz':
            continue
        else:
            str2_two.append(str2[i:i+2])
    
    temp_list = list(set(str1_two + str2_two))
    both = []
    total = []
    for i in range(len(temp_list)):
        cnt1, cnt2 = 0, 0
        if temp_list[i] in str1_two:
            cnt1 = str1_two.count(temp_list[i])
        if temp_list[i] in str2_two:
            cnt2 = str2_two.count(temp_list[i])
        if cnt1 <= cnt2:
            for _ in range(cnt1):
                both.append(temp_list[i])
            for _ in range(cnt2):
                total.append(temp_list[i])
        if cnt1 > cnt2:
            for _ in range(cnt2):
                both.append(temp_list[i])
            for _ in range(cnt1):
                total.append(temp_list[i])   
    if len(total) == 0:
        return 65536
    answer = int(len(both)/len(total)*65536)
    return answer