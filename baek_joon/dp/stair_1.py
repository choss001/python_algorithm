import sys
input = sys.stdin.readline

number = int(input())
stair_list = [int(input()) for _ in range(number)]
dp = [0] * number

dp[0] = stair_list[0]
dp[1] = stair_list[1] + dp[0]
for i in range(2,number):
    print(f'dp = {dp}')
    print(f'dp[{i-3}]+stair_list[{i-1}]+stair_list[{i}] = {dp[i-3]+stair_list[i-1]+stair_list[i]}')
    print(f'dp[{i-2}]+stair_list[{i}] = {dp[i-2]+stair_list[i]}')
    dp[i] = max(dp[i-3]+stair_list[i-1]+stair_list[i], dp[i-2]+stair_list[i])
print(dp[-1])
