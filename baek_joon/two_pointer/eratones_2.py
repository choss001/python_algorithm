import sys
input = sys.stdin.readline

n = int(input())
trace = [False, False] + [True] * (n  + 1)
answer_lnt = []
for i in range(2,n+1):
    if trace[i]:
        answer_lnt.append(i)
        for k in range(i*2, n+1, i):
            trace[k] = False


left, right = 0, 0

answer_count = 0
temp_sum = 0
while True:
    if temp_sum >= n:
        if temp_sum == n:
            answer_count += 1
        temp_sum -= answer_lnt[left]
        left += 1
    elif right == len(answer_lnt):
        break
    else:
        temp_sum += answer_lnt[right]
        right += 1

    
print(f'answer_count = {answer_count}')
