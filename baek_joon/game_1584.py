import heapq

input_map = [[0 for _ in range(501)] for _ in range(501)]

#N = 1
#danger =  [500, 0, 0, 500]
#M = 1
#death = [0, 0, 0, 0]

#d = [(-1, 0), (-1,1), (0, 1), (1,1 ), (1,0), (1, -1), (0, -1), (-1, -1)]
d = [(-1, 0), (0, 1), (1,0), (0, -1)]

N = 2
danger = [[0, 0, 250, 250], [250, 250, 500, 500]]
M = 2
death = [[0, 251, 249, 500], [251, 0, 500, 249]]

graph = [[[] for _ in range(501)] for _ in range(501)]
dist = [[float('inf') for _ in range(501)] for _ in range(501)]



def dijkstra(start_y, start_x):

    f = open('test_log.txt', 'w+')
    dist[start_y][start_x] = 0
    pq = [(0, (start_y, start_x))]    

    while pq:
        val ,(y, x) = heapq.heappop(pq)
        f.write('val={0:4d},y={1:3d},x={2:3d}\n'.format(val,y,x))

        for d_val, (dy, dx) in graph[y][x]:
            f.write('\td_val={0:4d},dy={1:3d},dx={2:3d}\n'.format(d_val,dy,dx))
            new_val = d_val + val
            if new_val < dist[dy][dx]:
                f.write('\t\tnew_val={0:4.0f},oldDist[{1:3d}][{2:3d}]={3:4.0f}\n'.format(new_val,dy,dx,dist[dy][dx]))
                heapq.heappush(pq, (new_val, (dy, dx)))
                dist[dy][dx] = new_val
    f.close()
        

for k in range(len(danger)):
    for i in range(min(danger[k][0], danger[k][2]), max(danger[k][0], danger[k][2]) + 1):
        for j in range(min(danger[k][1], danger[k][3]), max(danger[k][1], danger[k][3]) + 1):
            input_map[j][i] = 1

for k in range(len(death)):
    for i in range(min(death[k][0], death[k][2]), max(death[k][0], death[k][2]) + 1):
        for j in range(min(death[k][1], death[k][3]), max(death[k][1], death[k][3]) + 1):
            input_map[j][i] = 6

for i in range(501):
    for j in range(501):
        for dc in d:
            dy = j + dc[0]
            dx = i + dc[1]
            if 0 > dy or 0 > dx or dy >= 501 or dx >= 501:
                continue
            if input_map[dy][dx] == 1:
                graph[j][i].append((1, (dy, dx)))
            elif input_map[dy][dx] == 0:
                graph[j][i].append((0, (dy, dx)))

dijkstra(0, 0)
#for i in range(160, 180):
#    print()
#    for j in range(160, 180):
#        print(f'{dist[i][j]:5} {i},{j}', end='')
#for i in range(0, 500):
#    print()
#    for j in range(240, 260):
#        print(f'{input_map[i][j]:3}', end='')
#for i in range(500):
#    print(f'{graph[0][i]}', end='')
#print(f'{input_map[249][249]}')
#print(f'{input_map[250][249]}')
print(dist[500][500])
with open('test.txt', 'w+')as f:
    for i in range(500):
        for j in range(500):
            f.write('\ncurrent cooldinate (y={0:3d},x={1:3d})\n'.format(i, j))
            for k in range(len(graph[i][j])):
                f.write('value = {0:1d}, after cooldinate = (y={1:3d},x={2:3d}) ||| '.format(graph[i][j][k][0], graph[i][j][k][1][0], graph[i][j][k][1][1]))

with open('test_dist.txt', 'w+')as f:
    for i in range(500):
        f.write('\n')
        for j in range(500):
            if j%9 ==0:
                f.write('\n')
            f.write('dist={0:4.0f}, y={1:3d} ,x={2:3d} ||| '.format(dist[i][j], i, j))
#    for i in range(160, 180):
#        f.write('\n')
#        for j in range(160, 180):
#            f.write('||d={0:5d},y={1:5d},x={2:5d}'.format(dist[i][j], i, j))

