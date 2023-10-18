from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
N_lst = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[-1] * N for _ in range(N)]

mx = [0, 1, 0, -1]
my = [-1, 0, 1, 0]

q = deque()
q.append((0,0))
visited[0][0] = 0

while q:
    x, y = q.popleft()
    for k in range(4):
        dx = mx[k] + x
        dy = my[k] + y
        if 0 <= dx < N and 0 <= dy < N and visited[dy][dx] == -1 :
            if N_lst[dy][dx] == 1:
                q.appendleft((dx, dy))
                visited[dy][dx] = visited[y][x]
            else:
                q.append((dx, dy))
                visited[dy][dx] = visited[y][x] + 1
print(f'{visited[N-1][N-1]}')
for i in range(N):
    print(f'{visited[i]}')
