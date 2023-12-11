import sys
input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())

graph = [[] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(f'{graph}')
