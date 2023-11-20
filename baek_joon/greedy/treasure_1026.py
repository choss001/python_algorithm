import sys
input = sys.stdin.readline

N = int(input())
A_lst = list(map(int, input().split()))
B_lst = list(map(int, input().split()))

A_lst.sort()
after_B_lst = sorted(B_lst, reverse=True)
dic = {}
answer = 0
for i in range(N):
    answer += after_B_lst[i] * A_lst[i]
print(answer)
