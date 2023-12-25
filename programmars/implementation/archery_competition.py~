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
    def dfs(idx, lst):
        if idx == size:
            return lst
        for i in range(idx+1, size):
            lst[idx] =1
            print(f'lst = {lst}')
            lst = dfs(i, lst)
            lst[idx] =0
            print(f'lst = {lst}')
            lst = dfs(i, lst)
        return lst 
    lst = [0] * size
    dfs(0,lst)
    return -1
size = 3
print(solution(size))

