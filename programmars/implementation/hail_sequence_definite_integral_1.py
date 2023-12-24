import sys
input = sys.stdin.readline

def getUbak(k):
    result = []
    while k != 1:
        result.append(k)
        # 결과가 소수이므로 / 연산
        k = k / 2 if k % 2 == 0 else k * 3 + 1 
    result.append(k)
    print(f'result={result}')
    return result
 
def solution(k, ranges):
    answer = []
    print(f'k = {k}')
    ubak = getUbak(k)
 
    for r in ranges:
        total = 0
        ubakRange = ubak[r[0] : len(ubak)+r[1]]
        print(f'ubakRange={ubakRange}, ubak={ubak}')
        
        # 주어진 구간의 시작점이 끝점보다 커서 유효하지 않은 구간
        if r[0] >= r[1] + len(ubak):
            answer.append(-1)
            continue
            
        for i in range(len(ubakRange) - 1):
            # 사다리꼴 넓이 구하는 공식 : ((윗변+아랫변) * 높이) / 2
            total += (((ubakRange[i] + ubakRange[i+1]) * 1) / 2)
        answer.append(total)
        
    return answer
k,ranges = 5, [[0,0],[0,-1],[2,-3],[3,-3]]
print(solution(k,ranges))

#[[0, 5], [1, 16], [2, 8], [3, 4], [4, 2], [5, 1]]
#[10.5, 12.0, 6.0, 3.0, 1.5]
#[[0,0],[0,-1],[2,-3],[3,-3]]
#[33.0,31.5,0.0,-1.0]
#0,0 전체

#0, -1 => sum(0~6)
#0, -2 => sum(0~5)
#0, -3 => sum(0~4)
#array_dot[s][0], 




