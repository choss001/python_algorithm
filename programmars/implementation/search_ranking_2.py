import sys
input = sys.stdin.readline
from collections import defaultdict
from itertools import combinations

def solution(info, query):
    element = [0,1,2,3]
    hash_dic = defaultdict(list)

    combi_lst = []
    for i in range(1,5):
        combi_lst.append(list(combinations(element, i)))

    for item in info:
        temp_item = item.split()[:4]
        hash_dic[''.join(temp_item)].append(int(item.split()[4]))

        for combi in combi_lst:
            for i in combi:
                temp_temp_item = temp_item.copy()
                for k in i:
                    temp_temp_item[k] = '-'
                hash_dic[''.join(temp_temp_item)].append(int(item.split()[4]))
    answer = []
    for i in query:
        temp_query = i.split(" and ")
        divide_temp = temp_query[3].split()
        temp_query[3] = divide_temp[0]
        temp_query.append(int(divide_temp[1]))
        score_lst = hash_dic[''.join(temp_query[:4])]
        score_lst.sort()
        print(f'score_lst={score_lst}')
        temp_answer = 0
        for k in range(len(score_lst)):
            if score_lst[k] >= temp_query[4]:
                answer.append(len(score_lst)-k)
                break

        



    return answer

info, query = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info,query))
