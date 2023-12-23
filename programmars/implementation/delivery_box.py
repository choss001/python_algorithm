import sys
input = sys.stdin.readline
from collections import deque

def solution(order):
    base_q = deque([i for i in range(1,len(order)+1)])
    support_q = []

    answer = 0
    for item in order:
        if not base_q and not support_q:
            break
        if base_q and base_q[0] == item:
            base_q.popleft()
            answer += 1
            continue
        if support_q and support_q[len(support_q)-1] == item:
            support_q.pop()
            answer += 1
            continue
        flag = False
        while base_q:
            if item == base_q[0]:
                base_q.popleft()
                answer += 1
                flag = True
                break
            else:
                support_q.append(base_q.popleft())
        if not flag:
            break
    return answer

order = [4,3,1,2,5]
#order = [5,4,3,2,1]
#order = [3,2,1,5,4]
#order = [1,2,3,4,5]
#order = [1,2,3,5,4]
#order =[1]

print(solution(order))
