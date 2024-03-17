import sys
input = sys.stdin.readline

def solution(s):
    temp_lst = []
    answer = 'true'

    for i in s:
        if i == '(':
            temp_lst.append('(')
        else:
            if temp_lst:
                temp_lst.pop()
            else:
                answer = 'false'
                break

    return answer

#s = "(())()"
s = ")()("
print(solution(s))
