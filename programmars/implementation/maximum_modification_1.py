def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            print(f'a={a}, b={b}, e={e}')
            temp = [f"({i})" for i in e.split(b)]
            print(f'temp={temp}')
            temp_list.append(f'({b.join(temp)})')
            print(f'temp_list={temp_list}')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)

#expression = "50*6-3*2"
expression = "100-200*300-500+20"
print(f'solution={solution(expression)}')
