
def solution(maze):
    dic = {}
    f = open("test.txt", "w")
    answer = 99999999
    move = [(-1,0),(0,1),(1,0),(0,-1)]
    start_r = [0,0]
    start_b = [0,0]
    v_r = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
    v_b = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                start_r[0],start_r[1] = i,j
            if maze[i][j] == 2:
                start_b[0],start_b[1] = i,j

    def dfs(start_r, start_b, count):
        nonlocal answer
        nonlocal dic
        v_r[start_r[0]][start_r[1]] = True
        v_b[start_b[0]][start_b[1]] = True
        
        if maze[start_r[0]][start_r[1]] == 3 and \
                maze[start_b[0]][start_b[1]] == 4:
                    answer = min(answer, count)
                    f.write(f' answer = {answer}, count = {count}, start_r={start_r}, start_b={start_b}')
                    return

        f.write(f'\n')
        f.write(f'svr, {start_r}, count={count}\n')
        #print(f'svr, {start_r}' )
        for v in v_r:
            #print(v)
            f.write(f'{str(v)}\n')
        f.write(f'svb, {start_b}\n')
        #print(f'svb, {start_b}')
        for v in v_b:
            #print(v)
            f.write(f'{str(v)}\n')

        for i in range(4):
            d_r = [start_r[0] + move[i][0], start_r[1] + move[i][1]]

            if maze[start_r[0]][start_r[1]] == 3: d_r = start_r[0], start_r[1]
            if not (0 <= d_r[0] < len(maze)): continue
            if not (0 <= d_r[1] < len(maze[0])): continue
            if v_r[d_r[0]][d_r[1]] and maze[d_r[0]][d_r[1]] != 3 : continue
            if maze[d_r[0]][d_r[1]] == 5: continue
            for j in range(4):
                d_b = [start_b[0] + move[j][0], start_b[1] + move[j][1]]
                if maze[start_b[0]][start_b[1]] == 4: d_b = start_b[0], start_b[1]
                if not (0 <= d_b[0] < len(maze)): continue
                if not (0 <= d_b[1] < len(maze[0])): continue
                if v_b[d_b[0]][d_b[1]] and maze[d_b[0]][d_b[1]] != 4: continue
                if maze[d_b[0]][d_b[1]] == 5: continue
                if d_r[0] == start_b[0] and d_r[1] == start_b[1] and d_b[0] == start_r[0] and d_b[1] == start_r[1]: continue
                if d_r[0] == d_b[0] and d_r[1] == d_b[1]: continue
                if  not in dic:
                    dic[(),d_b,count] = True
                print(f'dic={dic}')                    
                print(f'entrace before = d_r = {d_r}, d_b = {d_b}')
                dfs(d_r, d_b, count + 1)
                v_r[d_r[0]][d_r[1]] = False
                v_b[d_b[0]][d_b[1]] = False

    dfs(start_r, start_b, 0)
    f.write(f'answer = {answer}')
    f.close()
    return answer if answer != 99999999 else 0

#maze = [[1, 4], [0, 0], [2, 3]]
maze = [[1, 0, 2], [0, 0, 0], [5, 0, 5], [4, 0, 3]]
print(solution(maze))


#######################################################################################################################

#[1,0,2] [0,1,0] [0,0,1] [0,2,0] [2,0,0] [0,0,0]
#[0,0,0] [0,0,2] [0,2,0] [0,0,1] [0,1,0] [2,0,0]
#[5,0,5] [5,0,5] [5,0,5] [5,0,5] [5,0,5] [5,1,5]
#[4,0,3] [4,0,3] [4,0,3] [4,0,3] [4,0,3] [4,0,3]

#[0,0,0] [0,0,0] [0,0,0] [0,0,0] [0,0,0] [0,0,0] [0,0,0] [0,0,0]
#[0,0,1] [0,1,0] [0,0,0] [0,0,0] [0,0,0] [0,0,0] [0,0,0] [0,0,0]
#[5,2,5] [5,0,5] [5,1,5] [5,1,5] [5,0,5] [5,0,5] [5,0,5] [5,0,5]
#[4,0,3] [4,2,3] [4,0,2] [2,0,3] [4,0,3] [4,0,3] [4,0,3] [4,0,3]

#[1,0,2] [0,2,0] [2,0,0] [0,0,0] [0,0,0] [0,0,0] [0,0,0] [0,0,0]
#[0,0,0] [1,0,0] [0,1,0] [2,0,0] [0,2,0] [0,0,0] [0,0,0] [0,0,0]
#[5,0,5] [5,0,5] [5,0,5] [5,1,5] [5,0,5] [5,2,5] [5,0,5] [5,0,5]
#[4,0,3] [4,0,3] [4,0,3] [4,0,3] [4,1,3] [4,0,1] [4,2,1] [2,0,1]
