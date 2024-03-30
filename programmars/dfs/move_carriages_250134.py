def solution(maze):
    move = [(-1,0),(0,1),(1,0),(0,-1)]
    start_r = [0,0]
    start_b = [0,0]
    v_r = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    v_b = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    print(f'v_r={v_r}, v_b={v_b}')

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                start_r[0],start_r[1] = i,j
            if maze[i][j] == 2:
                start_b[0],start_b[1] = i,j
    print(f'start_b={start_b}, start_r={start_r}')

    def dfs(start_r, start_b):
        v_r[start_r[0]][start_r[1]] = True
        v_b[start_b[0]][start_b[1]] = True

        print(f'svr, {start_r}' )
        for v in v_r:
            print(v)
        print(f'svb, {start_b}')
        for v in v_b:
            print(v)


        for i in range(4):
            d_r = [start_r[0] + move[i][0], start_r[1] + move[i][1]]
            if not (0 <= d_r[0] < len(maze)): continue
            if not (0 <= d_r[1] < len(maze[0])): continue
            if v_r[d_r[0]][d_r[1]]: continue
            if maze[d_r[0]][d_r[1]] == 5: continue
            if d_r[0] == start_b[0] and d_r[1] == start_b[1]: continue
            for j in range(4):
                d_b = [start_b[0] + move[j][0], start_b[1] + move[j][1]]
                if not (0 <= d_b[0] < len(maze)): continue
                if not (0 <= d_b[1] < len(maze[0])): continue
                if v_b[d_b[0]][d_b[1]]: continue
                dfs(d_r, d_b)
                v_r[d_r[0]][d_r[1]] = False
                v_b[d_b[0]][d_b[1]] = False

    dfs(start_r, start_b)
    



    return

maze = [[1, 4], [0, 0], [2, 3]]
print(solution(maze))

