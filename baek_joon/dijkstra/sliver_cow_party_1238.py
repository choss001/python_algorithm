import sys
input = sys.stdin.readline

N,M,T=map(int,input().split())
graph = [[1e9] *(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a][b]=c

for k in range(N+1):
    for a in range(N+1):
        for b in range(N+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
            answer = 0
for i in range(1,N+1):
    answer = max(answer, graph[i][2]+graph[2][i])
print(answer)
