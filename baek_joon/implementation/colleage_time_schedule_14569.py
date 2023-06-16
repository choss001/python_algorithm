import sys
input = sys.stdin.readline

C = int(input())
colleage_list = [list(map(int, input().split()))[1:] for _ in range(C)]
S = int(input())
student_list = [list(map(int, input().split()))[1:] for _ in range(S)]

for item in student_list:
    answer_num = 0
    for colleages in colleage_list:
        success_flag = True
        for col in colleages:
            if col not in item :
                success_flag = False
                break
        if success_flag == True :
            answer_num += 1
    print(answer_num)


        

