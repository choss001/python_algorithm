import sys
input = sys.stdin.readline
import heapq

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
def dijkstra(start):
    heapq.heappush(q, (start, 0))
    distance[start] = 0

    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))
for i in range(1, N+1):
    distance = [1e9] * (N+1)
    q = []
    dijkstra(i)
    for i in range(1, N+1):
        if distance[i] == 1e9:
            print(0, end=' ')
        else:
            print(distance[i],end=' ')
    print()
    


