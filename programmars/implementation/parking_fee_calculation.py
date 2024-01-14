import sys
import math
input = sys.stdin.readline 
def solution(fees, records):
    dic = {}
    dic_sort_car_num = []
    result_dic = {}
    answer = []
    for item in records:
        temp_record = item.split(' ')
        if temp_record[1] not in dic:
            dic[temp_record[1]] = [(temp_record[0], temp_record[2])]
            dic_sort_car_num.append(temp_record[1])
        else:
            dic[temp_record[1]].append((temp_record[0], temp_record[2]))
    dic_sort_car_num.sort()
    print(f'temp = {dic_sort_car_num}')
    for k,v in dic.items():
        print(f'k={k}   ',end='')
        result = math.ceil((calculate_fee(v)-fees[0])/fees[2])*fees[3] + fees[1]
        print(f'calulate_fee ={calculate_fee(v)}')
        result = result if result > fees[1] else fees[1]
        result_dic[k] = result
        print( result if result > fees[1] else fees[1])
    for i in dic_sort_car_num:
        answer.append(result_dic[i])
    return answer
def minus_time(before, after):
    after = list(map(int, after.split(':')))
    before = list(map(int, before.split(':')))
    print(f'after = {after}, before={before}')
    if after[1] < before[1]:
        return (after[0]-before[0]-1)*60+(after[1]-before[1]+60)
    else:
        return (after[0]-before[0])*60 + (after[1]-before[1])

def calculate_fee(lst):
    lst.sort()
    if len(lst) % 2  == 1:
        lst.append(('23:59', 'OUT'))
    print(f'lst ={lst}')
    temp = 0
    for i in range(0, len(lst), 2):
        temp += minus_time(lst[i][0], lst[i+1][0])
    return temp


#fees, records = [180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

#fees, records = [120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]

fees, records = [1, 461, 1, 10],["00:00 1234 IN"]
print(solution(fees, records))
