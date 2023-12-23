import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

n_lst = list(map(int, input().split()))

n_lst.sort()

left, right = 0, n -1

answer = 0
while left < right:
    temp_sum = n_lst[left] + n_lst[right]

    if temp_sum == m:
        answer += 1
        right -= 1
        left += 1
    elif temp_sum > m:
        right -=1
    elif temp_sum < m:
        left += 1
print(f'{answer}')
