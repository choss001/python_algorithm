def solution(n, m, section):
    
    count = 0
    end = 99999999
    for i in range(len(section)):
        start = i
        end = start + m - 1
        if start >= end :
            continue
        end = start + m - 1
        if end > n :
            count +=1
            break
        count +=1
    return count




        



n,m,section=8,4,[2,3,6]
print(solution(n,m,section))
