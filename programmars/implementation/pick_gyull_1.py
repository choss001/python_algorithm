import collections
def solution(k, tangerine):
    answer = 0
    cnt = collections.Counter(tangerine)
    print(f'cnt={cnt}')

    for v in sorted(cnt.values(), reverse = True):
        print(f'v={v}')
        k -= v
        answer += 1
        if k <= 0:
            break
    return answer

k, tangerine = 6, [1,3,2,5,4,5,2,3]

print(solution(k,tangerine))
