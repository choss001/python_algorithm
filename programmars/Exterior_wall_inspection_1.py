from itertools import permutations

def get_permutation(arr, n):
    print()
    print(f'arr = {arr}, n = {n}')
    if n == 1:
        return [[el] for el in arr]
    result = []
    for idx, fixed in enumerate(arr):
        print(f'idx = {idx}, fixed = {fixed}')
        rest = arr[:idx] + arr[idx+1:]
        print(f'rest = {rest}')
        perms = get_permutation(rest, n-1)
        print(f'perms = {perms}')
        attached = [[fixed] + perm for perm in perms]
        print(f'attacehd = {attached}')
        result.extend(attached)
        print(f'result = {result}')
    return result

def solution(n, weak, dist):
    length = len(weak)
    linear_weak = [0] * (length * 2 - 1)

    for i in range(length * 2 - 1):
        linear_weak[i] = weak[i] if i < length else weak[i - length] + n
    print(linear_weak)
    dist.sort(reverse=True)
    
    for i in range(1, len(dist) + 1):
        permutation = list(permutations(dist, i))
        print(f'permutation = {permutation}')
        print()
        for permu in permutation:
            print(f'permu = {permu}')
            for j in range(length):
                line = linear_weak[j:length+j]
                print(f'line = {line}')
                for p in permu:
                    coverage = line[0] + p
                    print(f'coverage = {coverage} , p = {p}')
                    line = [e for e in line if e > coverage]
                    print(f'after line = {line}')
                    if not line:
                        return i
    return -1
n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
print(solution(n, weak, dist))

n = 12
weak = [1,3,4,9,10]
dist = [3,5,7]
print(solution(n, weak, dist))


