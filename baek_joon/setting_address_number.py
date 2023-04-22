m =  int(input())
array = [list(map(int, input())) for _ in range(m)]
visited = [[False for _ in range(m)] for _ in range(m)]

the_number_of_home = 0
temp_sum =0
temp_array = []

ty = [1,0,-1,0]
tx = [0,1,0,-1]

def recursive(y, x):
    global array
    global visited
    global temp_sum
    if array[y][x] == 1 and visited[y][x] == False:
        visited[y][x] = True
        temp_sum +=1
        for i in range(4):
            ay = y+ty[i]
            ax = x+tx[i]
            if ay >= 0 and ax >= 0 and ay < m and ax < m:
                recursive(y+ty[i], x+tx[i])
        return 1
    return 0


for x in range(m):
    for y in range(m):
        the_number_of_home += recursive(y,x)
        if temp_sum != 0:
            temp_array.append(temp_sum)
            temp_sum = 0

print(the_number_of_home)
temp_array.sort()
for result in temp_array:
    print(result)
