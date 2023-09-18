import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

move_x = [0, 1, 1, 1, 0, -1, -1, -1]
move_y = [-1, -1, 0, 1, 1, 1, 0, -1]

def dfs(sx, sy, visited_check, mx, my, input_list):
    for move_coordinate in range(8):
        dx = sx + move_x[move_coordinate]
        dy = sy + move_y[move_coordinate]

        if dx <0 or dy < 0 or dx >= mx or dy >= my:
            continue
        if visited_check[dy][dx] == 1:
            continue
        if input_list[dy][dx] == 0:
            continue
        visited_check[dy][dx] = 1
        dfs(dx, dy, visited_check, mx, my, input_list)



while True:
    ix, iy = map(int, input().split())
    if ix == 0 and iy == 0:
        break

    input_list = []
    for dy in range(iy):
        ix_list = list(map(int, input().split()))
        input_list.append(ix_list)

    visited_check = [[0] * ix for _ in range(iy)]
    answer = 0
    for sy in range(iy):
        for sx in range(ix):
            if visited_check[sy][sx] == 0 and input_list[sy][sx] == 1:
                answer += 1
                dfs(sx, sy, visited_check, ix, iy, input_list)
    print(f'{answer}')
    


