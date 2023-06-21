import sys
input = sys.stdin.readline

test_case = int(input())

A_list = []
B_list = []


for _ in range(test_case):
    A_size, B_size = map(int, input().split())
    A_list_component = list(map(int, input().split()))
    B_list_component = list(map(int, input().split()))
    A_list_component.sort(reverse=True)
    B_list_component.sort()
    A_list.append(A_list_component)
    B_list.append(B_list_component)
print(A_list)

for k in range(len(A_list)):
    answer_count = 0
    for i in A_list[k]:
        u = len(B_list[k]) -1
        l = 0
        while True:
            if u < l :
                print(f'u = {u}, m = {m}, l = {l}, A_list = {i} u < l')
                if u == -1:
                    break
                if B_list[k][m] > i :
                    answer_count += m
                    break
                elif B_list[k][m] < i :
                    answer_count += m+1
                    break
            m = (u + l) // 2
            print(f'u = {u}, m = {m}, l = {l}, A_list = {i}')
            if i > B_list[k][m] :
                l = m + 1
            elif i < B_list[k][m] :
                u = m -1
            elif i == B_list[k][m] :
                while i == B_list[k][m]:
                    if m == 0 :
                        break
                    m -=1
                print(f'answer = {m} , A_list = {i} i == B_list')
                if B_list[k][m] != i :
                    answer_count += m+1
                elif B_list[k][m] == i:
                    answer_count += m
                break
    print(answer_count)


            


