import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_list = [i for i in range(1, N+1)]


i = 0
print('<',end='')
while N_list:
    #if len(N_list) < i+M :
    if len(N_list) == 1:
        print(f'{N_list[0]}',end='')
        break
    i =  (i+M-1) % len(N_list)
    print(f'{N_list[i]}, ',end='')
    del N_list[i]
    
print('>',end='')
