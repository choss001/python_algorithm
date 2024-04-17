move = [(0,1),(1,0),(0,-1),(-1,0)]
def solution(grid):


    visited = [[[False]*4 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    answer = []

    for ly in range(len(grid)):
        for lx in range(len(grid[0])):
            for d in range(4):
                print()
                print(f'another start : ly, lx, d = {ly}, {lx}, {d} ')
                y,x = ly,lx
                count = 0
                while not visited[y][x][d]:
                    print(f'y,x,d = {y,x,d}, grid=[{y}][{x}] = {grid[y][x]}')
                    visited[y][x][d] = True
                    for i in range(len(visited)):
                        print(visited[i])
                    count += 1
                    
                    if grid[y][x] == 'S': pass
                    elif grid[y][x] == 'L': d = (d-1) % 4
                    elif grid[y][x] == 'R': d = (d+1) % 4
                    y = (y+move[d][0]) % len(grid)
                    x = (x+move[d][1]) % len(grid[0])
                    print(f'after y, x, d = {y}, {x}, {d}')
                if count != 0: answer.append(count)
    answer.sort()
    return answer


#grid = ["SL","LR"]
#grid = ["S"]
#grid = ["R","R"]
#grid = ["R","R","R"]
#grid = ["L","L"]
#grid = ["SS","SS"]
grid = ["S","S"]

print(solution(grid))
