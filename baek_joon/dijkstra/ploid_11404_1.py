import sys
INF = int(1e9)

n = int(sys.stdin.readline())  # 도시의 수
m = int(sys.stdin.readline())  # 버스의 수

graph = [[INF] * (n + 1) for _ in range(n + 1)]    # 모든 최단 거리를 저장
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0
for i in range(n+1):
    print(f'{graph[i]}')
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(c, graph[a][b])   # 노선이 하나가 아닐 수 있음 > 최소값 넣기 
for i in range(n+1):
    print(f'{graph[i]}')

# 2. 다이나믹 프로그래밍
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            print('k={0:2d} a={1:2d} b={2:2d}\
 graph[a][b]={3:10d} graph[a][k]={4:10d} graph[k][b]={5:10d}'.format(k,a,b,graph[a][b],graph[a][k],graph[k][b]))
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
for i in range(n+1):
    print(f'{graph[i]}')

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("0",  end=" ")
        else:
            print(graph[a][b], end=" ")
    print()
