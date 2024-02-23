def solution(places):
    result = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def f(i, j, cnt):
        print(f'i={i}, j={j}, cnt={cnt}')
        nonlocal good
        if cnt >2 : return
        if -1<i<5 and -1<j<5:
            print(f'graph[i][j] = {graph[i][j]}')
            if graph[i][j] == 'X': return

            if cnt != 0 and graph[i][j] == 'P':
                good = 0
                return

            graph[i][j] = 'X'

            for z in graph:
                print(z)

            for w in range(4):
                ni = i+dx[w]
                nj = j+dy[w]
                print(f'ni={ni}, nj={nj}')
                f(ni, nj, cnt+1)

    for case in places:
        graph = [list(r) for r in case]
        good = 1
        for i in graph:
            print(i)
        for i in range(5):
            for j in range(5):
                if graph[i][j]=='P':
                    print(f'start = {i}, {j}')
                    f(i,j,0)

        result.append(good)
    return result

places = [["POOOP",
            "OXXOX",
            "OPXPX",
            "PXXOX",
            "OOXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))
