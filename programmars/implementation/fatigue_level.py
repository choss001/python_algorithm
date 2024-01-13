import sys
input = sys.stdin.readline


def make_combination(length, current, result, elements):

    if length == 0:
        print(f'current = {current}')
        result.append(current.copy())
        return result

    for i in range(elements):
        if i in current:
            continue
        current.append(i)
        make_combination(length-1, current, result,elements)
        current.pop()

    return result

def solution(k, dungeons):
    length = len(dungeons)
    result = []
    print(make_combination(length, [], result,length))
    

    answer = 0
    for i in result:
        temp_answer = 0
        u = k
        for ini, need in i :
            if u < ini:
                break
            temp_answer += 1
            u - need
        answer = max(temp_answer, answer)
            
        
    print(


    return

k, dungeons = 80, [[80,20],[50,40],[30,10],[20,10]]

print(solution(k, dungeons))


