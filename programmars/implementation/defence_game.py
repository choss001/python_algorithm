from heapq import heappush, heappop

def solution(n, k, enemy):
    stage = len(enemy)
    if k >= stage :
        return stage
    q = []
    
    for i in range(stage) :
        heappush(q, enemy[i])
        print(f'q = {q}')
        if len(q) > k :
            last = heappop(q)
            print(f'last={last}, n ={n}, i ={i}')
            if last > n :
                return i
            n -= last
        
    return stage
n, k, enemy = 7, 3, [4, 2, 4, 5, 3, 3, 1]
print(solution(n,k,enemy))
