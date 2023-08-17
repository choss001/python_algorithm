import heapq

def solution(scoville, k):
    heapq.heapify(scoville)
    
    answer = 0
    while scoville[0] < k and len(scoville) >= 2:
        answer += 1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + (b * 2))
         
    return -1 if scoville[0] < k else answer

scoville =[1, 2,3, 9, 10, 12]
k = 7
print(solution(scoville, k))
