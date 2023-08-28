def longestSubS(sequence):
    sequence = [0] + sequence
    sub = [[0, 0] for _ in sequence]
    print(f'before sub = {sub}')

    for i, n in enumerate(sequence):
        if i: # continue at 0
            sub[i][0] = max(sub[i-1]) # not using value
            print(f'i = {i}, n = {n}')
            print(f'some after sub = {sub}')
            print(f'sub[i-1] = {sub[i-1]}')

            prev = [sub[j][1] for j in range(i) if sequence[j] < sequence[i]]
            print(f'prev = {prev}')
            sub[i][1] = max(prev) + 1 # using value

    return max(sub[-1])
        
####

n = int(input())
seq = list(map(int, input().split()))

print(longestSubS(seq))
