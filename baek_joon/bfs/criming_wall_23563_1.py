import sys; input = sys.stdin.readline
from math import inf
from collections import deque
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우

H, W = map(int, input().split())
matrix = [input().strip() for _ in range(H)]

w = [[1] * W for _ in range(H)] # 0 : 벽에 인접한 빈칸, 1 : 벽에 인접하지 않은 빈칸, 2 : 벽
for i in range(H):
    for j in range(W):
        if matrix[i][j] == '#': # 벽
            w[i][j] = 2
            continue
        if matrix[i][j] == 'S': # 시작점
            si = i; sj = j
        elif matrix[i][j] == 'E': # 끝점
            ei = i; ej = j
        for di, dj in dir: # 벽에 인접한 지 확인
            if 0 <= i + di < H and 0 <= j + dj < W and matrix[i + di][j + dj] == '#':
                w[i][j] = 0
                break
for i in range(H):
    print(f'{w[i]}')
# 시작점부터 0-1 BFS 시작
dq = deque([(0, si, sj)]) # 거리, 행 번호, 열 번호
distance = [[inf] * W for _ in range(H)]
distance[si][sj] = 0

while dq:
    d, i, j = dq.popleft()
    if distance[i][j] < d:
        continue
    for di, dj in dir:
        if 0 <= i + di < H and 0 <= j + dj < W:
            if not w[i][j] and not w[i + di][j + dj]: # 벽에 인접한 빈칸 -> 벽에 인접한 빈칸 (가중치 0)
                if distance[i + di][j + dj] > d:
                    distance[i + di][j + dj] = d
                    dq.appendleft((d, i + di, j + dj)) # deque 앞에 넣기
            elif w[i + di][j + dj] != 2: # 벽으로 이동하는 경우를 제외한 나머지 (가중치 1)
                if distance[i + di][j + dj] > d + 1:
                    distance[i + di][j + dj] = d + 1
                    dq.append((d + 1, i + di, j + dj)) # deque 뒤에 넣기
for i in range(H):
    print(f'{distance[i]}')
print(distance[ei][ej])
