import sys 
input = sys.stdin.readline

diff = 0

def dfs(current, result, idx, n, info,current_sum, info_sum):
    global diff
    if n == 0:
        print(f'result !! || {current}, diff = {current_sum - info_sum}, current_sum = {current_sum}, info_sum ={info_sum}')
    if n == 0 and diff <= current_sum - info_sum and current_sum - info_sum != 0:
        diff = current_sum - info_sum
        result.append((current.copy(), diff))
        return result
    for i in range(idx, 11):
        if n < info[i]+1 and i != 10:
            #print(f'info[i]+1 and i != 0   ||||  current={current}, idx={idx}, n={n}, current_sum={current_sum}, info_sum={info_sum}, result={result}')
            continue
        if n >= info[i] +1:
            n -= info[i] +1
            current[i] = info[i] + 1
        else:
            current[i] = n
            n = 0
        if info[i] !=0:
            info_sum -= 10-i
        current_sum += 10 -i
        #print(f'current={current}, idx={idx}, n={n}, current_sum={current_sum}, info_sum={info_sum}, result={result}')
        dfs(current, result, i+1, n, info, current_sum, info_sum)
        n += current[i]
        current[i] = 0
        if info[i] !=0:
            info_sum += 10-i
        current_sum -= 10-i


    return result

def checker(result):
    temp_high_score = 0
    if result:
        print(f'result = {result}')
        temp_high_score = result[0][1]

        temp_a = [[0]*11,0]
        print(f'temp_a[0] = {temp_a[0]}')
        temp_result = []
        print(f'temp_high_score = {temp_high_score}')
    
        for item in result:
            if item[1] < temp_high_score:
                continue
            item = item[0]
            print(f'item = {item}')
            for i in range(10, -1, -1):
                print(f'item[i] = {item[i]}, temp_a[0][i] = {temp_a[0][i]} ')
                if item[i] == 0 and temp_a[0][i] == 0:
                    continue
                if item[i] > temp_a[0][i]:
                    temp_result = item
                    temp_a = (item,i)
                break
        result = temp_result

    return result

def solution(n, info):
    info_sum = 0 
    for i in range(10):
        if info[i]:
            info_sum += 10-i

    result = dfs([0]*11, [], 0, n, info, 0, info_sum)
    if not result:
        return [-1]

    result.sort(key=lambda x : (-x[1], x[0]))

    #result = checker(result)
    return checker(result)
    #return result[0][0] if result else [-1]

#n, info = 5, [2,1,1,1,0,0,0,0,0,0,0]
#n, info = 1, [1,0,0,0,0,0,0,0,0,0,0]
n, info = 9, [0,0,1,2,0,1,1,1,1,1,1]
#n, info = 10, [0,0,0,0,0,0,0,0,3,4,3]
#n, info = 1, [1,0,0,0,0,0,0,0,0,0,0]
#n, info = 11, [1,1,1,1,1,1,1,1,1,1,1]

print(f'solution = {solution(n, info)}')
