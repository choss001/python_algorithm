import sys
input = sys.stdin.readline

a_num = int(input())
a_list = map(int, input().split())
b_num = int(input())
b_list = map(int, input().split())
answer_list = {}

result = []

for i in a_list:
    if i not in answer_list:
        answer_list[i] = 0
    answer_list[i] = answer_list[i] +1
for j in b_list:
    if j not in answer_list:
        result.append('0')
    else :
        result.append(str(answer_list[j]))

print(' '.join(result))


