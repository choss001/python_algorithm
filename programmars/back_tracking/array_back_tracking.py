def solution():
    k = 5

    lst = [2,1,1,1,0,0,0,0,0,0,0]

    def dfs(lst, m, target, idx):
        nonlocal k
        if k == m:
            print(f'lst = {lst} target = {target}, k={k}, m={m}')

            a, b = 0, 0
            for l in range(11):
                if lst[l] != 0 and lst[l] >= target[l]:
                    a += 10 - l 
                elif lst[l] < target[l]:
                    b += 10 - l
                    
            print(f'a = {a}, b ={b}')    

            return -1
        for i in range(idx, 11):
            target[i] += 1
            dfs(lst, m+1, target, i)
            target[i] -= 1

        return -1


    dfs(lst, 0, [0]*11, 0)

    return -1

print(solution())

