import sys
input = sys.stdin.readline
from collections import deque



n, m = map(int, input().split()) #n 줄, m 컬럼
n_lst = [list(input().rstrip()) for _ in range(n)]
m_lst = [[-1] * m for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

mx = [0, 1, 0, -1]
my = [-1, 0, 1, 0]

q = deque()
end = []


for l in range(n):
    for k in range(m):
        if n_lst[l][k] == 'E':
            end = [l, k]
        if n_lst[l][k] == 'S':
            m_lst[l][k] = 5
            q.append((k, l))
            visited[l][k] = 0
        elif n_lst[l][k] == '#':
            m_lst[l][k] = 2
            for w in range(4):
                dk = mx[w] + k
                dl = my[w] + l
                if 0 <= dk < m and 0 <= dl < n and (n_lst[dl][dk] == '.' or n_lst[dl][dk] == 'E'):
                    m_lst[dl][dk] = 0

        elif (n_lst[l][k] == '.' or n_lst[l][k] == 'E') and m_lst[l][k] != 0:
            m_lst[l][k] = 1

#for i in range(m):
#    print(f'{m_lst[i]}')

while q:
    x, y = q.popleft()
    for sw in range(4):
        dx = x + mx[sw]
        dy = y + my[sw]
        if 0 <= dx < m and 0 <= dy and visited[dy][dx] == -1 and (n_lst[dy][dx] == '.' or n_lst[dy][dx] == 'E'):
            if m_lst[dy][dx] == 0:
                if m_lst[y][x] != 0:
                    visited[dy][dx] = visited[y][x] +1
                else:
                    visited[dy][dx] = visited[y][x]
                q.appendleft((dx, dy))
            elif m_lst[dy][dx] == 1:
                visited[dy][dx] = visited[y][x] +1
                q.append((dx, dy))
for i in range(n):
    print(f'{visited[i]}')
print(f'{end}')
print(f'{visited[end[0]][end[1]]}')


