import sys
input = sys.stdin.readline
from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(infos, query):
    answer = []
    dic = defaultdict(list)
    
    for info in infos:
        info = info.split()
        condition = info[:-1]  
        score = int(info[-1])
        print(f'info={info}, condition = {condition}, score={score}')
        for i in range(5):

            case = list(combinations([0,1,2,3], i))   
            print(f'case = {case}, i= {i}')
            for c in case:
                print(f'c = {c}')
                tmp = condition.copy()
                for idx in c:
                    tmp[idx] = "-"
                key = ''.join(tmp)
                dic[key].append(score) 

    for value in dic.values():
        value.sort()
    print(f'dic = {dic}')

    return 0

info, query = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"] 

print(solution(info,query))
