import heapq
def solution(jobs): 
    answer, now, i = 0, 0, 0
    start = -1
    heap = []
    
    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업들 저장
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, (j[1], j[0]))
        print(f'heapq = {heap}')
        if heap:
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1]
            i += 1
            print(f'cur={cur}, start={start}, now={now}, answer={answer}\
, i={i}')
        else:
            print(f'else now={now}')
            now += 1
    return answer // i
jobs =[[0, 3], [1, 9], [2, 6]] 
print(solution(jobs))
