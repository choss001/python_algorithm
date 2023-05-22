import sys
input = sys.stdin.readline

dp = [(-1, -1) for _ in range(41)]
dp[0] = (1, 0)
dp[1] = (0, 1)

def fibonacci(n):
    if n == 0:
        return dp[0];
    elif n == 1:
        return dp[1];
    else:
        if dp[n-1][0] == -1 and dp[n-2][0] == -1:
            dp[n] = (fibonacci(n-1)[0] + fibonacci(n-2)[0], fibonacci(n-1)[1] + fibonacci(n-2)[1])
            return dp[n]
        elif dp[n-1][0] != -1 and dp[n-2][0] == -1:
            dp[n] = (dp[n-1][0] + fibonacci(n-2)[0], dp[n-1][1] + fibonacci(n-2)[1])
            return dp[n]
        elif dp[n-1][0] == -1 and dp[n-2][0] != -1:
            dp[n] = (fibonacci(n-1)[0] + dp[n-2][0], fibonacci(n-1)[1] + dp[n-2][1])
            return dp[n]
        elif dp[n-1][0] != -1 and dp[n-2][0] != -1:
            dp[n] = (dp[n-1][0] + dp[n-2][0], dp[n-1][1] + dp[n-2][1])
            return dp[n]

N = int(input())

temp_l = []
temp_l_s = []
for _ in range(N):
    temp = int(input())
    temp_l.append(temp)
    temp_l_s.append(temp)
temp_l_s.sort(reverse=True)

fibonacci(temp_l_s[0])

for i in temp_l:
    print(*dp[i])
