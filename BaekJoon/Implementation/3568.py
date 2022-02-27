import sys
input = sys.stdin.readline
lst = list(input().split())
ans = [lst[0] for _ in range(len(lst)-1)]
for i in range(1, len(lst)):
    name = ""
    temp = ""
    for j in lst[i]:
        if j in "*[]&":
            temp += j
        elif j in ",;":
            continue
        else:
            name += j
    for t in range(len(temp)-1, -1, -1):
        if temp[t] == "]":
            continue
        elif temp[t] == "[":
            ans[i-1] += "[]"
            continue
        ans[i-1] += temp[t]
    ans[i-1] += " " + name + ";"
for a in ans:
    print(a)
