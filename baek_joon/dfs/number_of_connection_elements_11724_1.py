import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

def bfs(start):
    for k in graph[start]:
        if visited[k] == False:
            visited[k] = True
            bfs(k)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
answer = 0
for k in range(1, N+1):
    if visited[k] == False:
        visited[k] = True
        bfs(k)
        answer += 1
print(f'{answer}')
