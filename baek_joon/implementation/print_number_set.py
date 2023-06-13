import sys
input = sys.stdin.readline

M = input()[:-1]

answer_list = [0,0,0,0,0,0,0,0,0,0]

for i in M:
    i = int(i)
    if i == 6:
        if answer_list[i] <= answer_list[9]:
            answer_list[i] += 1
            continue
        else:
            answer_list[9] +=1
            continue
    elif i == 9:
        if answer_list[i] <= answer_list[6]:
            answer_list[i] += 1
            continue
        else:
            answer_list[6] +=1
            continue
    answer_list[i] += 1
print(max(answer_list))



