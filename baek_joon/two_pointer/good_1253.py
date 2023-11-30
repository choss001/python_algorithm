import sys
input = sys.stdin.readline

n = int(input())

left = 1
right = 1

answer = 0
temp_sum = 1


while left != n-1 and n != 1:

    if temp_sum < n:
        right += 1
        temp_sum += right
    elif temp_sum > n:
        left += 1
        right = left
        temp_sum = left+1
    else:
        print(f'before {left}, {right}')
        print(f'before temp_sum = {temp_sum}')
        answer += 1
        left += 1
        temp_sum = left+1
        right = left+1
        print(f'{left}, {right}')
        

if n ==1:
    print(1)
else:
    print(f'{answer+1}')    
