import sys
input = sys.stdin.readline

n, m = map(int, input().split())
input_lst = list(map(int, input().split()))
min_length = sys.maxsize

right, left = 0, 0
sum = 0
while True:
    
    if sum >= m:
        min_length = min(min_length, right-left)
        sum -= input_lst[left]
        left += 1
    elif right == n:
        break
    else:
        sum += input_lst[right]
        right += 1

if min_length == sys.maxsize:
    print(0)
else:
    print(f'{min_length}')
    



