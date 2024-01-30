import sys
input = sys.stdin.readline
from itertools import permutations

def solution(k, dungeons):
    base_lst = list(permutations([i for i in range(len(dungeons))],len(dungeons)))
    answer = 0
    for base in base_lst:
        temp_k = k
        temp_answer = 0
        print(f'base={base}')
        for i in base:
            print(f'temp_k={temp_k}, dungeons={dungeons[i]}, temp_answer={temp_answer}')temp_answer
            if temp_k >= dungeons[i][0]:
                temp_k -= dungeons[i][1]
                temp_answer += 1
            answer = max(answer, temp_answer)
            
            

    return answer

k, dungeons = 80,[[80,20],[50,40],[30,10]]
print(solution(k,dungeons))
