import sys
input = sys.stdin.readline

def dfs(current, result,  n, m):
    if len(current) == m:
        result.append(current.copy())
        return result

    for i in range(1,n+1):
        if i in current:
            continue
        current.append(i)
        dfs(current, result, n, m)
        current.pop()

        
    return result

def solution(k, dungeons):
    result = dfs([],[],len(dungeons), 3)
    print(f'result ={result}')
    
    return



k, dungeons = 80,[[80,20],[50,40],[30,10]]
print(solution(k,dungeons))

