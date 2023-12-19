import sys
input = sys.stdin.readline


N, M = map(int, input().split())

N_lst = [int(input()) for _ in range(N)]

answer = 0

for i in range(N-1, -1, -1):
    if M >= N_lst[i]:
        answer += M // N_lst[i]
        M = M%N_lst[i]
print(f'{answer}')
