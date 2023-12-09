import sys
input = sys.stdin.readline
import heapq


N, M =map(int, input().split())
graph = [[] for _ in range(N+1)]


for _ in range(N):
    a, b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

def dijkstra(start):
    q=[]

    heapq.heappush(q,(start,0))
    distance[start] = 0
    
    while q:
        now, dist = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(i[0],cost))

answer = int(1e9)
for i in range(1,N+1):
    distance = [int(1e9)]* (N+1)
    dijkstra(i)
    answer = min(answer, sum(distance[1:N+1]))
print(answer)

