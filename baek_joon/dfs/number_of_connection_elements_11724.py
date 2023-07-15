import sys
input = sys.stdin.readline
import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N+1)

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


answer = 0
li = []
for i in range(1, N+1):
    if visited[i] == 0:
        answer += 1
        heapq.heappush(li, i)
        while li:
            cur_position = heapq.heappop(li)
            for k in graph[cur_position]:
                if visited[k] == 0 :
                    visited[k] = 1
                    heapq.heappush(li, k)
print(answer)
