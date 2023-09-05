import sys
input = sys.stdin.readline

a,b = map(int, input().split())
i_l = list(map(int, input().split()))

answer_list = []

for item in i_l:
    if item < b:
        answer_list.append(str(item))

print(' '.join(answer_list))
