import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)



c_y = [-1, 0, 1, 0]
c_x = [0, 1, 0, -1]

def bfs(y, x):
    visited[y][x] = 1
    for k in range(4):
        dy = y + c_y[k]
        dx = x + c_x[k]
        if N > dy and dy >= 0 and \
        M > dx and dx >=0 and \
        map_list[dy][dx] == 1 and \
        visited[dy][dx] == 0:
            bfs(dy, dx)

for _ in range(int(input()[:-1])):
    answer = 0
    M, N, K = map(int, input().split())
    map_list = [[0] * M for _ in range (N)]
    visited = [[0] * M for _ in range (N)]
    for _ in range(K):
        x, y = map(int, input().split())
        map_list[y][x] = 1

    for x in range(M):
        for y in range(N):
            if map_list[y][x] == 1 and visited[y][x] == 0:
                answer += 1
                bfs(y, x)
    print(f'{answer}')



