def solution(board, moves):
    lst = []
    answer = 0
    for i in moves:
        for j in range(len(board[0])):
            if board[j][i-1] == 0:
                continue
            else:
                if lst and lst[-1] == board[j][i-1]:
                    lst.pop()
                    board[j][i-1] = 0
                    answer += 2
                    break
                else:
                    lst.append(board[j][i-1])
                    board[j][i-1] = 0
                    break
    return answer