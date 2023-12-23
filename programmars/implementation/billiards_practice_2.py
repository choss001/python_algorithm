import math
import sys

def solution(m, n, startX, startY, balls):
    answer_list = []
    start_list = [[-startX,startY], [startX,-startY],
            [startX,startY+(n-startY)*2],[startX+(m - startX)*2,startY]]
    for ball in balls:
        answer_list.append(get_length(ball, start_list))
    return answer_list
def get_length(ball,start_list):
    temp_answer = sys.maxsize
    for i in range(len(start_list)):
#       if ball[0] == start[0] or ball[1] == start[1]:
#           continue
        print(f'ball[0],ball[1]={ball[0],ball[1]}, start x,y = {start_list[i][0], start_list[i][1]}')
        if i == 0 and ball[1] == start_list[i][1] and ball[0] < abs(start_list[i][0]):
            continue
        if i == 1 and ball[0] == start_list[i][0] and ball[1] < abs(start_list[i][1]):
            continue
        if i == 2 and ball[0] == start_list[i][0] and ball[1] > abs(start_list[0][1]):
            continue
        if i == 3 and ball[1] == start_list[i][1] and ball[0] > abs(start_list[0][0]):
            continue
        print(f'ball[0],ball[1]={ball[0],ball[1]}, start x,y = {start_list[i][0], start_list[i][1]}')
        temp = (ball[0]-start_list[i][0])**2 + (ball[1]-start_list[i][1])**2

        temp_answer = min(temp_answer,temp ) 
    return temp_answer

#m,n,startX,startY,balls = 10,10,3,7,[[7, 7], [2, 7], [7, 3]]
m,n,startX,startY,balls = 4,2,1,1,[[1,2]]


print(solution(m,n,startX,startY,balls))
