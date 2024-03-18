import random
import time


def solution(numbers):
    answer = ''
    numbers = [str(i) for i in numbers]
    print(f'numbers = {numbers}')
    def sort_key_method(x):
        print(f'x*3 = {x*3}')
        return x*3
#    numbers.sort(key = lambda x: x*3, reverse = True)
   # numbers.sort(key = sort_key_method)
    numbers.sort(reverse=True)
    answer = str(int(''.join(numbers)))
    return answer




#numbers = [6,10,2]
#numbers = [3, 30, 34, 5, 9]
numbers = ['45', '42', '41', '4', '36', '34', '2', '19', '14', '10', '11']

#numbers = [1,11,212,1,0,333,3,33,343]
#numbers = [0,0,0,0,0]
print(solution(numbers))
