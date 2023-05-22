#m,n,a,b,c,d = 8, 5, 5, 3, 2, 1
#location_map = [
#    [1, 5, 10, 3, 7, 1, 2, 5],
#    [6, 12, 4, 4, 3, 3, 1, 5],
#    [2, 4, 3, 1, 6, 6, 19, 8],
#    [1, 1, 1, 3, 4, 2, 4, 5],
#    [6, 6, 3, 3, 3, 2, 2, 2]
#]

import sys
input = sys.stdin.readline


m,n,a,b,c,d = map(int, input().split())
location_map = [list(map(int, input().split())) for _ in range(n)]


temp_height = 0
answer_list = []
for i in range(m -a + 1):
    for j in range(n -b + 1):
        sum_temp = 0
        temp_list= []
        for item in location_map[j:j+b]:
            temp_list.append(item[i:i+a])
            sum_temp += sum(item[i:i+a])

        for l in range(1, a-c):
            temp_temp_list = []
            sum_temp_temp = 0
            for k in range(1, b-d):
                temp_temp_list.append(temp_list[k][l:l+c])
                sum_temp_temp += sum(temp_list[k][l:l+c])
                
            average = (sum_temp - sum_temp_temp) / ((a*b) - (c*d))
            if temp_height < average :
                answer_list = [i+1, j+1, i+l+1, j+k+1]
                temp_height = average

print(f'{answer_list[0]} {answer_list[1]}')
print(f'{answer_list[2]} {answer_list[3]}')

        
