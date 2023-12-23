import sys
input = sys.stdin.readline

N = int(input())
N_lst = [list(map(int, input().split())) for _ in range(N)]
dp_lst = [[-1] * 3 for _ in range(N)]

def dp(y, x):
    if y == 0:
        return N_lst[y][x]

    if dp_lst[y][x] == -1:
        temp_answer = -1
        if x==0:
            temp_answer = min(dp(y-1, 1)+N_lst[y][x], dp(y-1,2)+N_lst[y][x])
        elif x ==1:
            temp_answer = min(dp(y-1, 0)+N_lst[y][x], dp(y-1,2)+N_lst[y][x])
        elif x ==2:
            temp_answer = min(dp(y-1, 0)+N_lst[y][x], dp(y-1,1)+N_lst[y][x])
        dp_lst[y][x] = temp_answer
    return dp_lst[y][x]

for i in range(3):
    dp(N-1, i)
print(f'{min(dp_lst[N-1])}')
