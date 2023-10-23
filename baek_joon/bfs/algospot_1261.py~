import sys
input = sys.stdin.readline
from collections import deque

M, H = map(int, input().split())
n_lst = [list(map(int, input().rstrip())) for _ in range(H)]
visited = [[-1] * M for _ in range(H)]
mx = [0, 1, 0, -1]
my = [-1, 0, 1, 0]


q = deque()
q.append((0, 0))
visited[0][0] = 0
while q:
   x, y = q.popleft() 
   for mv in range(4):
       dx = mx[mv] + x
       dy = my[mv] + y
       if 0 <= dx < M and 0 <= dy < H and visited[dy][dx] == -1:
           if n_lst[dy][dx] == 0:
               q.appendleft((dx, dy))
               visited[dy][dx] = visited[y][x]
           else:
               q.append((dx, dy))
               visited[dy][dx] = visited[y][x] + 1
print(f'{visited[H-1][M-1]}')
