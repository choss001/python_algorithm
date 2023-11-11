import sys
input = sys.stdin.readline

N, M = map(int,input().split())
N_lst = [list(map(int, input().split())) for _ in range(N)]

mx = [0, 1, 0, -1]
my = [-1, 0, 1, 0]
answer = 0
def dfs(x, y):
    if x == M-1 and y == N-1:
        global answer
        answer += 1
    for i in range(4):
        dx = mx[i]+x
        dy = my[i]+y
        if 0<=dx<M and 0<=dy<N and N_lst[y][x] > N_lst[dy][dx]:
            dfs(dx, dy)
dfs(0,0)
print(f'{answer}')




