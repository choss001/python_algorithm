import sys
input = sys.stdin.readline

def solution(k, ranges):
    array_dot = [[0,k]]
    array_dot = hail_sequence(array_dot)
    print(f'array_dot={array_dot}')
    answer_list = []

    array_temp = get_width_array(array_dot)

    for g in ranges:
        if g[0] == 0 and g[1] == 0:
            answer_list.append(sum(array_temp))
            continue
        if g[0] >= len(array_dot) or -g[1] > len(array_dot):
            answer_list.append(-1)
            continue

        print(f'g[0]={g[0]},g[1]={g[1]}')
        start = array_dot[g[0]][0]
        end = len(array_temp) if g[1] == 0 else array_dot[g[1]][0]-1
        print(f'start={start},end={end}')
        if start <= end :
            print(f'sum = {sum(array_temp[start:end])}')
            answer_list.append(sum(array_temp[start:end]))
        else:
            answer_list.append(-1)


    print(f'array={array_temp}')
    print(f'answer_list={answer_list}')

    return answer_list

def get_width_array(array_dot):
    array = []
    for i in range(len(array_dot)-1):
        temp = (array_dot[i][1]+array_dot[i+1][1])/2
        array.append(temp)
    print(f'array in function = {array}')
    return array


def hail_sequence(array_dot):
    print(f'array_dot in function = {array_dot}')
    x = array_dot[-1][0]
    number = array_dot[-1][1]
    if number <= 1:
        print(f'return array_dot = {array_dot}')
        return array_dot
    if number % 2 == 0:
        array_dot.append([x+1,number//2])
        array_dot = hail_sequence(array_dot)
    else:
        array_dot.append([x+1,number*3+1])
        array_dot = hail_sequence(array_dot)
    return array_dot
    

k,ranges = 5, [[0,0],[0,-1],[0,-2],[1,-1],[2,-2],[2,-3],[5,0],[4,0]]
solution(k,ranges)

#[[0, 5], [1, 16], [2, 8], [3, 4], [4, 2], [5, 1]]
#[10.5, 12.0, 6.0, 3.0, 1.5]
#[[0,0],[0,-1],[2,-3],[3,-3]]
#[33.0,31.5,0.0,-1.0]
#0,0 전체

#0, -1 => sum(0~6)
#0, -2 => sum(0~5)
#0, -3 => sum(0~4)
#array_dot[s][0], 

#k = 10000
#array_dot=[[0, 10000], [1, 5000], [2, 2500], [3, 1250], [4, 625], [5, 1876], [6, 938], [7, 469], [8, 1408], [9, 704], [10, 352], [11, 176], [12, 88], [13, 44], [14, 22], [15, 11], [16, 34], [17, 17], [18, 52], [19, 26], [20, 13], [21, 40], [22, 20], [23, 10], [24, 5], [25, 16], [26, 8], [27, 4], [28, 2], [29, 1]]


