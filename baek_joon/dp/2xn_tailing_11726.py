import sys
input = sys.stdin.readline

answer_list = [-1] * 1001

def dp(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    if answer_list[num] == -1:
        answer_list[num] = dp(num-2) + dp(num-1)
    return answer_list[num]


num = int(input())
print(dp(num)% 10007)
