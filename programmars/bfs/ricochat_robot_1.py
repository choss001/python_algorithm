def solution(board):
    que = []
    for x, row in enumerate(board):
        for y, each in enumerate(row):
            if board[x][y] == 'R':
                que.append((x, y, 0))
    visited = set()
    while que:
        x, y, length = que.pop(0)
        if (x, y) in visited:
            continue
        if board[x][y] == 'G':
            return length
        visited.add((x, y))
        for diff_x, diff_y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            now_x, now_y = x, y
            while True:
                next_x, next_y = now_x + diff_x, now_y + diff_y
                print(f'next_x={next_x},next_y={next_y},diff_x={diff_x},\
diff_y={diff_y}')
                if 0 <= next_x < len(board) and \
                        0 <= next_y < len(board[0]) and \
                        board[next_x][next_y] != 'D':
                    print(f'next_x={next_x},next_y={next_y} it meet conditon!!!')
                    now_x, now_y = next_x, next_y
                    continue
                que.append((now_x, now_y, length + 1))
                print(f'que={que}')
                break
    return -1

board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
print(f'solution = {solution(board)}')
