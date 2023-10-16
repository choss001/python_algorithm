from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split()) 
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])
def bfs():
    while queue:
        print(f'queue = {queue}')
        x, y = queue.popleft()
        print(f'x= {x}, y = {y}')
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                print(f'meet the condition! nx = {nx}, ny = {ny}')
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny)) 

bfs()
print(f'graph = {graph}')
day = 0
for row in graph:
    for i in row:
        if i == 0:  
            print(-1)
            exit() 
    else: 
        day = max(day, max(row)) 

print(day-1)
