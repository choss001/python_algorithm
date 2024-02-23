from itertools import permutations

def solution(numbers):
    answer = ""
    temp = list(map(str, numbers))
    print(f'before sort = {temp}')
    bubble_sort(temp)
    print(temp)
    return ''.join(temp)

def bubble_sort(numbers):
    str_numbers = list(map(str,numbers))
    for i in range(len(numbers)-1):
        for j in range(0, len(numbers)-1-i):
            bigger_value = check_bigger(numbers[j], numbers[j+1])
            print(f'j = {j}, bigger_value={bigger_value}, numbers[j]={numbers[j]}, numbers[j+1]={numbers[j+1]}')
            if bigger_value != numbers[j]:
                numbers[j+1] = numbers[j]
                numbers[j] = bigger_value
            print(f'after numbers = {numbers}')


             

def check_bigger(a, b):
    temp_a,temp_b = a,b
    if len(temp_a) > len(temp_b): temp_b += temp_b[-1]*(len(temp_a)-len(temp_b))
    elif len(temp_a) < len(temp_b): temp_a += temp_a[-1]*(len(temp_b)-len(temp_a))
    for i in range(len(temp_a)):
        if temp_a[i] > temp_b[i]: return a
        elif temp_a[i] < temp_b[i]: return b
    return a

#numbers = [6,10,2]
numbers = [3, 30, 34, 5, 9]
print(solution(numbers))


334
33

334
3

333
3

332
3




33, 30
3, 30
41 ,30
31, 3
32, 3
33, 3
30, 3
3, 5, 9, 30
9, 5, 3, 30
21
9 ,5, 3, 31, 21
9, 5, 3, 32, 21
9, 5, 3, 33, 21
9, 5, 33, 334
