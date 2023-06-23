import sys
from collections import deque
input = sys.stdin.readline

C = int(input())
L = int(input())
edge_list =[]
graph = [[] for _ in range(C+1)]
visited = [False for _ in range(C+1)]
answer_list =[1]

for _ in range(L):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

l = deque([1])
visited[1] = True
while l:
    start = l.popleft()
    for i in graph[start]:
        if visited[i] == False:
            visited[i] = True
            answer_list.append(i)
            l.append(i)
print(len(answer_list) - 1)
