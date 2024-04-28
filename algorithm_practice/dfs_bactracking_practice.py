import sys
input = sys.stdin.readline


def solution(n,m):
    def dfs(current, elements, result, size, idx):
        if idx == size:
            print(current)
            result.append(current.copy())
            return

        for i in elements:
            current.append(i)
            dfs(current, elements, result, size, idx+1)
            current.pop()


        return -1
    result = []
    dfs([],m,result,n,0)
    print(f'result = {result}')
    return -1

n, m = 4, ['A','B','C']

solution(n,m)
