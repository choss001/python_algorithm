t = int(input())

answer_list = [1] *100

for i in range(3, 100):
    answer_list[i] = answer_list[i-2] + answer_list[i-3]

for _ in range(t):
    p = int(input())
    print(answer_list[p-1])

