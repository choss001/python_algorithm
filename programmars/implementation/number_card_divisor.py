import sys
input =sys.stdin.readline
import math
from collections import Counter

def solution(arrayA,arrayB):
    answer = 0
    arrayA_dic = {}
    arrayB_dic = {}
    for i in arrayA:
        arrayA_dic = find_divisor(i, arrayA_dic)
    arrayA_list = list(arrayA_dic.items())
    arrayA_list.sort(key = lambda x:(-x[1], -x[0]))
    for i in arrayB:
        arrayB_dic = find_divisor(i, arrayB_dic)
    arrayB_list = list(arrayB_dic.items())
    arrayB_list.sort(key = lambda x:(-x[1], -x[0]))

    print(f'arrayA_dic={arrayA_dic}')
    print(f'arrayA_dic={arrayA_list[0][0]}')
    if arrayA_list[0][1] == len(arrayA):
        answer = max(answer, arrayA_list[0][0])
    if arrayB_list[0][1] == len(arrayB):
        answer = max(answer, arrayB_list[0][0])
    print(f'answer = {answer}')
    return answer

def find_divisor(number, dic):

    print(f'number={number}, int(math.sqrt(number))+1={int(math.sqrt(number))+1}')
    for i in range(1,int(math.sqrt(number))+1):
        print(f'i = {i}')
        if number % i == 0:
            if i not in dic: 
                dic[i] = 1
            else:
                dic[i] = dic[i] + 1
            if i != number//i:
                if number//i not in dic: 
                    dic[number//i] = 1
                else:
                    dic[number//i] = dic[number//i] + 1
    return dic
arrayA,arrayB=[10,17],[5,20]
solution(arrayA,arrayB)
