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
    distance_lst = [999999999] * (N+1)
    distance_lst[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dis, v = heapq.heappop(q)

        if distance_lst[v] < dis:
            continue

        for i in graph[v]:
            cost = i[1] + dis
            if cost >= distance_lst[i[0]]:
                continue
            distance_lst[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))


    return distance_lst

S,E = map(int, input().split())
print(dijkstra(S)[E])

