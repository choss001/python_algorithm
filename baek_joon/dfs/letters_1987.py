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
        if dx < 0 or dx >= column_num or dy < 0 or dy >= row_num:
            continue
        if input_list[dy][dx] in visited_alphabet:
            continue
        temp_answer += 1
        answer = max(answer, temp_answer)
        visited_alphabet[input_list[dy][dx]] = 1
        dfs(dx, dy, visited_alphabet, temp_answer)
        temp_answer -= 1
        del visited_alphabet[input_list[dy][dx]]
            

row_num, column_num = map(int, input().split())
input_list = []



for _ in range(row_num):
    input_list.append(list(input().strip()))


visited_alphabet = {}
visited_alphabet[input_list[0][0]] = 1
dfs(0, 0, visited_alphabet, 1)
print(f'{answer}')


