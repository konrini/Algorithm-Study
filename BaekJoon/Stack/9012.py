import sys

def check(x):
    stack = []
    for j in x:
        if j != ')':
            stack.append(j)
            continue
        if stack and stack[-1] == '(':
            stack.pop()
        else:
            return False
    if stack != []:
        return False
    return True

for i in range(int(sys.stdin.readline())):
    a = sys.stdin.readline().rstrip()
    if check(a):
        print('YES')
    else:
        print('NO')
