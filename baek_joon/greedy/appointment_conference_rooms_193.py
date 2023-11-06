import sys
input = sys.stdin.readline


N = int(input())
N_lst = []

for _ in range(N):
    a, b = map(int, input().split())
    N_lst.append((a, b))
N_lst.sort(key = lambda N_lst:(N_lst[1], N_lst[0]))

end_time = N_lst[0][1]
count = 1
for i in range(1, N):
    start_time = N_lst[i][0]
    if end_time <= start_time:
        end_time = N_lst[i][1]
        count += 1

print(count)
