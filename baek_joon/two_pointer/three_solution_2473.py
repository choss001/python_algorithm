import sys
input = sys.stdin.readline

n = int(input())
n_lst = list(map(int, input().split()))

n_lst.sort()

answer_lst = [n_lst[0], n_lst[1], n_lst[2]]
answer_sum = abs(sum(answer_lst))

for i in range(len(n_lst)):
    refer = n_lst[i]

    left, right = 0, len(temp_lst) - 1
    while left < right:
        temp_sum = temp_lst[left] + temp_lst[right] + n_lst_fixed_value

        if abs(temp_sum) < answer_sum:
            answer_sum = abs(temp_sum)
            answer_lst = [temp_lst[left], temp_lst[right], n_lst_fixed_value]
        
        if temp_sum > 0:
            right -= 1
        elif temp_sum < 0:
            left += 1
        else:
            answer_lst = [temp_lst[left], temp_lst[right], n_lst_fixed_value]
            break

answer_lst.sort()
print(f'{answer_lst}')

