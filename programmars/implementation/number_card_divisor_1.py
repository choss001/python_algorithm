import sys
input =sys.stdin.readline
import math
from collections import Counter
from collections import deque

def solution(arrayA,arrayB):
    print(f'find_divisor(arrayA)={find_divisor(arrayA)}')
    print(f'find_divisor(arrayB)={find_divisor(arrayB)}')

    arrayA_divisor = find_divisor(arrayA) if len(arrayA)!=1 else arrayA[0]
    arrayB_divisor = find_divisor(arrayB) if len(arrayB)!=1 else arrayB[0]
    checkA = check_can_divide(arrayB_divisor, arrayA)
    checkB = check_can_divide(arrayA_divisor, arrayB)
    print(f'checkA={checkA}, checkB={checkB}')

    if checkA ==True and checkB == False:
        return arrayA_divisor
    elif checkA ==False and checkB == True:
        return arrayB_divisor
    elif checkA == False and checkB == False:
        return max(arrayB_divisor, arrayA_divisor)
    elif checkA == True and checkB == True:
        return 0
            
def find_divisor(array):
    q = deque(array)
    cal_array = deque([q.popleft(), q.popleft()])
    while True:
        big = max(cal_array[0], cal_array[1])
        small = min(cal_array[0], cal_array[1])
        print(f'cal_array1={cal_array}')
        cal_array.pop()
        cal_array.pop()
        while small !=1 or big != 1 or samll != 0 or big != 0:
            if big % small == 0:
                cal_array.append(small)
                print(f'cal_array2={cal_array}')
                break
            temp = big
            big = small
            small = temp%small
            print(f'small = {small}, big={big}')
        if q :
            cal_array.append(q.popleft())
        else:
            break
    print(f'cal_array3={cal_array}')

    return cal_array[0]
def check_can_divide(divisor, array):
    for item in array:
        if item % divisor == 0:
            return True
    return False
#arrayA,arrayB=[10,20],[5,17]
#arrayA,arrayB =[14, 35, 119],[18,30,102]
arrayA,arrayB =[20,40,10],[3,17]
print(solution(arrayA,arrayB))
