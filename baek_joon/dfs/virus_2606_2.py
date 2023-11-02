import sys
input = sys.stdin.readline


N = int(input())
M = int(input())
graph = [[] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b= map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(start):
    global answer_count
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False:
            answer_count += 1
            dfs(i)
    
answer_count = 0
dfs(1)
print(f'{answer_count}')
