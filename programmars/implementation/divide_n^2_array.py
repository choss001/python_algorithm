import sys
from collections import deque

def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        answer.append(i//n+1) if i//n >= (i%n)+1 else answer.append(i%n+1)
    return answer

n, left, right = 4, 7, 14
print(solution(n, left, right))
