import sys
input = sys.stdin.readline

H, W, C = map(int, input().split())
input_lst = [[0] * W for _ in range(H)]
square_lst = []

for _ in range(C):
    temp = list(map(int, input().split()))
    square_lst.append(temp)
print(f'{square_lst}')

for item in square_lst:
    for y in range(item[1], item[3]):
        for x in range(item[0], item[2]):
            
            input_lst[y][x] = 1
    

for i in range(H):
    print(f'{input_lst[i]}')
