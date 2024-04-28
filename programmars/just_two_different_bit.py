from itertools import combinations
from collections import deque

def solution(numbers):
    answer = []
    for number in numbers:
        bit = make_bit(number)
        two_diff = list(combinations([i for i in range(len(bit))],2))
        one_diff = list(combinations([i for i in range(len(bit))],1))
        print(f'bit = {bit}')
        print(f'two_diff={two_diff}, one_diff={one_diff}')
#   print(make_bit(3))
#   print(make_number([1,1]))
#   print(pow(2,2))
    return 0

def make_bit(number):
    q = deque()
    while number >0 :
        q.appendleft(number % 2)
        number = number // 2
    return q

def make_number(q):
    number = 0
    for i in range(len(q)-1, -1 ,-1):
        if q[i]: number += pow(2,i)
    return number

def temp_answer(q, diffs):
    change_dic = {1:0, 0:1}
    for diff in diffs:
        c_p = q.copy()
        c_p = change_dic[c_p[diffs[0]]]


numbers = [2,7]

solution(numbers)
