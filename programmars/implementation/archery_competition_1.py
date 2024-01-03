import sys
input = sys.stdin.readline

def dfs(m, idx, lst):
    nonlocal f

    if m == n:
        #print(f'lst={lst}')
        f.write(lst)
        return -1

    for k in range(idx, 11):
        lst[k] += 1
        dfs(m+1, idx, lst)
        lst[k] -= 1
    return -1

def solution(n, info):
    f = open("temp.txt", "a")
    dfs(0,0,[0]*11)
    f.close()

    return -1

#n, info = 9,[0,0,1,2,0,1,1,1,1,1,1] 
n, info = 5, [2,1,1,1,0,0,0,0,0,0,0]

print(solution(n,info))
