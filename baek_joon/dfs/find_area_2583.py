import sys
input = sys.stdin.readline

H, W, C = map(int, input().split())
input_lst = [[0] * W for _ in range(H)]
visited = [[False] * (W) for _ in range(H)]
square_lst = []
answer_square_count = []
number_of_square = 0

mx = [0, 1, 0, -1]
my = [-1, 0, 1, 0]

for _ in range(C):
    temp = list(map(int, input().split()))
    square_lst.append(temp)

for item in square_lst:
    for y in range(item[1], item[3]):
        for x in range(item[0], item[2]):
            input_lst[y][x] = 1
    

def dfs(x, y):
    global temp_answer_square_count
    for i in range(4):
        dx = mx[i] + x
        dy = my[i] + y
        if 0<=dx<W and 0<=dy<H and visited[dy][dx] == False and input_lst[dy][dx] == 0:
            visited[dy][dx] = True
            dfs(dx,dy)
            temp_answer_square_count += 1

temp_answer_square_count = 0

for y in range(H):
    for x in range(W):
        if input_lst[y][x] == 0 and visited[y][x] == False:
            temp_answer_square_count = 1
            visited[y][x] = True
            dfs(x,y)
            answer_square_count.append(temp_answer_square_count)
            number_of_square += 1
print(f'{number_of_square}')        

answer_square_count.sort()
for i in answer_square_count:
    print(f'{i}', end = ' ')

