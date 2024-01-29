import sys
input = sys.stdin.readline


def dfs(current, result, count, info, idx):

    if count == 0 :
        result.append(current.copy())
        return result


    for i in range(idx, 11):
        if count < info[i] + 1:
            continue
        count -= info[i] + 1
        current[i] = info[i] + 1
        dfs(current, result, count, info, i+1)
        count += info[i] + 1
        current[i] = 0

    return result

def solution(n, info):
    result = dfs([0]*11, [], n, info, 0)
    print(f'result = {result}')
    return -1

#n, info = 9,[0,0,1,2,0,1,1,1,1,1,1] 
n, info = 5, [2,1,1,1,0,0,0,0,0,0,0]

print(solution(n,info))
