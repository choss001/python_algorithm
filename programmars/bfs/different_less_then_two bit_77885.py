from collections import deque
def solution(numbers):
    #bit_to_number(number_to_bit(5))
    answer = []
    for number in numbers:
        ori_bit = number_to_bit(number)
        dif = 9999999
        while dif >2:
            number += 1
            bit = number_to_bit(number)
            print(f'bit={bit}, number={number}')
            dif = check_different_bit(ori_bit, bit)
        answer.append(number)    

    
    return answer
def check_different_bit(ori, after):
    dif = 0
    if len(ori) > len(after):
        while len(ori) != len(after): after.appendleft(0)
    elif len(ori) < len(after):
        while len(ori) != len(after): ori.appendleft(0)
    for i in range(len(ori)):
        if ori[i] != after[i]: dif+=1
    return dif

def number_to_bit(number):
    bit = deque()

    while number > 0:
        bit.appendleft(number % 2)
        number = number // 2
    return bit

def bit_to_number(bit):
    number = 0
    print(f'bit ={bit}')
    for i in range(len(bit)):
            if bit[i]:
                number += 2**(len(bit) -i -1)
    print(number)                
    return number

numbers = [2,7]
print(solution(numbers))
