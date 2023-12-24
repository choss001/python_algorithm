import sys
input = sys.stdin.readline

def solution(n, info):
    temp_answer_lst = [-1] * 11
    for i in range(11):
        start = i
        temp_n = n
        for k in range(i,11):
            print(f'start={start}, k={k}, n={n}, info[{k}] = {info[k]}')
            if info[k] > temp_n:
                print(f'i dont know what do to yet')
                break
            elif info[k] == temp_n:
                print(f'equal info[{k}] == {n}')
                break
            else:
                temp_answer_lst[start] += abs(10-k)
                temp_n -= info[k]
        print(f'temp_answer_lst = {temp_answer_lst}')
    return -1

n, info = 5,[2,1,1,1,0,0,0,0,0,0,0] 
print(solution(n, info))
