import random
import time

def check_bigger(a, b):
    temp_a,temp_b = a,b
    if len(temp_a) > len(temp_b): temp_b += temp_b[-1]*(len(temp_a)-len(temp_b))
    elif len(temp_a) < len(temp_b): temp_a += temp_a[-1]*(len(temp_b)-len(temp_a))
    print(f'a={a}, b={b}, temp_a={temp_a}, temp_b={temp_b}')
    if temp_a >= temp_b: return a
    elif temp_a < temp_b: return b

def solution(numbers):
    if len(numbers) == 1: return str(numbers)
    str_numbers = list(map(str, numbers))
#   print(quick_sort(str_numbers)[::-1])
    return ''.join(quick_sort(str_numbers)[::-1])
def quick_sort(lst):
    if not lst: return []
    pivot = lst[0]
    lesser = quick_sort([x for x in lst[1:] if check_bigger(pivot, x) == pivot])
    grater = quick_sort([x for x in lst[1:] if check_bigger(pivot, x) == x])
    return lesser + [pivot] + grater






#numbers = [6,10,2]
#numbers = [3, 30, 34, 5, 9]
#numbers = ['45', '42', '41', '4', '36', '34', '2', '19', '14', '10', '11']
#numbers = [1,11,212,1,0,333,3,33,343]
numbers = [0,0,0,0,0]
print(solution(numbers))


#lst = []
#while len(lst) != 100000: lst.append(random.randint(0,1000))
#print(f'make lst complete!')
#start_time = time.time()
#print(f'start time = {start_time}')
#print(solution(lst))
#end_time = time.time()
#print(f'end time = {end_time}')
#print(f'inter time = {start_time-end_time}')
