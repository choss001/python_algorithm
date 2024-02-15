def solution(places):
    square_base = [[(-1,-1),(-1,0),(0,-1)],[(-1,1),(-1,0),(0,1)],[(1,1),(1,0),(0,1)],[(1,-1),(0,-1),(0,-1)]]
    distance_base = [[(-2,0),(-1,0)],[(0,2),(0,1)],[(2,0),(1,0)],[(0,-2),(0,-1)]]
    near_base = [(-1,0),(0,1),(1,0),(0,-1)]


    def check(i, j, place):
        for s in square_base:
            if i+s[0][0] < 0 or i+s[0][0] > 4 or j+s[0][1] < 0 or j+s[0][1] > 4: continue
            if place[i+s[0][0]][j+s[0][1]] != 'P': continue
            if not (place[i+s[1][0]][j+s[1][1]] == 'X' and place[i+s[2][0]][j+s[2][1]] == 'X'):
                print(f'i={i}, j={j}, s = {s}')
                print(f'place[i+s[1][0]][j+s[1][1]] = {place[i+s[1][0]][j+s[1][1]]}, place[i+s[2][0]][j+s[2][1]]={place[i+s[2][0]][j+s[2][1]]}')
                return 0
        for d in distance_base:
            if i+d[0][0] < 0 or i+d[0][0] > 4 or j+d[0][1] < 0 or j+d[0][1] > 4: continue
            if place[i+d[0][0]][j+d[0][1]] != 'P': continue
            if place[i+d[1][0]][j+d[1][1]] != 'X' or place[i+d[1][0]][j+d[1][1]] != 'X':
                print(f'place[i+d[1][0]][j+d[1][1]] ={place[i+d[1][0]][j+d[1][1]]}, place[i+d[1][0]][j+d[1][1]]={place[i+d[1][0]][j+d[1][1]]}')
                print(f'i={i}, j={j}')
                return 0
        for n in near_base:
            if i+n[0] < 0 or i+n[0] > 4 or j+n[1] < 0 or j+n[1] > 4: continue
            if place[i+n[0]][j+n[1]] == 'P' :
                print(f'place[i+n[0]][j+n[1]] = {place[i+n[0]][j+n[1]]}')
                print(f'i={i}, j={j}')
                return 0
        return 1

#   for place in places:
#       print(f'')
#       for i in place:
#           print(f'i={i}')

    answer = []
    for place in places:
        temp_check_bool = 1
        print()
        for i in place:
            print(f'i={i}')

        for i in range(5):
            if not temp_check_bool: break
            for j in range(5):
                if place[i][j] == 'P':
                    temp_check_bool = check(i,j,place)
                    if not temp_check_bool: break
        answer.append(temp_check_bool)                


    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))

#pseudo code



#POO     P=(0,0)
#XPO     square_xy = [[(-1,-1),(-1,0),(0,-1)],[],[],[]]
#POO
#        P=(1,1)
#
#        def check():
#            if ~~~~
#            return 0
#
#            for 
#                if P[x-square_x][y-square_y] == 'P' and (item[x-square_x][y-square_y] = 'O' or item[x-square_x][y-square_y] == 'O')
#                return 0
#
#            for ~
#                if ~
