import sys
input = sys.stdin.readline

def solution(line):

    cross_point = []
    min_x, max_x, min_y, max_y =  1000000000000000, -1000000000000000, 1000000000000000, -1000000000000000
    for i in range(len(line)):
        for k in range(i+1, len(line)):
            A,B,E = line[i][0], line[i][1],line[i][2]
            C,D,F = line[k][0], line[k][1],line[k][2]
            if A*D - B*C == 0:
                continue
            x = (B*F - E*D) / (A*D - B*C)
            y = (E*C - A*F) / (A*D - B*C)
            if x.is_integer() and y.is_integer():
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                min_y = min(min_y, y)
                max_y = max(max_y, y)
                cross_point.append((x, y))
    answer_lst =[['.' for _ in range(int(max_x-min_x+1))] for _ in range(int(max_y-min_y+1))]
    print(f'answer_lst={answer_lst}')
    print(f'cross_point = {cross_point}')
    print(f'max_x,min_x = {max_x}, {min_x}, max_y, min_y = {max_y}, {min_y}')
    for item in cross_point:
        x, y = item
        x -= min_x
        y -= min_y
        print(f'y = {y}, x = {x}')
        answer_lst[int(y)][int(x)] = '*'

    answer = []
    for i in answer_lst[::-1]:
        print(f'{"".join(i)}')
        answer.append(''.join(i))

    return answer

#line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
#line = [[0, 1, -1], [1, 0, -1], [1, 0, 1]]
#line = [[1, -1, 0], [2, -1, 0]]
line = [[0,1,0],[1,0,5],[1,0,-3]]
#line = [[1,1,0],[1,-1,0]]
#line = [[1,-3,0],[1,0,-3]]
print(solution(line))
