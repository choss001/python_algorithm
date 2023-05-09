import heapq
import sys
input = sys.stdin.readline

N = int(input())
danger = [list(map(int, input().split())) for _ in range(N)]

M = int(input())
death = [list(map(int, input().split())) for _ in range(M)]

input_map = [[0] * 501 for _ in range(501)]
d = [(-1, 0), (0, 1), (1,0), (0, -1)]

graph = [[[] for _ in range(501)] for _ in range(501)]
dist = [[float('inf') for _ in range(501)] for _ in range(501)]



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
        
if N:
    for k in range(len(danger)):
        for i in range(min(danger[k][0], danger[k][2]), max(danger[k][0], danger[k][2]) + 1):
            for j in range(min(danger[k][1], danger[k][3]), max(danger[k][1], danger[k][3]) + 1):
                input_map[j][i] = 1

if M:
    for k in range(len(death)):
        for i in range(min(death[k][0], death[k][2]), max(death[k][0], death[k][2]) + 1):
            for j in range(min(death[k][1], death[k][3]), max(death[k][1], death[k][3]) + 1):
                input_map[j][i] = 6

for i in range(501):
    for j in range(501):
        for dc in d:
            dy = j + dc[0]
            dx = i + dc[1]
            if not (0 <= dy < 501 and 0 <= dx < 501):
                continue
            if input_map[dy][dx] == 1:
                graph[j][i].append((1, (dy, dx)))
            elif input_map[dy][dx] == 0:
                graph[j][i].append((0, (dy, dx)))

dijkstra(0, 0)
print(dist[500][500] if dist[500][500] != float('inf') else -1)
