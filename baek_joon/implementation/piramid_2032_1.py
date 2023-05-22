import sys

m, n, a, b, c, d = map(int, sys.stdin.readline().split())
terrain_map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

average_height = 0
pyramid_location = (0, 0)
room_location = (0, 0)

sum_temp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        sum_temp[i][j] = sum_temp[i - 1][j] + sum_temp[i][j - 1] - sum_temp[i - 1][j - 1] + terrain_map[i - 1][j - 1]

for i in range(m - a + 1):
    for j in range(n - b + 1):
        temp_sum = sum_temp[j + b][i + a] - sum_temp[j][i + a] - sum_temp[j + b][i] + sum_temp[j][i]
        temp_room_sum = sum_temp[j + d][i + c] - sum_temp[j][i + c] - sum_temp[j + d][i] + sum_temp[j][i]

        temp_average = (temp_sum - temp_room_sum) / (a * b - c * d)

        if temp_average > average_height:
            average_height = temp_average
            pyramid_location = (i, j)
            room_location = (i + c, j + d)

print(f'{pyramid_location[0] + 1} {pyramid_location[1] + 1}')
print(f'{room_location[0] + 1} {room_location[1] + 1}')

