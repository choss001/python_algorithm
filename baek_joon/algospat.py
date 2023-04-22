if __name__ == '__main__':
    from collections import deque
#   x, y = 6, 6
#   block_room = [
#   [0,0,1,1,1,1],
#   [0,1,0,0,0,0],
#   [0,0,1,1,1,1],
#   [1,1,0,0,0,1],
#   [0,1,1,0,1,0],
#   [1,0,0,0,1,0],
#   ]
    visited = [[False for _ in range(x)] for _ in range(y)]
    visited[0][0] = True
    count_room = [[0 for _ in range(x)] for _ in range(y)]
    Q = deque()
    Q.append((0,0))
    mx = [0, -1, 0, 1]
    my = [-1, 0, 1, 0]
    while Q:
        bx, by = Q.popleft()
        break_block_num = count_room[by][bx]
        if bx == x -1 and by == y -1:
            print(count_room[y-1][x -1])
        for i in range(4):
            ax, ay = bx + mx[i], by + my[i]
            if ax >= 0 and ay >= 0 and ax < len(block_room[0]) and ay < len(block_room) and visited[ay][ax] != True:
                if block_room[ay][ax] == 1:
                    count_room[ay][ax] = break_block_num + 1
                    Q.append((ax, ay))
                else:
                    count_room[ay][ax] = break_block_num
                    Q.appendleft((ax,ay))
                visited[ay][ax] = True
                




