import sys
input = sys.stdin.readline

N = int(input())
N_lst = [int(input()) for _ in range(N)]

def dp(k):
    if k < 3 :
        return dp_lst[k]
    if dp_lst[k] == -1:
        temp_answer = max(dp(k-3) + N_lst[k-1], dp(k-2)) + N_lst[k]
        dp_lst[k] = temp_answer
    return dp_lst[k]

if N == 1:
    print(N_lst[0])
elif N == 2:
    print(N_lst[0] + N_lst[1])
elif N == 3:
    print(max(N_lst[0], N_lst[1]) + N_lst[2])
else:

    dp_lst = [-1] * N
    dp_lst[0] = N_lst[0]
    dp_lst[1] = N_lst[0] + N_lst[1]
    dp_lst[2] = max(N_lst[0], N_lst[1]) + N_lst[2]

    dp(N-1)
    print(f'{dp_lst[-1]}')

