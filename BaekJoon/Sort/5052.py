import sys


t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    phone_list = []
    for j in range(n):
        phone_list.append(str(sys.stdin.readline().strip()))
    phone_list.sort()
    for k in range(len(phone_list)-1):
        if phone_list[k+1].startswith(phone_list[k]):
            print('NO')
            break
    else:
        print('YES')