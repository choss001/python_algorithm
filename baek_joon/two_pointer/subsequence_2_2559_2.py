import sys
input = sys.stdin.readline

n, m = map(int, input().split())
input_lst = list(map(int, input().split())) 

max_sum = -sys.maxsize

temp_sum = sum(input_lst[:m])
max_sum = max(max_sum, sum(input_lst[:m]))

for k in range(m, n):
    temp_sum = temp_sum - input_lst[k-m] + input_lst[k]
    max_sum = max(max_sum, temp_sum)

print(f'{max_sum}')
