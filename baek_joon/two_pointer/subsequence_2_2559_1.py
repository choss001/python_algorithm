import sys
input = sys.stdin.readline

n, m = map(int, input().split())
input_lst = list(map(int, input().split())) 

sum_max = -sys.maxsize

i = 0
while True:
    if m + i >= n:
        break
    sum_max = max(sum_max, sum(input_lst[i:m+i]))
    i += 1
    
print(f'{sum_max}')
            
