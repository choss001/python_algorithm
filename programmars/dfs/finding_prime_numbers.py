from itertools import permutations

def prime_number_list_up(number):
    boolean_lst = [True] * (number+1)
    boolean_lst[1] = False
    boolean_lst[0] = False
    for i in range(2, number+1):
        if boolean_lst[i]:
            for k in range(i*2, number+1, i):
                boolean_lst[k] = False


    return boolean_lst

#def prime_number():


def solution(numbers):
    answer = 0
    boolean_lst = prime_number_list_up(9999999)
    check_duple = [True] * (9999999+1)
    for i in range(1, len(numbers)+1):
        lst = list(permutations(numbers,i))
        for item in lst:
            value = int(''.join(item))
            print(f'value = {value}')
            if boolean_lst[value] and check_duple[value]:
                check_duple[value] = False
                answer += 1


    return answer

numbers = "011"
print(solution(numbers))


