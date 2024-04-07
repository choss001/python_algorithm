import sys
input = sys.stdin.readline
from collections import deque

def solution(queue1,queue2):
    
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    q1 = deque(queue1)
    q2 = deque(queue2)
    answer = 0 
    while q1_sum != q2_sum:
        answer += 1
        if q1_sum > q2_sum:
            q1_temp = q1.popleft()
            q2.append(q1_temp)
            q1_sum -= q1_temp
            q2_sum += q1_temp
        elif q1_sum < q2_sum:
            q2_temp = q2.popleft()
            q1.append(q2_temp)
            q1_sum += q2_temp
            q2_sum -= q2_temp
        print(f'q1 ={q1}, q2={q2}')
        if answer > len(q1)+len(q2):
            return -1
    
    return answer if answer != 0 else 1

#q1, q2 = [3, 2, 7, 2], [4, 6, 5, 1]
#q1,q2 = [1,2,1,2], [1,10,1,2]
#q1,q2 = [1,1], [1,5]
q1,q2 = [1], [1]

print(f'solution = {solution(q1,q2)}')
