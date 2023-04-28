import heapq

N, M = map(int, input().split())

graph = [[[] for _ in range(M+1)] for _ in range(N+1)]

print(graph)

dist = [[float('inf') for _ in range(M+1)] for _ in range(N+1)]

def dijkstra(start_x, start_y):
    dist[start_y][start_x] = 0
    pq = [(0, (start_x, start_y))]
    while pq:
        val, (x, y) = heapq.heappop(pq)
        if dist[y][x] < val:
            continue
        for w, (nx, ny) in graph[y][x]:
            new_val = val + w
            if dist[ny][nx] > new_val:
                dist[ny][nx] = new_val
                heapq.heappush(pq, (new_val, (nx, ny)))

for i in range(N):
    s = input()
    for j in range(M):
        if s[j] == '/':
            graph[i][j+1].append((0, (j, i+1)))
            graph[i+1][j].append((0, (j+1, i)))
            graph[i][j].append((1, (j+1, i+1)))
            graph[i+1][j+1].append((1, (j, i)))
        else:
            graph[i][j].append((0, (j+1, i+1)))
            graph[i+1][j+1].append((0, (j, i)))
            graph[i][j+1].append((1, (j, i+1)))
            graph[i+1][j].append((1, (j+1, i)))
for i in graph:
    for j in i:
        print(j)

dijkstra(0, 0)
if dist[N][M] == float('inf'):
    print('NO SOLUTION')
else:
    print(dist[N][M])
