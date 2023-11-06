import sys
input = sys.stdin.readline
import heapq
from collections import deque

N, M = map(int, input().split())
start = int(input())
graph = [[] for _ in range(N+1)]
distance = [1e9]*(N+1)

for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
def dijkstra(start):
    q = []
    q = deque()
    q.appendleft((start, 0))
    distance[start] = 0

    while q:
        now, dist = q.popleft()
        print(f'now={now}, dist={dist}, distance={distance}')

        if distance[now] < dist:
            print(f'continue')
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                    print(f'true cost={cost}, distance[i[0]]={distance[i[0]]}, i={i}')
                    distance[i[0]] = cost
                    q.append((i[0], cost))


dijkstra(start)
print(f'{distance}')

