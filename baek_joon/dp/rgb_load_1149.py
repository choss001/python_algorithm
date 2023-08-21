import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
map_list = []

x_list = [[1, 2], [0, 2], [0, 1]]
answer_list = []

for _ in range(int(input())):
    map_list.append(list(map(int, input().split())))
    answer_list.append([-1, -1, -1])


def dp(y, x):
    if y == 0:
        return map_list[y][x]
    a,b = x_list[x]
    if answer_list[y][x] == -1:
        answer_list[y][x] = min(dp(y-1, a) + map_list[y][x], dp(y-1, b) + map_list[y][x])
    return answer_list[y][x]

y_val = len(map_list) -1
for x_val in range(3):
    dp(y_val, x_val)
print(f'{min(answer_list[-1])}')
