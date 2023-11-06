import sys
input = sys.stdin.readline

n = int(input())
input_lst = list(map(int, input().split()))
m = int(input())

right = len(input_lst)-1
left = 0

answer_count = 0
input_lst.sort()
while right > left:
    if input_lst[left]+input_lst[right] == m:
        #print(f'({input_lst[left]}, {input_lst[right]})')
        answer_count += 1
        right -= 1
        left += 1
    elif input_lst[left]+input_lst[right] > m:
        right -= 1
    else:
        left += 1

print(f'{answer_count}') 
