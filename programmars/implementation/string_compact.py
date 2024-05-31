import sys
input = sys.stdin.readline

def solution(s):
    answer = 999999999

    for i in range(1,len(s)):
#       if len(s) % i != 0:
#           continue
        print(f'i = {i}')

        temp_before = s[0:0+i]
        temp_count = 1
        temp_result = ''
        for k in range(i,len(s),i):
            temp_now = s[k:k+i]
            print(f'temp_before = {temp_before}, temp_now = {temp_now}')
                
            if temp_before == temp_now:
                temp_count +=1

            else:
                temp_result += ('' if temp_count == 1 else str(temp_count)) + temp_before
                temp_count =1

            if k+i >= len(s):
                print(f' k= {k}, temp_now={temp_now}, temp_before={temp_before}')
                temp_result += ('' if temp_count == 1 else str(temp_count)) + temp_now

            temp_before = temp_now
            print(f'{k}, s = {s[k:k+i]}')
            print(f'temp_result = {temp_result}')
        print(f'temp_result_size = {len(temp_result)}')
        answer = min(answer, len(temp_result))
import sys
input = sys.stdin.readline

def solution(s):
    answer = 999999999

    for i in range(1,len(s)):
#       if len(s) % i != 0:
#           continue
        print(f'i = {i}')

        temp_before = s[0:0+i]
        temp_count = 1
        temp_result = ''
        for k in range(i,len(s),i):
            temp_now = s[k:k+i]
            print(f'temp_before = {temp_before}, temp_now = {temp_now}')
                
            if temp_before == temp_now:
                temp_count +=1

            else:
                temp_result += ('' if temp_count == 1 else str(temp_count)) + temp_before
                temp_count =1

            if k+i >= len(s):
                print(f' k= {k}, temp_now={temp_now}, temp_before={temp_before}')
                temp_result += ('' if temp_count == 1 else str(temp_count)) + temp_now

            temp_before = temp_now
            print(f'{k}, s = {s[k:k+i]}')
            print(f'temp_result = {temp_result}')
        print(f'temp_result_size = {len(temp_result)}')
        answer = min(answer, len(temp_result))
    return answer
        
    return 1 if answer == 999999999 else answer

#s = "abcabcabcabcdededededede"
#s = "xababcdcdababcdcd"
#s = "ababcdcdababcdcd"
#s = "abcabcdede"
s = "1"
print(solution(s))


