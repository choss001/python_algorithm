from collections import deque

#input_map = [
#    ['1','#','1','0','1','1','1'],
#    ['1','1','0','1','0','0','1'],
#    ['0','0','1','*','1','1','1'],
#    ['1','1','0','1','1','1','1'],
#    ['0','0','1','1','0','0','1'],
#]
#
#h, w = 5, 7
#ty1, tx1 = 3, 4
#ty2, tx2 = 1, 2




#h, w = 3, 5
#ty1, tx1 = 3, 5 
#ty2, tx2 = 1, 1
#input_map = [
#['#','0','0','0','0'],
#['1','1','1','1','1'],
#['0','0','0','0','*']
#]
h, w = map(int, input().split())
temp = list(map(int, input().split()))
ty1, tx1 = temp[0], temp[1]
ty2, tx2 = temp[2], temp[3]

input_map = [list(input().rstrip()) for _ in range(h)]


d = [[-1, 0],[0, 1],[1, 0],[0, -1]]
visited = [[False] * w for _ in range(h)]

y1, x1 = ty1 -1, tx1 -1
y2, x2 = ty2 -1, tx2 -1


q = deque([(y1, x1, 1)])
visited[y1][x1] = True

answer = 1e9

while(q):
    y, x, c = q.popleft()

    for i in d:
        dy, dx = y + i[0] , x + i[1]
        if 0 <= dy < h and 0 <= dx < w and not visited[dy][dx]:
            if input_map[dy][dx] == '1':
                q.append((dy, dx, c+1))
                visited[dy][dx] = True
            elif input_map[dy][dx] == '0':     
                q.appendleft((dy, dx, c))
                visited[dy][dx] = True
            else:
                answer = min(answer, c)

print(answer)
