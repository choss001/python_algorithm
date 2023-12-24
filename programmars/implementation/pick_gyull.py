import sys
input = sys.stdin.readline

def solution(k, tangerine):
    list = [0] * 10000001
    answer = 0
    for i in tangerine:
        list[i] = list[i] + 1

    list.sort(reverse=True)
    i = 0
    while k > 0:
        k -= list[i]

        i+=1
        answer += 1
        if list[i]==0:
            break

    return answer
#k, tangerine = 6, [1,3,2,5,4,5,2,3]
k, tangerine = 4, [1]


print(solution(k,tangerine))
