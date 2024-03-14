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


