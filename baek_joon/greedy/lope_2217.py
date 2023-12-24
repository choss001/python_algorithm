import sys
input = sys.stdin.readline

N = int(input())
N_lst = [int(input()) for _ in range(N)]
N_lst.sort()
answer = 0

for i in range(N):
    answer = max(N_lst[i] * (N - i), answer)
print(f'{answer}')
