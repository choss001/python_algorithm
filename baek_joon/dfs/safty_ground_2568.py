import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

move_x = [0, 1, 0, -1]
move_y = [-1, 0, 1, 0]

m = int(input())

input_list = [ list(map(int, input().split())) for _ in range(m)]


def dfs(ix, iy, height, visited_check):

    for next_num in range(4):
        dx = ix + move_x[next_num]
        dy = iy + move_y[next_num]

        if dx < 0 or dx >= m or dy < 0 or dy >=m:
            continue
        if input_list[dy][dx] < height:
            continue
        if visited_check[dy][dx] == 1:
            continue
        visited_check[dy][dx] = 1
        dfs(dx, dy, height, visited_check)

def graph_exam(height):
    temp_answer = 0
    visited_check = [[0] * m for _ in range(m)]
    for ix in range(m):
        for iy in range(m):
            if input_list[iy][ix] >= height and \
                    visited_check[iy][ix] == 0:
                    temp_answer += 1
                    visited_check[iy][ix] = 1
                    dfs(ix, iy, height, visited_check)
    return temp_answer

answer = 0

max_value = 0
for max_value_candidate in input_list:
    max_value = max(max(max_value_candidate), max_value)
for value in range(max_value+1):
    answer = max(graph_exam(value), answer)
    
print(f'{1 if answer == 0 else answer}')




