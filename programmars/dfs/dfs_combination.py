import sys
input = sys.stdin.readline
#k,  dungeons= 80, [[80,20],[50,40],[30,10]]


def generate_combinations(lst, length, current_combination, result):
    if length == 0:
        result.append(current_combination.copy())
        return

    for element in lst:
        current_combination.append(element)
        generate_combinations(lst, length - 1, current_combination, result)
        current_combination.pop()

def generate_all_combinations(lst):
    result = []
    for length in range(1, len(lst) + 1):
        generate_combinations(lst, length, [], result)
    return result

lst = ['A', 'B', 'C']
all_combinations = generate_all_combinations(lst)

result = []
generate_combinations(lst, 4, [], result)
print(result)

# Print all combinations
for combination in all_combinations:
    print(combination)

