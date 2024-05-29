import sys
input = sys.stdin.readline
from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def binary_search(lst, target, start, end, temp):

    if start > end:
        return temp
    mid = (start+end) // 2
#   if lst[mid] >= target:
#       end = mid -1 
#       temp = mid
#   else:
#       start = mid +1
    if lst[mid] <= target:
        start = mid +1 
        temp = mid
    else:
        end = mid -1
    return binary_search(lst, target, start, end, temp)

def solution(info, query):
    element = [0,1,2,3]
    base_dic = defaultdict(list)

    base_combi_elements = []

    for i in range(1,5):
        for k in combinations(element,i):
            base_combi_elements.append(k)

    for info_item in info:
        conditions = info_item.split()[:4]
        score = int(info_item.split()[4])
        base_dic[''.join(conditions)].append(score)
        for base_combi in base_combi_elements:
            temp_condi = conditions.copy()
            for base in base_combi:
                temp_condi[base] = '-'
            base_dic[''.join(temp_condi)].append(score)
    for value in base_dic.values():
        value.sort()

    answer = []
    for i in query:
        i = i.replace("and ", "")
        i = i.split()
        condition = ''.join(i[:4])
        score = i[4]
        score_lst = base_dic[condition]

#       idx = binary_search(score_lst, int(score), 0, len(score_lst))
#       answer.append(len(score_lst)-idx)
    test = [1,1,1,1,1,2,3,4,5,55,5,5,5,5,5,5,5,5555, 356]
    test.sort()
    print(f'test={test}')
    result = binary_search(test, 5, 0, len(test)-1, -1)
    print(f'test = {result}')
    return answer


info, query = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"] 

print(solution(info,query))
