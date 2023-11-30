import sys
input = sys.stdin.readline

def solution(storey):

    answer = 0
    while storey >0 :
        if storey % 10 >= 5:
#           if storey % 100 >= 50:
            answer += 10 - (storey % 10)
            print(f'+answer = {10 - (storey%10)}')
            storey += 10 - (storey % 10)
            storey //= 10
            print(f'storey = {storey}')
            continue
        answer += (storey % 10) 
        print(f'+answer = {storey %10}')
        storey -= (storey % 10)
        storey //= 10
        print(f'storey = {storey}')


    return answer
#storey = 2554
#storey = 3554
storey = 1
print(solution(storey))
