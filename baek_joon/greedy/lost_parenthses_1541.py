import sys
input = sys.stdin.readline

N = input().split('-')
N[-1] = N[-1][:-1]

total_sum = 0
for i in range(len(N)):
    if i == 0 and len(N) > 1:
        #total_sum += int(N[i])
        temp = map(int, N[i].split('+'))
        total_sum += sum(temp)
    elif len(N) == 1:
        temp = map(int, N[i].split('+'))
        total_sum += sum(temp)
    else:
        temp = map(int, N[i].split('+'))
        total_sum -= sum(temp)
print(f'{total_sum}')
