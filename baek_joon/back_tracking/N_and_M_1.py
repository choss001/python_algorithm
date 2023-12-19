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
