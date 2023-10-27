import heapq
import sys
input = sys.stdin.readline
INF = 1e9

v,e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
distance = [INF]*(v+1)

for i in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
print(graph)
def dijstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        list(q)
        print(f'q = {q}')
        heapq.heapify(q)
        dist, now = heapq.heappop(q)
        print(f'dist={dist},now={now}')

        if distance[now] < dist:
            print(f'distance[now]={distance[now]},dist={dist} distance row than dist so that coninue')
            continue

        for i in graph[now]:
            cost = dist + i[1]
            print(f'dist={dist}, i={i}, distance[i[0]]={distance[i[0]]},cost={cost}')
            if cost < distance[i[0]]:
                print(f'cost row than distance so pointer can here')
                distance[i[0]] = cost
                print(f'distance[{i[0]}]={distance}')
                heapq.heappush(q, (cost, i[0]))

dijstra(start)

for i in range(1, v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
