import sys
input = sys.stdin.readline
from collections import deque

def solution(topping):
    answer = 0

    a = {topping[0]:1}
    b = {}
    for i in range(1,len(topping)):
        if topping[i] not in b:
            b[topping[i]] = 1
        else:
            b[topping[i]] = b[topping[i]] + 1

    if len(a) == len(b):
        answer += 1
    for i in range(1,len(topping)-1):
        if topping[i] not in a:
            a[topping[i]] = 1
        else:
            a[topping[i]] = a[topping[i]] + 1

        b[topping[i]] = b[topping[i]] - 1
        if b[topping[i]] == 0 :
            del b[topping[i]]

        if len(a) == len(b):
            answer += 1
        

    return answer


topping = [1, 2, 1, 3, 1, 4, 1, 2]
print(f'solution={solution(topping)}')
