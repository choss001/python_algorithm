import sys
input = sys.stdin.readline

#def solution(n, info):
#    for i in range(11):
#        temp_n = n
#        for k in range(i,11):
#            if info[i]
#
#
#    return -1
#n, info = 5, [2,1,1,1,0,0,0,0,0,0,0]	
#solution(n,info)

def solution(size):
    def dfs(idx, lst,temp_lst):
        print(f'idx={idx}, size={size}')
        if idx == size-1:
            lst.append(temp_lst.copy())
            print(f'lst = {lst}')
            return lst
        for i in range(idx+1, size):
            temp_lst[idx] =1
            print(f'temp_lst = {temp_lst}')
            lst = dfs(i, lst, temp_lst.copy())
            temp_lst[idx] =0
            lst = dfs(i, lst, temp_lst.copy())
        return lst 
    temp_lst = [0] * size
    dfs(0,[], temp_lst)
    return -1
size = 3
print(solution(size))

