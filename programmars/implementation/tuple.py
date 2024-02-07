def solution(s):
    s = s[2:-2].split('},{')
    s.sort(key = lambda x : len(x))

    answer = []
    print(f's = {s}')
    for item in s:
        item_lst = list(map(int,item.split(",")))
        for k in item_lst:
            if k in answer:
                continue
            answer.append(k)

    return answer
#s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
#s = "{{123}}"
#s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
#s = "{{1}}"
#s = "{{100000}}"
s =  "{{22},{2,22},{242,22,2}}"
print(f'solution = {solution(s)}')
