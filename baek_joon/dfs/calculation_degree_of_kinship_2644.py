import sys
input = sys.stdin.readline

N = int(input())
A, B = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(int(input())):
    C,D = map(int,input().split())
    graph[C].append(D)
    graph[D].append(C)
    
real_answer = 0
def dfs(start, answer):
    global real_answer
    if start == B:
        real_answer = answer
    for i in graph[start]:
        if visited[i] == False:
            visited[i] = True
            answer += 1
            dfs(i, answer)
            visited[i] = False
            answer -= 1
            
visited[A] = True
dfs(A, 0)
print(-1 if real_answer == 0 else real_answer)
