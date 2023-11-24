import sys
input = sys.stdin.readline

N = int(input())
N_lst = list(map(int, input().split()))

N_lst.sort()
acc_lst = [N_lst[0]]

for i in range(1,N):
    acc_lst.append(acc_lst[i-1] + N_lst[i])
print(f'{sum(acc_lst)}')

