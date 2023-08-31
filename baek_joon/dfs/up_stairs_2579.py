import sys
input = sys.stdin.readline

input_list = []

for _ in range(int(input())):
    input_list.append(int(input()))

dp = [-1] * len(input_list)
if len(input_list) <= 2:
    print(sum(input_list))
else:
    dp[0] = input_list[0]
    dp[1] = input_list[0] + input_list[1]
    dp[2] = max(input_list[0] + input_list[2], input_list[1]+ input_list[2])
    for i in range(3,len(input_list)):
        dp[i] = max(dp[i-2]+input_list[i], dp[i-3]+input_list[i-1]+input_list[i])
    print(dp[-1])
