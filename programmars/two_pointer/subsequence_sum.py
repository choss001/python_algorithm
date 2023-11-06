import sys

answer =[0,sys.maxsize]
def solution(sequence,k):
    s,e = 0,0
    temp_sum = sum(sequence[s:e+1])
    while e < len(sequence):
        if temp_sum < k:
            e += 1
            if e >= len(sequence):
                break
            temp_sum += sequence[e]
        elif temp_sum > k:
            temp_sum -= sequence[s]
            s += 1
        else:
            if answer[1]-answer[0] > e-s:
                answer[0] = s
                answer[1] = e
            if e+1 >= len(sequence) or s+1 >= len(sequence):
                break
            temp_sum = temp_sum - sequence[s] + sequence[e+1] 
            e += 1
            s += 1
    return answer
sequence = [1, 1, 1, 2, 3, 4, 5]
k = 5
print(solution(sequence,k))

