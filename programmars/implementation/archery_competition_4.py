import sys 
input = sys.stdin.readline

diff = 0

def dfs(current, result, idx, n, info,current_sum, info_sum):
    global diff
    if n == 0 and diff <= current_sum - info_sum and current_sum - info_sum != 0:
        diff = current_sum - info_sum
        result.append((current.copy(), diff))
        return result
    print(f'current={current}, idx={idx}, n={n}, current_sum={current_sum}, info_sum={info_sum}, result={result}')
    for i in range(idx, 11):
        if n < info[i]+1 and i != 10:
            continue
        if n >= info[i] +1:
            n -= info[i] +1
            current[i] = info[i] + 1
        else:
            current[i] = n
            n = 0
        #n -= info[i] +1 if n >= info[i]+1 else n
        #current[i] = info[i] +1 if n >= info[i]+1 else n
        if info[i] !=0:
            info_sum -= 10-i
        current_sum += 10 -i
        dfs(current, result, i+1, n, info, current_sum, info_sum)
        n += current[i]
        current[i] = 0
        if info[i] !=0:
            info_sum += 10-i
        current_sum -= 10-i


    return result

def solution(n, info):
    info_sum = 0 
    for i in range(10):
        if info[i]:
            info_sum += 10-i

    result = dfs([0]*11, [], 0, n, info, 0, info_sum)
    result.sort(key=lambda x : (-x[1], x[0]))

    for item in result:
        print(item)
    return result[0][0] if result else [-1]

#n, info = 5, [2,1,1,1,0,0,0,0,0,0,0]
#n, info = 1, [1,0,0,0,0,0,0,0,0,0,0]
n, info = 9, [0,0,1,2,0,1,1,1,1,1,1]
#n, info = 10, [0,0,0,0,0,0,0,0,3,4,3]
#n, info = 1, [1,0,0,0,0,0,0,0,0,0,0]
print(f'solution = {solution(n, info)}')
