import sys
input = sys.stdin.readline
import heapq

def dijkstra(start):
    distance[start] = 0

    q = []
    heapq.heappush(q, (0,start))
    while q:
        print(f'q ={q}')
        d,p = heapq.heappop(q)

        for g_i in graph[p]:
            if g_i[0]+d < distance[g_i[1]]:
                print(f'g_i={g_i}, p={p},{d}')
                distance[g_i[1]] = g_i[0]+d
                heapq.heappush(q, (g_i[0]+d, g_i[1]))


    return 0

    

N,M = map(int,input().split())
S = int(input())

graph = [[] for _ in range(N+1)]
distance = [9999999] * (N+1)
print(f'graph = {graph}')
for i in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((c,b))
print(f'graph = {graph}')

dijkstra(S)
print(f'distance = {distance}')

for i in range(1, N+1): print(distance[i] if distance[i] != 9999999 else 'INF')

