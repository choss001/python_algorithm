import sys
input = sys.stdin.readline
import heapq

N,M,T = map(int,input().split())
graph = [[] for _ in range(N+1)]

def dijkstra(start):
    q=[]
    heapq.heappush(q,(start, 0))

    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1]+dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(i[0],cost))

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

answer = 0

party_graph = []
distance = [1e9] * (N+1)
dijkstra(T)
party_graph = distance[0:]
for i in range(1,N+1):
    distance = [1e9] * (N+1)
    dijkstra(i)
    answer = max(answer, distance[T]+party_graph[i])
    print(f'distance = {distance},i={i}, party_graph={party_graph}\
            distance[{T}]={distance[T]}, party_graph[{i}]={party_graph[i]}')
print(answer)
