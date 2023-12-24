from collections import Counter


def solution(weights):
    counter = Counter(weights)
    answer = 0
    visited = {}
    for weight, v in counter.items():
        if v > 1 and weight not in visited:
            visited[weight] = 1
            answer += (v)*(v-1)//2
            print(f'condition in weight = {weight}, v = {v}, ==, answer={answer}')
        if weight * 1/2 in counter:
            answer += counter[weight * 1/2] * v
            print(f'condition in weight = {weight}, v = {v}, 1/2, answer={answer}')
        if weight * 3/4 in counter:
            answer += counter[weight * 3/4] * v
            print(f'condition in weight = {weight}, v = {v}, 3/4, answer={answer}')
        if weight * 2/3 in counter:
            answer += counter[weight * 2/3] * v
            print(f'condition in weight = {weight}, v = {v}, 2/3, answer={answer}')


    return answer

#weights = [100,180,360,100,270]
weights = [100, 100, 100, 150, 150, 200, 300]
#weights = [200, 100, 100, 200, 100]
print(solution(weights))

#4   3   2   0   2   3   4
#        360             180 
#    270         180
#270                 360
#        100     100
#
#360 * 1/2 = 180
#270 * 2/3 = 180
#270 * 4/3 = 360
#
#4*a = 2*b   a = 2/4*b   2a = 4b
#4*a = 3*b   a = 3/4*b   3a = 4b
#4*a = 4*b   a = 4/4*b   4a = 4b
#
#3*a = 2*b   a = 2/3*b   2a = 3b
#===============================
#3*a = 3*b   a = 3/3*b   3a = 3b
#3*a = 4*b   a = 4/3*b   4a = 3b
#
#2*a = 2*b   a = 2/2*b   2a = 2b
#2*a = 3*b   a = 3/2*b   3a = 2b
#2*a = 4*b   a = 4/2*b   4a = 2b

#100 *3
#150 * 1
#150 : 100 = 6
#200 : 10016

