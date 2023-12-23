import sys
input = sys.stdin.readline

def solution(elements):
    length = len(elements)

    dic = {sum(elements) : 1}
    
    for i in range(1,length):
        start, end = 0, i
        temp_sum = sum(elements[0:i])
        if temp_sum not in dic:
            dic[temp_sum] = 1
        print(f'start={start},end={end}')
        print(f'temp_sum start = {temp_sum}')
        while start < length-1:
            print(f'start={start},end={end}')
            print(f'temp_sum = {temp_sum}, elements[start] = {elements[start]}\
                    elements[end] = {elements[end]}')
            temp_sum  = temp_sum -elements[start] + elements[end]
            print(f'temp result temp sum = {temp_sum}')
            start +=1
            end = 0 if end + 1 == length else (end := end + 1)
            if temp_sum not in dic:
                dic[temp_sum] = 1
    
        print(f'dic = {dic}')
        temp_list = list(dic.items())
        temp_list.sort()
    print(f'temp_list = {temp_list}')
    return len(dic)
elements = [7,9,1,1,4]

print(solution(elements))
