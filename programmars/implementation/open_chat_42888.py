def solution(record):
    dic = {}
    answer = []
    for k in record:
        k = k.split()
        if k[0] != 'Leave': dic[k[1]] = k[2]
    for k in record:
        k = k.split()
        if k[0] == 'Enter': answer.append(f'{dic[k[1]]}님이 들어왔습니다.')
        elif k[0] == 'Leave': answer.append(f'{dic[k[1]]}님이 나갔습니다.')

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
