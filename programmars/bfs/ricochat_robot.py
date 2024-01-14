from collections import deque
mx = [0,1,0,-1]
my = [-1,0,1,0]

def solution(board):
    visited = [[-1] *len(board[0]) for _ in range(len(board))]
    q = deque()
    answer_coor=[]

    for k in range(len(board)):
        for l in range(len(board[0])):
            if board[k][l] == 'R':
                visited[k][l] = 0
                q.append((k,l,0))
            elif board[k][l] == 'G':
                answer_coor.append((k,l))


    answer = 1e9
    while len(q)>0:
        y,x,c = q.popleft()

        for i in range(4):
            dy = y
            dx = x
            while True:
                dx += mx[i]
                dy += my[i]
                if dx <0 or dx >= len(board[0]) or\
                        dy < 0 or dy >= len(board):
                    if visited[dy-my[i]][dx-mx[i]] != -1:
                        break
                    visited[dy-my[i]][dx-mx[i]] = c +1
                    q.append((dy-my[i],dx-mx[i],c+1))
                    break
                elif board[dy][dx] == 'D':
                    dx-=mx[i]
                    dy-=my[i]
                    if visited[dy][dx] != -1:
                        break
                    if board[dy][dx] == 'G':
                        answer = min(answer, c+1)
                    q.append((dy,dx,c+1))
                    visited[dy][dx] = c+1
                    break
#   for i in range(len(board)):
#       print(visited[i])
    y, x = answer_coor.pop()
    return visited[y][x]

#board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
#board = [".D.R", "....", ".G..", "...D"]
board = ["..R",
"...",
"...",
"..D",
"DG."]
print(f'answer = {solution(board)}')


