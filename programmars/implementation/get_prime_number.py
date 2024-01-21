import sys
input = sys.stdin.readline
from collections import deque
import math

def get_convert_number(n, k):
    q = deque()
    reminder, quotient = 0,0
    while n >= k:
        reminder = n % k
        quotient = n // k
        q.appendleft(reminder)
        n = quotient
    q.appendleft(n)
    temp = ''.join(map(str,q))
    return temp

def is_prime():
    lst_hash = [1]+[1]+[0]*33333333
    k = 2
    while 33333335 > k:
        if lst_hash[k] == 1:
            k+=1
            continue
        for i in range(k *2, 33333335, k):
            lst_hash[i] = 1
        k += 1

    #return True if lst_hash[number] == 0 else False
    return lst_hash

def is_prime2(value):
    k = 2
    if value == 1:
        return False
    for i in range(2,int(math.sqrt(value))+1):
        if value % i == 0:
            return False

    return True

def solution(n, k):
    temp_value = get_convert_number(n, k)
    print(f'temp_value = {temp_value}')
    print(temp_value.split('0'))
    answer = 0
    for i in temp_value.split('0'):
        if i == '':
            continue
        i = int(i)
        print(f'i = {i}, is_prime = {is_prime2(i)}')
        if is_prime2(i) == True:
            answer+=1
        
    

    return answer

n,k = 437674,3

print(solution(n, k))

