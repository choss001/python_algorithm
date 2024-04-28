from itertools import permutations

def solution(numbers):
    answer = 0 
    permu = list(permutations(numbers,len(numbers)))
    for i in range(len(permu)):
        temp = ''
        for j in permu[i]:
            temp = temp+str(j)
        answer = max(answer, int(temp))

    

    return str(answer)

numbers = [6,10,2]

print(solution(numbers))
