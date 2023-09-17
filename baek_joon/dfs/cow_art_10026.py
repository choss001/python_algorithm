import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

height = int(input())
input_two = []
c_boolean_dic = {}
h_boolean_dic = {}
cow_sight = ['G', 'R']
c_answer = 0
h_answer = 0

fx = [0, 1, 0, -1]
fy = [-1, 0, 1, 0]

for _ in range(height):
    one_line = input()
    one_array = [k for k in one_line[:-1]]
    input_two.append(one_array)

def cdfs(now_co_y, now_co_x):
    for after in range(4):
        dy = now_co_y + fy[after]
        dx = now_co_x + fx[after]
        if dy < 0 or dy >= height or \
                dx < 0 or dx >= height:
            continue
        if(input_two[now_co_y][now_co_x] == input_two[dy][dx]) or \
                (input_two[now_co_y][now_co_x] in cow_sight and input_two[dy][dx] in cow_sight):
            if (dy, dx) not in c_boolean_dic:
                c_boolean_dic[(dy,dx)] = 1
                cdfs(dy, dx)

def hdfs(now_co_y, now_co_x):
    for after in range(4):
        dy = now_co_y + fy[after]
        dx = now_co_x + fx[after]
        if dy < 0 or dy >= height or \
                dx < 0 or dx >= height:
            continue
        if(input_two[now_co_y][now_co_x] == input_two[dy][dx]):
            if (dy, dx) not in h_boolean_dic:
                h_boolean_dic[(dy,dx)] = 1
                hdfs(dy, dx)

for cx in range(height):
    for cy in range(height):
        if (cy,cx) not in c_boolean_dic:
            cdfs(cy, cx)
            c_answer += 1
        if (cy,cx) not in h_boolean_dic:
            hdfs(cy, cx)
            h_answer += 1



print(f'{h_answer} {c_answer}')

