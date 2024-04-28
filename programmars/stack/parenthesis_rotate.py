from collections import defaultdict
from collections import deque


def check(lst):

    element_lst = ['[','(','{']
    dic = defaultdict(list)
    mirror_dic = {'[':']', '{':'}', '(':')'}
    for i in range(len(lst)):
        if lst[i] in element_lst:
            dic[mirror_dic[lst[i]]].append(lst[i])
        else:
            if not dic[lst[i]]:
                return False
            dic[lst[i]].pop()
    for i in dic.values():
        if i:
            return False
    return True

def solution(s):
    q = deque(s)
    answer = 0
    if len(s) == 1:
        return 0
    for i in range(len(s)):
        if check(q):
            answer +=1
        temp = q.popleft()
        q.append(temp)
    return answer


#s = "[](){}"
#s = "}]()[{"

s= '['
print(solution(s))


#from collections import deque
#def solution(s):
#    flag  = False   # 올바른 문자열 확인 플래그
#    count = 0      # 올바른 문자열 카운트
#    stack = []     # 올바른 문자열 확인을 위한 스택
#    queue = deque(s) # 문자열 큐로 변환
#    
#    # 문자열 큐 길이 만큼 for loop
#    for i in range(len(queue)):
#        # 괄호 문자열 하나씩 확인하는 for loop
#        print(f'end')
#        for el in queue:
#            print(f'i={i}, el={el}, stack={stack}, queue={queue} flag = {flag}, count={count}')
#            # 괄호 여는 문자열이면 스택에 저장
#            if el == '[' or el == '{' or el == '(':
#                stack.append(el)
#            # 괄호 닫는 문자열이면 스택 마지막 값과 확인
#            else:
#                # 스택에 값이 있고 괄호 문자열이 완성되면 제거 후 플래그 True
#                if stack:
#                    if stack[-1] == '[' and el == ']':
#                        stack.pop()
#                        flag = True
#                    elif stack[-1] == '{' and el == '}':
#                        stack.pop()
#                        flag = True
#                    elif stack[-1] == '(' and el == ')':
#                        stack.pop()
#                        flag = True
#        
#        # 올바른 문자열이 만들어졌고 스택이 비어있다면 카운트 1씩 증가
#        if flag and not stack: count += 1
#        
#        # 스택, 플래그 초기화, 문자열 회전
#        stack = []
#        flag = False        
#        queue.append(queue.popleft())
#        
#    # 올바른 문자열 카운트 반환
#    return count
#s = "}]()[{"
#print(solution(s))
