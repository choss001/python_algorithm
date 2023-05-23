import heapq

#m,n,a,b,c,d = 8, 5, 5, 3, 2, 1
#location_map = [
#    [1, 5, 10, 3, 7, 1, 2, 5],
#    [6, 12, 4, 4, 3, 3, 1, 5],
#    [2, 4, 3, 1, 6, 6, 19, 8],
#    [1, 1, 1, 3, 4, 2, 4, 5],
#    [6, 6, 3, 3, 3, 2, 2, 2]
#]

m,n,a,b,c,d = map(int, input().split())
location_map = [list(map(int, input().split())) for _ in range(n)]


piramids = []
rooms = []

answer_average = 0
answer_list = []

#width
for i in range(m - a + 1):
    #height
    for j in range(n - b + 1):
        result_map = [location_map[k][i:i+a] for k in range(j, j+b)]
        piramids.append([sum(sum(result_map,[])), j, i])
#width
for i in range(1, m - c):
    #height
    for j in range(1, n - d):
        result_map = [location_map[k][i:i+c] for k in range(j, j+d)]
        rooms.append([sum(sum(result_map, [])), j, i])

rooms.sort()
piramids.sort(reverse=True)
while piramids:
    p_sum, p_y, p_x = piramids.pop(0) 
    for r_sum, r_y, r_x in rooms:
        if (p_y < r_y and p_y+b-d > r_y) and (p_x < r_x and p_x+a-c > r_x):
            temp_average = (p_sum-r_sum)/(a*b-c*d)
            if answer_average < temp_average:
                answer_average = temp_average
                answer_list = [p_x+1, p_y+1, r_x+1, r_y+1]
            #print(f'p_y = {p_y}, p_x = {p_x}, r_y = {r_y}, r_x = {r_x}, p_sum = {p_sum}, r_sum = {r_sum}, aver={(p_sum-r_sum)/(a*b-c*d)}')
            

print(f'{answer_list[0]} {answer_list[1]}')
print(f'{answer_list[2]} {answer_list[3]}')


