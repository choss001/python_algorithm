def get_permutation(arr, n):
    if n == 1:
        return [[el] for el in arr]
    result = []
    for idx, fixed in enumerate(arr):
        rest = arr[:idx] + arr[idx+1:]
        perms = get_permutation(rest, n-1)
        attached = [[fixed] + perm for perm in perms]
        result.extend(attached)
    return result

def solution(n, weak, dist):
    length = len(weak)
    linear_weak = [0] * (length * 2 - 1)

    for i in range(length * 2 - 1):
        linear_weak[i] = weak[i] if i < length else weak[i - length] + n
    print(linear_weak)
    dist.sort(reverse=True)
    
    for i in range(1, len(dist) + 1):
        permutation = get_permutation(dist, i)
        for permu in permutation:
            for j in range(length):
                line = linear_weak[j:length+j]
                for p in permu:
                    coverage = line[0] + p
                    line = [e for e in line if e > coverage]
                    if not line:
                        return i
    return -1
n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
print(solution(n, weak, dist))