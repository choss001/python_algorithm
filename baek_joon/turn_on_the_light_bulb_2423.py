from collections import deque

#input_map= [
#['\\','\\','/','\\','\\'],
#['\\','\\','/','/','/'],
#['/','\\','\\','\\','\\'],
#]
#n,m = 3, 5
n, m = map(int, input().split())
input_map = [list(input().rstrip())  for _ in range(n)]
map_c = [[0 if j == '/' else 1 for j in i] for i in input_map]
dis_map = [[0 for _ in range(m)] for _ in range(n)]
visited_map = [[False for _ in range(m)] for _ in range(n)]

d = [(-1, 1), (1, -1),(-1, -1), (1, 1), (-1, 0),(0, 1), (1, 0), (0, -1)]
q = deque([])

if map_c[0][0] == 0:
    dis_map[0][0] = 1
q.append((0,0))
visited_map[0][0] = True

while q:
    y,x = q.popleft();

    for i in d:
        dy = y + i[0]
        dx = x + i[1]

        if 0 > dy or dy >=n or  0> dx or dx >= m or visited_map[dy][dx] == True:
            continue
        
        if map_c[y][x] == 0:
            if (i[0] == 1 and i[1] == 1) or (i[0] == -1 and i[1] == -1):
                continue
        elif map_c[y][x] == 1:
            if (i[0] == -1 and i[1] == 1) or (i[0] == 1 and i[1] == -1):
                continue



        if (i[0] == -1 and i[1] == 1) or (i[0] == 1 and i[1] == -1):
            if map_c[y][x] == map_c[dy][dx]:
                q.appendleft((dy,dx))
                dis_map[dy][dx] = dis_map[y][x]
                visited_map[dy][dx] =True
                continue
            else:
                q.append((dy,dx))
                dis_map[dy][dx] = dis_map[y][x]+1
                visited_map[dy][dx] =True
                map_c[dy][dx] = 0
                continue

        if (i[0] == 1 and i[1] == 1) or (i[0] == -1 and i[1] == -1):
            if map_c[y][x] == map_c[dy][dx]:
                q.appendleft((dy,dx))
                dis_map[dy][dx] = dis_map[y][x]
                visited_map[dy][dx] =True
                continue
            else:
                q.append((dy,dx))
                dis_map[dy][dx] = dis_map[y][x]+1
                visited_map[dy][dx] =True
                map_c[dy][dx] = 1
                continue


        if map_c[y][x] != map_c[dy][dx]:
            q.appendleft((dy,dx))
            dis_map[dy][dx] = dis_map[y][x]
            visited_map[dy][dx] =True
        elif map_c[y][x] == map_c[dy][dx]:
            q.append((dy,dx))
            dis_map[dy][dx] = dis_map[y][x]+1
            visited_map[dy][dx] =True
            visited_map[dy][dx] = 0 if visited_map[y][x] == 1 else 1
            
        else:
            print('must no here')

if visited_map[n-1][m-1] == False:
    print('NO SOLUTION')
else:
    print(dis_map[n-1][m-1])
