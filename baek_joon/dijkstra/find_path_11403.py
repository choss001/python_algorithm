import sys
input = sys.stdin.readline

N = int(input())

graph = [list(map(int,input().split())) for _ in range(N)]
for a in range(N):
    for b in range(N):
        if graph[a][b] == 0:
            graph[a][b] = 1e9

for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(N):
    for b in range(N):
        if graph[a][b] != 1e9:
            graph[a][b] = 1
        else:
            graph[a][b] = 0
for a in range(N):
    print(f"{' '.join(map(str,graph[a]))}")
