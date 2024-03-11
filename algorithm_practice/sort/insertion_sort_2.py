def solution(l):
    
    for i in range(1,len(l)):
        for k in range(0,i+1):
            if l[k] < l[k-1]:
                t = l[k-1]
                l[k-1] = l[k]
                l[k] = t

    return l

l = [3,7,5,1]

print(f'solution = {solution(l)}')
