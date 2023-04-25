import sys
from collections import deque

input = sys.stdin.readline

d = [[-1, 0], [0, -1], [1, 0], [0, 1]]

h, w = 5, 9
prison = [
['.','.','.','.','.','.','.','.','.','.','.'],
['.','*','*','*','*','#','*','*','*','*','.'],
['.','*','.','.','#','.','#','.','.','*','.'],
['.','*','*','*','*','.','*','*','*','*','.'],
['.','*','$','#','.','#','.','#','$','*','.'],
['.','*','*','*','*','*','*','*','*','*','.'],
['.','.','.','.','.','.','.','.','.','.','.'],
]

def BFS(y, x):
    q = deque()
    cnt = [[-1] * (w + 2) for _ in range(h + 2)]
    q.append([y, x])
    cnt[y][x] = 0

    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ty = y + dy
            tx = x + dx
            if 0 <= ty < h + 2 and 0 <= tx < w + 2:
                if cnt[ty][tx] == -1:
                    if prison[ty][tx] == '.':
                        q.appendleft([ty, tx])
                        cnt[ty][tx] = cnt[y][x]
                    elif prison[ty][tx] == '#':
                        q.append([ty, tx])
                        cnt[ty][tx] = cnt[y][x] + 1

    return cnt


start = []

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if prison[i][j] == '$':
            start.append([i, j])
            prison[i][j] = '.'
            

print(f'start = {start}')
print(f'start[0][0] = {start[0][0]}, start[0][1] = {start[0][1]}')
cnt1 = BFS(start[0][0], start[0][1])
for i in cnt1:
    for j in i:
        print(f'{j:3}', end='')
    print()
cnt2 = BFS(start[1][0], start[1][1])
print()

for i in cnt2:
    for j in i:
        print(f'{j:3}', end='')
    print()
cnt3 = BFS(0, 0)
print()
for i in cnt3:
    for j in i:
        print(f'{j:3}', end='')
    print()

ans = float('inf')
cnt4 = [[-2] * (w+2) for _ in range(h + 2)]
print()
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if cnt1[i][j] != -1 and cnt2[i][j] != -1 and cnt3[i][j] != -1:
            if prison[i][j] == '.':
                ans = min(ans, cnt1[i][j] + cnt2[i][j] + cnt3[i][j])
                cnt4[i][j] = cnt1[i][j] + cnt2[i][j] + cnt3[i][j]
            elif prison[i][j] == '#':
                ans = min(ans, cnt1[i][j] + cnt2[i][j] + cnt3[i][j] - 2)
                cnt4[i][j] = cnt1[i][j] + cnt2[i][j] + cnt3[i][j] -2

for i in cnt4:
    for j in i:
        print(f'{j:3}', end='')
    print()
print(ans)

