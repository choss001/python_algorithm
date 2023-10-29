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

answer_graph = []
answer = 0
for i in range(1,N+1):
    distance = [1e9] * (N+1)
    dijkstra(i)
    answer_graph.append(distance[1:])
for i in range(N):
    #print(f'answer_graph[i][1]={answer_graph[i][1]}, answer_graph[1][i]={answer_graph[1][i]}')
    if i!=1:
        answer = max(answer, answer_graph[i][T-1]+answer_graph[T-1][i])
print(answer)

#for i in range(N):
    #print(answer_graph[i])
