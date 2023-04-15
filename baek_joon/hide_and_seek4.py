import copy

n,m = map(int, input().split())
#n subin
#m target
answer = 1e9

def reculsive(n, m, tempAnswer):
    print('n :',n,',m: ',m,',tempAnswer : ',tempAnswer)
    global answer
    if tempAnswer > 20:
        return
    if n > m:
        reculsive(n-1, m, tempAnswer+1)
    elif n < m:
    #   3option
#       tempAnswer1 = copy.deepcopy(tempAnswer)
#       tempAnswer2 = copy.deepcopy(tempAnswer)
#       n1 = copy.deepcopy(n)
#       n2 = copy.deepcopy(n)
        reculsive(n*2, m, tempAnswer)
        reculsive(n+1, m, tempAnswer +1)
        reculsive(n-1, m, tempAnswer+1)
    else:
        answer = min(tempAnswer, answer)
        print('result : ',answer)

reculsive(n, m, 0)

print(answer)
