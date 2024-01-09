import sys
input = sys.stdin.readline
#k,  dungeons= 80, [[80,20],[50,40],[30,10]]

def generate_combination(elements, length, current, result):
    if length == 0:
        result.append(current.copy())
        return
    for i in elements:
        if i not in current:
            current.append(i)
            generate_combination(elements, length-1, current, result)
            current.pop()
elements, result = ['A','B','C'], []
generate_combination(elements, 3, [], result)
print(f'result = {result}')
