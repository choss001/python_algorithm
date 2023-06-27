from itertools import permutations
from itertools import combinations

print('nothing')

prime_number_list = []
def get_prime_numbers(max_number):
    num_list = [1 for _ in range(max_number + 1)]
    num_list[0] = 0
    num_list[1] = 0
    max_p = int(max_number ** 0.5)
    for i in range(2, max_number + 1):
        if num_list[2] != 1:
            continue
        for k in range(i + i, max_number + 1, i):
            num_list[k] = 0
    global prime_number_list
    prime_number_list = [i for i in range(max_number + 1) if num_list[i] == 1]
    #print(f'prime_number_list = {prime_number_list}')
    
        

get_prime_numbers(120)
print(f'prime_number_list = {prime_number_list}')
