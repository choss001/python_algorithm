def solution(rows, columns, queries):
    answer = []

    board = [[i+(j)*columns for i in range(1,columns+1)] for j in range(rows)]
    # print(board)

    for a,b,c,d in queries:
        stack = []
        r1, c1, r2, c2 = a-1, b-1, c-1, d-1
        print(f'r1, c1, r2, c2 = {r1}, {c1}, {r2}, {c2}')


        for i in range(c1, c2+1):

            stack.append(board[r1][i])
            print(f'stack = {stack}, board[r1][i]={board[r1][i]}, i={i}')
            if len(stack) == 1:
                continue
            else:
                print(f'stack[-2] = {stack[-2]}')
                board[r1][i] = stack[-2]
        for q in range(len(board)):
            print(board[q])

        for j in range(r1+1, r2+1):
            stack.append(board[j][i])
            board[j][i] = stack[-2]
        print(f'stack = {stack}, wow')
        for q in range(len(board)):
            print(board[q])
        for k in range(c2-1, c1-1, -1):
            stack.append(board[j][k])
            board[j][k] = stack[-2]

        print(f'stack = {stack}')
        for l in range(r2-1, r1-1, -1):
            stack.append(board[l][k])
            board[l][k] = stack[-2]

        print(f'stack = {stack}')
        answer.append(min(stack))


    return answer

rows,columns,queries=6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]
#rows,columns,queries=3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
#rows,columns,queries=2,2,[[1,1,2,2]]
print(solution(rows, columns, queries))



