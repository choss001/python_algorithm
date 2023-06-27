import sys
input = sys.stdin.readline


graph = [[] for _ in range(int(input()) + 1)]

print(graph)

M, N = map(int, input().split())

for _ in range(int(input())):
    c, p = map(int, input().split())
    graph[c].append(p)


print(graph)
