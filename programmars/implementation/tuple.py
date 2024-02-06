def solution(s):
    s = s[2:-2].split('},{')
    s.sort(key = lambda x : len(x))

    answer = []
    for item in s:
        item = item.replace(",", "")
        print(f'item={item}')
        for k in answer:
            item = item.replace(str(k),'')
        answer.append(int(item))



    print(f's={s}')
    print(f'answer = {answer}')


    return answer
#s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
#s = "{{123}}"
#s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
#s = "{{1}}"
s = "{{100000}}"
print(f'solution = {solution(s)}')
