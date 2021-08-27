def solution(N, stages):
    stages.sort(reverse=True)
    answer = []
    
    for i in range(N):
        cnt = 0
        for j in range(len(stages)):
            if stages[j] >= i+1:
                cnt += 1
            else:
                break
        if cnt == 0:
            answer.append((i+1, 0))
            continue
        answer.append((i+1, stages.count(i+1)/cnt))
    answer = sorted(answer, key = lambda x:(-x[1], x[0]))
    
    ans = []
    for num in answer:
        ans.append(num[0])
    
    return ans