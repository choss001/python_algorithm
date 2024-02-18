from itertools import permutations

def solution(numbers):
    answer_lst = []
    for item in permutations(numbers):
        temp = ''.join(map(str,item))
        answer_lst.append(temp)
        answer_lst.sort(reverse=True)
    return answer_lst[0]


#numbers = [6,10,2]
numbers = [3, 30, 34, 5, 9]
print(solution(numbers))
