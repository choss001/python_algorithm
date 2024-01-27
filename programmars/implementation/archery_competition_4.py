import sys 
input = sys.stdin.readline

diff = 0

def dfs(current, result, idx, n, info,current_sum, info_sum):
    global diff
    if n == 0 and diff <= current_sum - info_sum:
        diff = current_sum - info_sum
        result.append((current.copy(), diff))
        print(f'result !!current = {current}, current_sum = {current_sum}, info_sum={info_sum}, diff={diff}')
        return result

    for i in range(idx, 11):
        if n < info[i]+1:
            continue
        n -= info[i] +1
        current[i] = info[i] +1
        if info[i] !=0:
            info_sum -= 10-i
        current_sum += 10 -i
        print(f'current = {current} i={i}, info_sum={info_sum}, 10-i={10-i}, current_sum={current_sum}')
        dfs(current, result, i+1, n, info, current_sum, info_sum)
        n += info[i] +1
        current[i] = 0
        if info[i] !=0:
            info_sum += 10-i
        current_sum -= 10-i
        print(f'current = {current} i={i}, info_sum={info_sum}, 10+i={10-i} current_sum={current_sum}')


    return result

def solution(n, info):
    info_sum = 0 
    for i in range(10):
        if info[i]:
            info_sum += 10-i

    print(f'info_sum={info_sum}')
    result = dfs([0]*11, [], 0, n, info, 0, info_sum)
    for item in result:
        print(item)
    return 0

n, info = 5, [2,1,1,1,0,0,0,0,0,0,0]
print(f'solution = {solution(n, info)}')
