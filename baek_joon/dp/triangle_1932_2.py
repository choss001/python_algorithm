import sys
input = sys.stdin.readline

N = int(input())
N_lst = []
dp_lst = [[None] * N for _ in range(N)]

for i in range(N):
    temp = list(map(int, input().split())) + [-1] *(N-i)
    N_lst.append(temp)
def dp(y, x):
    if y == 0:
        return N_lst[y][x]
    if dp_lst[y][x] == None:
        if x-1 <0 :
            dp_lst[y][x] = N_lst[y][x] + dp(y-1, x)
        else:
            dp_lst[y][x] = max(dp(y-1,x), dp(y-1,x-1)) + N_lst[y][x]
    return dp_lst[y][x]
    
for k in range(N):
    dp(N-1, k)
if N == 1:
    print(f'{N_lst[0][0]}')
else:
    print(f'{max(dp_lst[N-1])}')
