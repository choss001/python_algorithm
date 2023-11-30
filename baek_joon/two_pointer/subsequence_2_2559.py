import sys
input = sys.stdin.readline


n, m = map(int, input().split())
input_lst = list(map(int, input().split()))

max_value = 0

left, right = 0, 0
sum_value = -sys.maxsize
while right < n:
    if right - left == m:
        sum_value = max(sum_value, sum(input_lst[left:right]))
        right += 1
        left += 1
    else:
        right +=1
print(sum_value)
