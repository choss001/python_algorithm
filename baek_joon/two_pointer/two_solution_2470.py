import sys
input = sys.stdin.readline


n = int(input())
input_lst = list(map(int, input().split()))

input_lst.sort()


left = 0
right = len(input_lst) - 1

print(f'sort lst = {input_lst}')
while True:
    temp_sum = input_lst[left] + input_lst[right]
    if temp_sum < 0 :
        left += 1
    elif temp_sum == 0 :
        break
    else :
        right -= 1
    if left >= right:
        break

print(f'{input_lst[left]} {input_lst[right]}')
