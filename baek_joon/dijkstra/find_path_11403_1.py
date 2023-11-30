from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

def bfs(x):
    queue = deque()
    queue.append(x)
    check = [0 for _ in range(n)]
    for i in range(n):
        print(visited[i])

    while queue:
        q = queue.popleft()
        print(f'q={q}, x={x}')

        for i in range(n):
            print(f'check[{i}]={check[i]},graph[{q}][{i}]={graph[q][i]},i={i}')
            if check[i] == 0 and graph[q][i] == 1:
                print(f'true')
                queue.append(i)
                check[i] = 1
                visited[x][i] = 1

for i in range(0, n):
    bfs(i)

for i in visited:
    print(*i)

