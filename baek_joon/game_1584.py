import heapq

input_map = [[0 for _ in range(500)] for _ in range(500)]

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
dist = [[float('inf') for _ in range(500)] for _ in range(500)]



def dijkstra(start_y, start_x):
    dist[start_y][start_x] = 0
    pq = [(0, (start_y, start_x))]    

    while pq:
        val ,(y, x) = heapq.heappop(pq)

        for d_val, (dy, dx) in graph[y][x]:
            new_val = d_val + val
            if new_val < dist[dy][dx]:
                heapq.heappush(pq, (new_val, (dy, dx)))
                dist[dy][dx] = new_val
        

for k in range(len(danger)):
    for i in range(min(danger[k][0], danger[k][2]), max(danger[k][0], danger[k][2])):
        for j in range(min(danger[k][1], danger[k][3]), max(danger[k][1], danger[k][3])):
            input_map[j][i] = 1

for k in range(len(death)):
    for i in range(min(death[k][0], death[k][2]), max(death[k][0], death[k][2])):
        for j in range(min(death[k][1], death[k][3]), max(death[k][1], death[k][3])):
            input_map[j][i] = 6

for i in range(500):
    for j in range(500):
        for dc in d:
            dy = j + dc[0]
            dx = i + dc[1]
            if 0 > dy or 0 > dx or dy >= 500 or dx >= 500:
                continue
            if input_map[dy][dx] == 1:
                graph[j][i].append((1, (dy, dx)))
            elif input_map[dy][dx] == 0:
                graph[j][i].append((0, (dy, dx)))

dijkstra(0, 0)
print(dist[499][499])
for i in range(240, 280):
    print()
    for j in range(240, 280):
        print(f'{dist[i][j]:5}', end='')
#for i in range(240, 280):
#    print()
#    for j in range(240, 280):
#        print(f'{input_map[i][j]:3}', end='')
