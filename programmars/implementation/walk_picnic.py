def solution(park, routes):
    n_y = 0
    n_x = 0
    
    dic_move = {'E':(1,0), 'W':(-1,0), 'S': (0,1), 'N':(0,-1)}

    for i in range(len(park)):
        for k in range(len(park[0])):
            if park[i][k] == 'S':
                n_y,n_x = i,k
                break
    for r in routes:
        temp_y = dic_move[r[0]][1] * int(r[2])
        temp_x = dic_move[r[0]][0] * int(r[2])
        if temp_y >= len(park) or temp_y < 0 or temp_x < 0 or temp_x >=len(park[0]):
            continue


    
    return 0

park, routes = ["SOO","OOO","OOO"], ["E 2","S 2","W 1"]

print(solution(park, routes))
