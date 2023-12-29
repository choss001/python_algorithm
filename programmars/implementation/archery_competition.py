
def solution(n, info):
    answer = []
    ryan = [0]*11
    diff = 0

    def dfs(m, idx):
        nonlocal answer, diff, ryan

        print(f'answer = {answer}, diff={diff}, ryan={ryan}, m={m}, idx={idx}')
        if m == n:
            r, a = 0, 0

            for j in range(11):
                if ryan[j] > info[j]:
                    r += 10-j
                elif 0 != info[j] and ryan[j] <= info[j]:
                    a += 10-j
                    
            print(f'r={r}, a={a}')
            if r > a:
                if diff < r - a:
                    diff = r - a
                    answer = ryan[:]
                    
                elif diff == r - a:
                    for i in range(10, -1, -1):
                        if ryan[i] < answer[i]:
                            break
                        if ryan[i] > answer[i]:
                            answer = ryan[:]
                            break
            return

        print(f'm={m}')
        for i in range(idx, 11):
            ryan[i] += 1
            dfs(m+1, i)
            ryan[i] -= 1

    dfs(0, 0)

    return answer if answer else [-1]

n, info = 5, [2,1,1,1,0,0,0,0,0,0,0]
print(f'solution = {solution(n, info)}')
