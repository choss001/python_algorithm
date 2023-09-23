import sys
input = sys.stdin.readline

mx = [0, 1, 0, -1]
my = [-1, 0, 1, 0]
answer = 0

def dfs(x, y, visited_alphabet, temp_answer):
    for move in range(4):
        global answer
        dx = x + mx[move]
        dy = y + my[move]
        if input_list[dy][dx] in visited_alphabet:
            continue
        visited_alphabet[input_list[dy][dx]] = 1
        dfs(dx, dy, visited_alphabet)
        del visited_alphabet[input_list[dy][dx]]
            

row_num, column_num = map(int, input().split())
input_list = []



for _ in range(row_num):
    input_list.append(list(input().strip()))


visited_alphabet = {}
visited_alphabet[input_list[0][0]] = 1
dfs(0, 0, visited_alphabet, 0)
print(f'input_list = {input_list}')


