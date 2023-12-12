from collections import deque

visited = [-1] * 10000000
def bfs(x, y, n):
    q = deque()
    q.append((x, 0))
    while q :
        x, c = q.popleft()
        if x*3 ==y or x*2 ==y or x+n == y:
            return c+1
        if x*3 < y and visited[x*3] == -1:
            visited[x*3] = c+1
            q.append((x*3,c+1))
        if x*2 < y and visited[x*2] == -1:
            visited[x*2] = c+1
            q.append((x*2,c+1))
        if x+n < y and visited[x+n] == -1:
            visited[x+n] = c+1
            q.append((x+n,c+1))


    return -1


def solution(x,y,n):
    if x==y:
        return 0
    return bfs(x,y,n)




x, y, n = 10, 40, 30
#x, y, n = 2, 5, 4
print(solution(x,y,n))
