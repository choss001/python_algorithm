import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A_list = list(map(int, input().split()))


answer = 0
before, after = 0, 0
while before < N + 1 and after < N + 1:
    print(f'before = {before}, after = {after}, sum = \
            {sum(A_list[before:after])}')
    if sum(A_list[before:after]) == M :
        answer += 1
        before +=1
    elif sum(A_list[before:after]) < M :
        after += 1
    elif sum(A_list[before:after]) > M :
        before += 1

print(answer)
