import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

mx = [0, 1, 0, -1]
my = [-1, 0, 1, 0]

def dfs(y, x):
    visited[y][x] = 1
    for m in range(4):
        dy = my[m] + y
        dx = mx[m] + x
        if N > dy and dy >= 0 and \
            M > dx and dx >= 0 and \
            visited[dy][dx] == 0 and \
            map_cabbage[dy][dx] == 1:
            dfs(dy, dx)

for _ in range(int(input())):
    M, N, K = map(int,input().split())
    
    map_cabbage = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    answer = 0

    for _ in range(K):
        x, y = map(int, input().split())
        map_cabbage[y][x] = 1

    
    for x in range(M):
        for y in range(N):
            if visited[y][x] == 0 and map_cabbage[y][x] == 1:
                answer += 1
                dfs(y ,x)
    print(f'{answer}')

