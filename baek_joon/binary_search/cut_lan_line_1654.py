import sys
input = sys.stdin.readline

n, m = map(int, input().split())

input_lst = [int(input()) for _ in range(n)]


start = 0
end = min(input_lst)


def binary_search(start, end):
    while start <= end :
        temp_answer = 0
        mid = (start + end) // 2
        print(f'start = {start}, end = {end}, mid = {mid}')
        for item in input_lst:
            temp_answer += item//mid
            print(f'item = {item}, temp_answer = {item//mid}')
        
        if temp_answer >= m :
            print(f'temp_answer >= m,  temp_answer = {temp_answer} , m = {m}')
            start = mid +1
        else :
            print(f'temp_answer < m,  temp_answer = {temp_answer} , m = {m}')
            end = mid -1
    
    #print(f'start = {start}, end = {end}')
    print(f'{end}')
binary_search(0, end)

