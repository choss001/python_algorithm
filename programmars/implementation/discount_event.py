import sys
input = sys.stdin.readline

def solution(want, number, discount):
    dic_solution ={}
    dic_target = sum_discount(discount)

    for i in range(len(want)):
        dic_solution[want[i]] = number[i]
    check_dic = make_check_dic(dic_solution)
    print(f'number')
    print(f'dic_solution={dic_solution.items()}')
    print(f'dic_target ={dic_target}')
    print(f'check_dic={check_dic}')
    result = []

    start, end = 0, 10
    while True:
        dic_want = dic_solution.copy()
        check_flag = check_all_true(check_true(dic_target, dic_want, check_dic))
        print(f'check_flag = {check_flag}')
        print(f'dic_want={dic_want.items()}')
        print(f'dic_target ={dic_target}')
        if check_flag:
            result.append(start)
        start += 1
        end += 1
        dic_target[discount[start]] -= 1
        if len(discount) <= end :
            break
        if discount[end] not in dic_target:
            dic_target[discount[end]] = 1
        else:
            dic_target[discount[end]] = dic_target[discount[end]] + 1
            
    print(f'result={result}')

    return 0
def sum_discount(discount):
    dic_target = {}
    for i in range(10):
        if discount[i] not in dic_target:
            dic_target[discount[i]] = 1
        else:
            dic_target[discount[i]] = dic_target[discount[i]] + 1
    return dic_target
def check_true(dic_target, dic_want, check_dic):
    for k,v in dic_target.items():
        if k in dic_want:
            dic_want[k] -= 1
            if dic_want[k] <= 0:
                check_dic[k] = True
    return check_dic
def check_all_true(check_dic):
    for k,v in check_dic.items():
        if v == False:
            return False
    return True
def make_check_dic(dic_solution):
    dic = {}
    for k,v in dic_solution.items():
        dic[k] = False
    return dic

want, number, discount = ["banana", "apple", "rice", "pork", "pot"],\
[3, 2, 2, 2, 1],\
["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
solution(want, number, discount)
