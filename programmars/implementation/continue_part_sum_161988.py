def solution(sequence):

    a_perse = sequence.copy()
    b_perse = sequence.copy()

    k = 1
    for i in range(len(a_perse)):
        a_perse[i] = a_perse[i] * k
        k *= -1
    k = -1
    for i in range(len(b_perse)):
        b_perse[i] = b_perse[i] * k
        k *= -1
    print(f'a_perse = {a_perse}, b_perse={b_perse}')


    a_answer = 0
    for i in range(len(a_perse)):
        k = i
        a_sum = 0
        print()
        while len(a_perse) > k:
            a_sum = a_sum+a_perse[k]
            k +=1
            print(f'a_sum = {a_sum}')
            a_answer = max(a_sum, a_answer)
    print(f'a_answer={a_answer}')
    b_answer = 0
    for i in range(len(b_perse)):
        k = i
        b_sum = 0
        print()
        while len(b_perse) > k:
            b_sum = b_sum+b_perse[k]
            k +=1
            print(f'b_sum = {b_sum}')
            b_answer = max(b_sum, b_answer)
    print(f'b_answer={b_answer}')

    


    return max(a_answer, b_answer)
sequence = [2,3,-6,1,3,-1,2,4]
solution(sequence)
