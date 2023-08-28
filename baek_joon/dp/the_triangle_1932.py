import sys
input = sys.stdin.readline

n = int(input())
input_list = [[0]+list(map(int, input().split()))+[0]*(n-i) for i in range(n)]
dp_list = [[-1 for _ in range(n + 1)] for _ in range(n)]



def dp(depth, row):
    if dp_list[depth][row] != -1:
        return dp_list[depth][row]
    if row == 0:
        dp_list[depth][row] = 0
        return 0
    if depth == 0:
        dp_list[depth][row] = input_list[depth][row]
        return input_list[depth][row]

    dp_list[depth][row] = input_list[depth][row] +max(dp(depth-1,row-1),dp(depth-1,row))        
    return dp_list[depth][row]

for i in range(n+1):
    dp(n-1, i)

print(f'{max(dp_list[-1])}')
