def solution(s):
    s = s[2:-2].split('},{')
    s.sort(key = lambda x : len(x))

    answer = []
    print(f's={s}')
    for item in s:
        item = item.replace(",", "")
        print(f'before before item = {item}')
        for k in answer:
            print(f'before item = {item}')
            item = item.replace(str(k),'')
            print(f'after item = {item}')
        answer.append(int(item))
    return answer

#s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s = "{{22},{2}}"
print(solution(s))
