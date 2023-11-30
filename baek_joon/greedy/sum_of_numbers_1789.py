import sys
input = sys.stdin.readline

N = int(input())
sum_lst =[]
sum_answer = 0

i = 0
count = 0
while True:
    i += 1
    sum_answer = sum_answer + i
    count += 1
    if N == sum_answer:
        print(f'{count}')
        break
    elif N < sum_answer:
        print(f'{count-1}')
        break
