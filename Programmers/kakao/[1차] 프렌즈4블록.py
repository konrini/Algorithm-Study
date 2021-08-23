def bomb(m, n, board):
    delete = []
    for i in range(m - 1):
        for j in range(n - 1):
            if board[i][j] == 0:
                continue
            if board[i][j] == board[i + 1][j] and board[i][j] == board[i][j + 1] and board[i][j] == board[i + 1][j + 1]:
                delete.append((i, j))
                delete.append((i, j + 1))
                delete.append((i + 1, j))
                delete.append((i + 1, j + 1))
            else:
                continue
    delete = list(set(delete))
    cnt = len(delete)
    for k in range(cnt):
        board[delete[k][0]][delete[k][1]] = 0
    return cnt

def gravity(m, n, board):
    for i in range(m - 1, 0, -1):
        for j in range(n):
            if board[i][j] == 0:
                if i == 0:
                    continue
                k = 0
                while i - k >= 0 and board[i - k][j] == 0:
                    k += 1
                if i - k == -1:
                    continue
                board[i][j] = board[i - k][j]
                board[i - k][j] = 0

def solution(m, n, board):
    new = []
    for i in range(len(board)):
        new.append(list(board[i]))
    board = new
    answer = 0
    cnt = bomb(m, n, board)
    while cnt != 0:
        answer += cnt
        gravity(m, n, board)
        cnt = bomb(m, n, board)
    answer += cnt
    return answer
