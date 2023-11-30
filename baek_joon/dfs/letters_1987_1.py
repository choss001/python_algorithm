import sys
input = sys.stdin.readline


N, M = map(int, input().split())
N_lst = [list(input().rstrip()) for _ in range(N)]
visited = [False] * 50
mx = [0, 1, 0, -1]
my = [-1, 0, 1, 0]

answer = 0


def dfs(x, y, temp_answer):
    global answer
    #print(f'answer = {answer}')
    for k in range(4):
        dx = mx[k] + x
        dy = my[k] + y
        if 0> dx or M <= dx or 0 > dy or N <= dy:
            continue
        convert_num = ord(N_lst[dy][dx]) - 65
        #print(f'convert_num = {convert_num}, dy = {dy}, dx = {dx}, x={x}, y={y}, temp_answer={temp_answer}')
        if visited[convert_num] == False:
        #    print(f' not visited ')
            visited[convert_num] = True
            temp_answer += 1
            dfs(dx, dy, temp_answer)
            visited[convert_num] = False
            temp_answer -= 1
        else:
            answer = max(answer,  temp_answer)


        
visited[ord(N_lst[0][0]) - 65] = True
dfs(0, 0, 1)
print(f'{answer}')
