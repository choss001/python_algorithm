import sys
input = sys.stdin.readline

dp = [(1, 0), (0, 1)] + [(-1, -1) for _ in range(39)]

def fibonacci(n):
    if dp[n][0] == -1 and dp[n][1] == -1:
        dp[n] = (fibonacci(n-1)[0] + fibonacci(n-2)[0], fibonacci(n-1)[1] + fibonacci(n-2)[1])
    return dp[n]

N = int(input())
temp_l = [int(input()) for _ in range(N)]
temp_l_s = sorted(temp_l, reverse=True)

fibonacci(temp_l_s[0])

for i in temp_l:
    print(*dp[i])

