import sys
input = sys.stdin.readline
from collections import defaultdict
from itertools import combinations


def solution(info,query):
    base_dic = defaultdict(list)
    base_lst = [0,1,2,3]

    for item in info:

        temp_item = item.split()
        condition = temp_item[:4]
        score = int(temp_item[-1])
        
        base_dic[''.join(condition)].append(score)
        base_dic['----'].append(score)
        for i in range(1,5):
            temp_combination = list(combinations(base_lst,i))
            for k in temp_combination:
                for j in k:
                    print(f'j = {j}')
            temp_condition = condition.copy()
            temp_condition[i] = '-'
            print(f"temp_condition={''.join(temp_condition)}")
            base_dic[''.join(temp_condition)].append(score)
    print(f'base_dic = {base_dic}')
    
    answer = []
    
    for item in query:
        item = item.split(' and ')
        query_last = item[3].split()
        item[3] = query_last[0]
        item.append(query_last[1])
        print(f'item = {item}')
        print(f"base = {''.join(item[:4])}")
        print(f'result = {base_dic["".join(item[:4])]}')
        score_lst = base_dic[''.join(item[:4])]
        score_lst.sort()
        print(f'sort socre_lst = {score_lst}')
        for i in range(len(score_lst)):
            if score_lst[i] >= int(item[4]):
                print(f'socre_lst={score_lst}, item[4]={item[4]}')
                answer.append(len(score_lst)-i)
                break
    return answer

info, query= ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))
