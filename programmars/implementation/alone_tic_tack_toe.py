import sys
input = sys.stdin.readline

def check_line(board):
    answer = 0 
    success_list = [] 
    for i in range(3):
        if board[0][i] != '.' and board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            answer +=1
            success_list.append(board[0][i])
        if board[i][0] != '.' and board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            answer +=1
            success_list.append(board[i][0])
    if board[0][0] != '.' and board[0][0] == board[1][1] == board[2][2]:
        answer += 1
        success_list.append(board[0][0])
    if board[0][2] != '.' and board[0][2] == board[1][1] == board[2][0]:
        answer += 1
        success_list.append(board[0][2])
    return answer, success_list

def solution(board):
    count, success_list = check_line(board)
    black, white = 0, 0
    for k in range(3):
        for l in range(3):
            if board[k][l] == 'O':
                white +=1
            elif board[k][l] == 'X':
                black += 1

    print(f'white={white}, black={black}')
    print(f'count, success_list = {count}, {success_list}')
    if white - black not in [0,1]:
        return 0
    if count == 1 and success_list[0] == 'X' and white - black >= 1:
        return 0
    elif count ==1 and success_list[0] == 'O' and white - black == 0:
        return 0

    if count == 2 and success_list[0] != success_list[1]:
        return 0
    elif count > 2:    
        return 0
    
    return 1


#board=    ["OXO", "XOX", "OXO"]
#board=    ["OOX", "XXO", "OOX"]
#board=    ["XXX", ".OO", "O.."]
#board=    ["OX.", ".O.", ".XO"]
#board=    ["...", "...", ".O."]
#board=    ["X.X", "X.O", "O.O"]
#board=    ["XO.", "OXO", "XOX"]
#board=    ["OOO", "XOX", "XXO"]
board=    ["OOO", "XOX", "X.X"]
#board=    ["XXX", "OO.", "OO."]
#board=    [".X.", "...", "..."]
#board=    [".X.", "X..", ".O."]
#board=    ["XOX", "OXO", "XOX"]
#board=    ["XXX", "XOO", "OOO"]
#board=    ["OOX", "OXO", "XOO"]
#board=    ["OOX", "OXO", "XOX"]
#board=    [".OX", "OXO", "XO."]
#board=    ["OOO", "XX.", "X.."]


print(solution(board))
