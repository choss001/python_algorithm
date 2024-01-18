import sys
input = sys.stdin.readline
import heapq
from collections import deque



N, M = map(int, input().split())
start = int(input())

graph = [[] for _ in range(N+1)]

def dijkstra(start, end):
    distance_lst = [999999999] * (N+1)
    q = []
    heapq.heappush(q, (0, start))
    while q:
        print(f'q = {q}')
        distance, s = heapq.heappop(q) 
        if distance_lst[s] < distance:
            continue
        for i in graph[s]:
            t, accumulate = i
            if distance+accumulate >= distance_lst[t]:
                continue
            distance_lst[t] = distance + accumulate
            heapq.heappush(q, (distance_lst[t], t))

    return distance_lst

for i in range(M):
    u,v,w = map(int, input().split())
    graph[u].append((v,w))
distance_lst = dijkstra(start,0)

for i in range(1,N+1):
    if start == i:
        print(0)
        continue
    if distance_lst[i] == 999999999:
        print(f'INF')
        continue
    print(distance_lst[i])


graph = [[], [(2, 2), (3, 3)], [(3, 4), (4, 5)], [(4, 6)], [], [(1, 1)]]
distance_lst = [999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999]
distance,s = 0, 1
distance_lst[1] = 999999999
distance = 0

(2,2)
t, accumulate = 2, 2

distance_lst[2] = 0 + 2
q = (2, 2)
distance_lst = [999999999, 999999999, 2, 999999999, 999999999, 999999999, 999999999, 999999999, 999999999]
t, accumulate = 3, 3
distance_lst[3] = 0 + 3
distance_lst = [999999999, 999999999, 2, 3, 999999999, 999999999, 999999999, 999999999, 999999999]
q = (2, 2), (3, 3)
==========================

distance,s = 2, 2
distance_lst[2] = 2    , distance = 2
q = (3,3)

graph[2] = [(3, 4), (4, 5)]
t, accumulate = 3, 4
distance+ accumulate = distance_lst[3]
2 + 4 = 3
continue

t, accumulate = 4, 5
2 + 5 >= 9999999
distance_lst[4] = 7
distance_lst = [999999999, 999999999, 2, 3, 7, 999999999, 999999999, 999999999, 999999999]
q = 5, 4

============================
distance, s = 5, 4
7, 5
for 


