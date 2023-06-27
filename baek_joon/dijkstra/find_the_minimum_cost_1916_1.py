# floyd-warshall... too long!
import sys
input = sys.stdin.readline

INF = int(1e10)

V = int(input())
E = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    i, j, k = map(int, input().split())
    graph[i].append((j, k)) # graph[start].append(end, weight)

visited = [False] * (V+1)
distance = [INF] * (V+1)

def get_min():
    min_val = INF
    index = 0
    for i in range(1, V+1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for i in graph[start]:
        distance[i[0]] = min(distance[i[0]], i[1]) # if start == end

    for _ in range(V-1):
        now = get_min()
        visited[now] = True

        for j in graph[now]:
            if distance[now] + j[1] < distance[j[0]]:
                distance[j[0]] = distance[now] + j[1]
start, end = map(int, input().split())
dijkstra(start)
print(distance[end])
