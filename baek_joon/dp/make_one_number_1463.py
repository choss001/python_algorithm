import sys
input = sys.stdin.readline

N = int(input())
if N == 1:
    print(0)
elif N == 2:
    print(1)
elif N == 3:
    print(1)
else:
    dp = [-1] * (N+1)
    dp[3] = 1
    dp[2] = 1
    dp[1] = 0

    for i in range(4, N+1):
        if i % 2 == 1 and i%3!=0:
            dp[i] = dp[i-1] + 1
        elif i%3==0 and i%2 != 0:
            dp[i] = dp[i//3] + 1
        elif i%3==0 and i%2 ==0:
            dp[i] = min(dp[i//3], dp[i//2]) + 1
        elif i%2==0 and i%3!=0:
            dp[i] = min(dp[i//2], dp[i-1]) + 1
    for i in range(N):
        print(f'{i}\t{dp[i]}')

    print(f'{dp[N]}')
