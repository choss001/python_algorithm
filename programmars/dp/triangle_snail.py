def solution(n):
    if n == 1:
        return [1]
    base_lst = [[0]*n for _ in range(n)]
    base_lst[0][0] = 1
    print(f'base_lst={base_lst}')
    end = 0
    if n%2 == 0: end = (n+1)*n//2
    else: end = ((n+1)*(n//2)) + (n//2+1)

    def dfs(n, start, base_lst, x, y, end):
        print(f'n, start,  x, y, end = {n, start, x, y, end}')
        for q in base_lst:
            print(q)
        if n == 1:
            y+=1
            base_lst[y][x] = end
            return
        for i in range(n-1):
            start += 1
            y+=1
            base_lst[y][x] = start
            if start == end: return
        for k in range(n-1):
            start +=1
            x += 1
            base_lst[y][x] = start
            if start == end: return
        for l in range(n-2):
            start +=1 
            x -= 1 
            y -= 1
            base_lst[y][x] = start
            if start == end: return
        for q in base_lst:
            print(q)
        print(f' end  !!! n, start,  x, y, end = {n, start, x, y, end}')
        if start != end-1:
            y +=1
            start +=1
            base_lst[y][x] = start
        dfs(n-3, start, base_lst, x, y, end)
    dfs(n,1,base_lst,0,0,end)
    print(f'base_lst={base_lst}')
    answer = []
    for i in range(len(base_lst)):
        for k in range(len(base_lst[0])):
            if base_lst[i][k] != 0:
                answer.append(base_lst[i][k])
    for q in base_lst:
        print(q)
    return answer

n=1
print(solution(n))

#dfs(size, start, base_lst, x, y, end):
#    for i in range(size-1):
#        start +=1
#        y += 1
#        base_lst[y][x] = start
#    for k in range(size-1):
#        start +1
#        x += 1
#        base_lst[y][x] = start
#    for l in range(size-2):
#        start +1
#        x -= 1 \y -= 1
#        base_lst[y][x] = start
#    if start == end:
#        return

    

#1
#2,  9
#3, 10,  8
#4,  5,  6,  7
#
#len (x) = 4
#len (y) = 4
#1,2,9,3,10,8,4,5,6,7


