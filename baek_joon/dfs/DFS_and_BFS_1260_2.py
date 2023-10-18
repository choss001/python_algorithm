import sys
input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())
graph = [[] * (N + 1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

    
for i in graph:
    i.sort()

print(f'{graph}')

def dfs(start):
    visited[start] = True
    print(start, end=" ")

    for i in graph[start]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        k = q.popleft()
        print(f'bfs = {k}')
        for i in graph[k]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True
        

    
    
visited = [False] * (N +1)
dfs(V)
print()

visited = [False] * (N+1)
bfs(V)
print()
