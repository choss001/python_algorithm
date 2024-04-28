def solution(places):
    move = [(-1,0),(0,1),(1,0),(0,-1)]

    def dfs(y, x, cnt, place,visited):
        if cnt > 2: return True
        visited[y][x] = True
        if cnt != 0 and place[y][x] == 'P': return False
        if place[y][x] == 'X': return True

        for m in move:
            dy=y+m[0]
            dx=x+m[1]
            if not (-1<dy<5 and -1<dx<5) or visited[dy][dx] == True: continue
            if not dfs(dy, dx, cnt+1, place, visited): return False

        return True
    answer = []
    for place in places:
        flag = True
        for i in range(5):
            if not flag: break
            for k in range(5):
                visited = [[False for _ in range(5)] for _ in range(5)]
                if place[i][k] == 'P' and dfs(i,k,0,place,visited) == False:
                    answer.append(0)
                    flag = False
                    break
        if flag: answer.append(1)
    return answer

#places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

places = [["POOOP",
            "OXXOX",
            "OPXPX",
            "PXXOX",
            "OOXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]


print(solution(places))
