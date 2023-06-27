import sys
input = sys.stdin.readline
N, M = map(int,input().split())
answer_list = [i for i in range(N, M+1)]
i = 2
while i*i<=M:
    k = 1
    while True:
        dk = i* i * k
        if dk in answer_list :
            answer_list.remove(dk)
        if dk > M :
            break
        k += 1
    i+=1
print(len(answer_list))
