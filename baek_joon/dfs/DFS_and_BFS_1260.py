import heapq

N, M, E = map(int, input().split())
vertex_DFS = [[] for _ in range(N + 1)]
vertex_BFS = [[] for _ in range(N + 1)]
visited_DFS = [i+1 for i in range(N+1)]
visited_BFS = [i+1 for i in range(N+1)]
DFS_answer = []
BFS_answer = []

for _ in range(M):
    a,b = map(int, input().split())
    vertex_DFS[a].append(b)
    vertex_DFS[b].append(a)
    vertex_BFS[a].append(b)
    vertex_BFS[b].append(a)

def DFS(E):
    DFS_answer.append(E)

    if len(vertex_DFS[E]) == 0:
        return

    heapq.heapify(vertex_DFS[E])
    for i in range(len(vertex_DFS[E])):
        next = heapq.heappop(vertex_DFS[E])
        if visited_DFS[next] == 1:
            continue
        visited_DFS[next] = 1
        DFS(next)

def BFS(E):
    BFS_answer.append(E)
    if len(vertex_BFS[E]) == 0:
        return

    li = [E]
    while li:
        #current = heapq.heappop(li)
        current = li.pop(0)
        if len(vertex_BFS[current]) == 0:
            return
        heapq.heapify(vertex_BFS[current])
        for i in range(len(vertex_BFS[current])):
            next = heapq.heappop(vertex_BFS[current])
            if visited_BFS[next] == 1:
                continue
            #heapq.heappush(li, next)
            li.append(next)
            visited_BFS[next] = 1
            BFS_answer.append(next)

visited_DFS[E] = 1
DFS(E)
visited_BFS[E] = 1
BFS(E)
#print(*DFS_answer)
#print(*BFS_answer)
for i in DFS_answer:
    print(i,end=' ')
print()
for i in BFS_answer:
    print(i,end=' ')
