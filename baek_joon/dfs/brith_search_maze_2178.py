import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
ax = [0, 1, 0, -1] 
ay = [-1, 0, 1, 0]

maze_map = [[int(e) for e in input()[:-1]] for _ in range(M)]
visited = [[False]* N for _ in range(M) ]

l = deque([[0, 0, 1]])
visited[0][0] = True

while l:
    end_flag =False
    y, x, v= l.popleft()
    for i in range(4):
        dx = ax[i] + x
        dy = ay[i] + y
        if  M-1 >= dy and dy >= 0 and N-1 >= dx and dx >= 0 \
        and visited[dy][dx] == False and maze_map[dy][dx] == 1:
            visited[dy][dx] = True
            l.append([dy, dx, v+1])
        if dy == M-1 and dx == N-1 :
            print(f'{v + 1}')
            end_flag = True
            break
    if end_flag:
        break

