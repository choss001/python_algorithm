# down, left, up, right
dy=(1,0,-1,0)
dx=(0,-1,0,1)

def solution(grid):
    answer=[]

    ly,lx=len(grid),len(grid[0])

    # 4방향 방문 기록 리스트 : y*x*4
    visited=[[[False]*4 for _ in range(lx)] for _ in range(ly)]

    # 모든 좌표에 대하여 탐색
    for y in range(ly):
        for x in range(lx):

            # (y, x) 좌표에 대해 4방향 탐색
            for d in range(4):
                # 해당 좌표-방향 이 기존에 사용된 경우
                if visited[y][x][d]:
                    continue

                # 사용되지 않은 좌표-방향인 경우
                count = 0
                ny, nx = y, x
                # 빛을 이동 시켜가며 탐색
                while not visited[ny][nx][d]:
                    for i in range(ly):
                        for k in range(lx):
                            print(f'visited={visited[i][k]}')
                    print(f'ny={ny}, nx={nx}, d={d},grid[ny][nx]={grid[ny][nx]}')
                    visited[ny][nx][d] = True
                    count += 1
                    if grid[ny][nx] == "S": # S의 경우 방향 변경 X
                        pass
                    elif grid[ny][nx] == "L": # L의 경우 반시계방향
                        d = (d - 1) % 4
                    elif grid[ny][nx] == "R": # R의 경우 시계방향
                        d = (d + 1) % 4
                    print(f'd = {d}')

                    # 좌표의 길이로 %연산을 하여 격자를 벗어난 경우에도 자리를 찾아가도록함.
                    ny = (ny + dy[d]) % ly
                    nx = (nx + dx[d]) % lx

                answer.append(count)
    answer = sorted(answer) # 오름차순 정렬
    return answer


grid = ["SL","LR"]
#grid = ["S"]
#grid = ["R","R"]

print(f'solution = {solution(grid)}')


#[
#        [[False, False, False, False],[False, False, False, False]], 
#        [[False, False, False, False],[False, False, False, False]]
#]  
#dy=(1,0,-1,0)
#dx=(0,-1,0,1)
ly, lx = 2, 2
d = 0
y, x = 0, 0
ny, nx  = 0 , 0
#############################
visited[0][0][0] = False
count = 1
d = 0
ny = ny+dy[0] % ly = (0+1) % 2 = 1
nx = (nx+dx[0]) % lx = (0+0)%2= 0 
#############################
visited[1][0][0] = False
count = 2
grid[ny][nx][0] = L
d = (d -1) % 4 = 3
ny = (ny + dy[3]) % ly = (1+0)%2 = 1
nx = (nx + dy[3]) % ly = (0+1)%2 = 1
#############################










def turn(to, d):
    if to == "S":
        return d
    elif to == "L":
        return (d + 3) % 4
    else:
        return (d + 1) % 4

def solution(grid):
    answer = []
    
    R = len(grid)
    C = len(grid[0])
    map = [[c for c in row] for row in grid]
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    visited = [[[False for _ in range(4)] for _ in range(C)] for _ in range(R)]
    
    for i in range(R):
        for j in range(C):
            for k in range(4):
                if visited[i][j][k]:
                    continue
                
                start = {"y": i, "x": j, "dir": k}
                cur = start.copy()
                count = 0
                
                while True:
                    if visited[cur["y"]][cur["x"]][cur["dir"]]:
                        break
                    
                    count += 1
                    visited[cur["y"]][cur["x"]][cur["dir"]] = True
                    
                    nd = turn(map[cur["y"]][cur["x"]], cur["dir"])
                    ny = (cur["y"] + dy[nd] + R) % R
                    nx = (cur["x"] + dx[nd] + C) % C
                    
                    cur["y"] = ny
                    cur["x"] = nx
                    cur["dir"] = nd
                    
                    if cur == start and count > 0:
                        answer.append(count)
                        break
                
    return sorted(answer)
