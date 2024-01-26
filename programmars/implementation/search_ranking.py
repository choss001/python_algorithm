import sys
input = sys.stdin.readline

def solution(info, query):
    members =[]
    condition_idx = [0,2,4,6,7]
    for i in info:
        member = i.split(' ')
        print(f'member={member}')
        members.append(member)
    print(f'members = {members}')

    answer_lst = []
    for i in query:
        condition = i.split(' ')
        temp_answer = 0
        for k in members:
            if condition[0] != '-' and condition[0] != k[0]:
                continue
            if condition[2] != '-' and condition[2] != k[1]:
                continue
            if condition[4] != '-' and condition[4] != k[2]:
                continue
            if condition[6] != '-' and condition[6] != k[3]:
                continue
            if int(condition[7]) > int(k[4]):
                continue
            temp_answer += 1
        answer_lst.append(temp_answer)
        
    print(f'answer_lst = {answer_lst}')

    return answer_lst

info, query = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"] 

print(solution(info,query))
