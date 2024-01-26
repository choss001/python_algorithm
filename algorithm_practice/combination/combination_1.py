import sys
input = sys.stdin.readline

def combination(current,result, idx, length, elements):
    if length == len(current):
        print(f'current = {current}')
        result.append(current.copy())
        return result
    for i in range(idx,len(elements)):
        if elements[i] not in current:
            current.append(elements[i])
            result = combination(current, result, i, length, elements)
            current.pop()

    return result

def permutation(current,result, idx, length, elements):
    if length == len(current):
        print(f'current = {current}')
        result.append(current.copy())
        return result
    for i in range(len(elements)):
        current.append(elements[i])
        result = permutation(current, result, i, length, elements)
        current.pop()

    return result
    


def solution(n):
    print(combination([],[],0,2,n))
    print(f'permutation = {permutation([],[],0,2,n)}')
    

    return
n = ['A','B','C']
solution(n)
