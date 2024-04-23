
def solution(dirs):
    answer = 0
    b_x, b_y = 0, 0
    a_x, a_y = 0, 0
    graph = [[[] for _ in range(10)] for _ in range(10)]
    for item in dirs:

        if item == 'U':
            if b_y+1 > 5: continue
            a_y = b_y+1
        elif item == 'L':
            if b_x-1 < -5: continue
            a_x = b_x-1
        elif item == 'D':
            if b_y-1 < -5: continue
            a_y = b_y-1
        elif item == 'R':
            if b_x+1 > 5: continue
            a_x = b_x+1
        

        if (a_y,a_x) not in graph[b_y][b_x]:
            graph[b_y][b_x].append((a_y,a_x))
            graph[a_y][a_x].append((b_y,b_x))
            answer += 1
        b_x = a_x
        b_y = a_y
                
    print(f'answer = {answer}')
    return

#dirs = "ULURRDLLU"
dirs = "LULLLLLLU"
print(f'solution = {solution(dirs)}')

