from collections import deque

def solution(n, t, m, p):
    answer = ''
#   print(n_to_jinso(16, 31))
    temp_answer =  deque()
    temp_answer.appendleft('0')
    for i in range(0,100):
        print(''.join(map(str,n_to_jinso(n,i))))
        temp_answer.append(''.join(map(str,n_to_jinso(n,i))))
    print(''.join(temp_answer))
    temp_answer = ''.join(temp_answer)
    temp_answer = temp_answer *2
    i = p-1
    answer = deque()
    while i < len(temp_answer):
        if len(answer) == t:
            break
        print(f'temp_answer[i] = {temp_answer[i]}')
        answer.append(temp_answer[i])
        i += m

    
    print(f'answer = {answer}')
    return ''.join(answer)

def n_to_jinso(jinsu, number):
    q = deque()

    while number > 0:
        q.appendleft(number_to_alphabet(number % jinsu))
        number = number // jinsu
    return q

def number_to_alphabet(number):
    dic = {}
    for i in range(6): dic[10+i] = chr(65+i)
    if number < 10: return number
    return dic[number]
#n,t,m,p = 2,4,2,1
n,t,m,p = 16,16,2,1
solution(n,t,m,p)
