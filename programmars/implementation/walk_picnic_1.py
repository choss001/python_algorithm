import sys

def solution(park, routes):
    n_y,n_x = 0,0
    move_dic = {'E':(0,1),'N':(-1,0),'S':(1,0),'W':(0,-1)}
    for i in range(len(park)):
        for k in range(len(park[0])):
            if park[i][k] == 'S':
                n_y,n_x=i,k
    for i in routes:
        print(f'i = {i}')
        flag = True
        temp_y, temp_x = n_y, n_x
        for k in range(int(i[2])):
            print(f'k = {k}')
            temp_y += move_dic[i[0]][0]
            temp_x += move_dic[i[0]][1]
            print(f'temp_y={temp_y}, temp_x={temp_x}')
            if 0 > temp_y or temp_y >= len(park) or \
                0 > temp_x or temp_x >= len(park[0]):
                    flag = False
                    break
            if park[temp_y][temp_x] == 'X':
                flag = False
                break
        print(f'flag = {flag}')
        if flag: n_y,n_x = temp_y, temp_x
        print(f'n_y={n_y}, n_x={n_x}')
    return [n_y,n_x]
#park, routes = ["SOO","OXX","OOO"], ["E 2","S 2","W 1"]
#park, routes = ["SOO","OOO","OOO"], ["E 2","S 2","W 1"]
park, routes = ["OSO","OOO","OXO","OOO"], 	["E 2","S 3","W 1"]

print(f'solution = {solution(park,routes)}')


#solution()
#    find s
#    move route
#    just one stem and check wall every time
#    if move to wall then skip 
#temp_y = move_dic + n_y
#if move wall or obstrac:
#break
#if temp_y <= range:
#    n_y = temp_y
    
