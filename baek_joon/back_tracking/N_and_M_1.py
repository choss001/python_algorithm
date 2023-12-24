<<<<<<< HEAD
import sys
input = sys.stdin.readline

def solution(m,n):

    def dfs(lst, temp):
        if len(temp) == n:
            lst.append(temp)
            return lst
        for i in range(1,m+1):
            if i not in temp:
                temp.append(i)
                lst = dfs(lst, temp.copy())
                temp.pop()
        return lst
    lst = dfs([],[])
    return lst

m, n = 4,3
print(solution(m,n))
=======
import sys
input = sys.stdin.readline
n,m = list(map(int,input().split()))

def solution(n,m):
    lst = backtracking(n, m, [], [])
    print(f'answer = {lst}')
    for i in lst:
        print(' '.join(map(str, i)))
    return -1
    
def backtracking(n, m, lst,temp):
    print(f'list={lst}, temp={temp}')
    if len(temp) == m:
        lst.append(temp.copy())
        return lst
    for i in range(1,n+1):
        if i not in temp:
            temp.append(i)
            lst = backtracking(n,m,lst,temp)
            temp.pop()

    return lst
    
solution(n,m)

#4,2, [], []
#1
#back(n,m,[],[1])
#back(n,m,[1,2],[1,2,3])
>>>>>>> f9a1ca5fa85a557127d97082ce9a708d70099889
