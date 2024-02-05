

f = open("temp.txt", "w+")

def solution(n, info):
    global answer, result

    def score(ryan):
        s = 0
        for i in range(11):
            if ryan[i] == info[i] == 0:
                continue
            if ryan[i] > info[i]:
                s += 10 - i
            else:
                s -= 10 - i
        return s

    def dfs(idx, left, ryan):
        global answer, result
        f.write(f'idx={idx}, left={left}, ryan={ryan}\n')
        if idx == -1 and left:
            return
        if left == 0:
            s = score(ryan)
            f.write(f's={s}\n')
            if result < s:
                answer = ryan[:]
                result = s
            return
        for i in range(left, -1, -1):
            f.write(f'i={i}, ryan[idx]={ryan[idx]}\n')
            ryan[idx] = i
            dfs(idx-1, left-i, ryan)
            ryan[idx] = 0

    answer = [0 for _ in range(11)]
    result = 0
    dfs(10, n, [0 for _ in range(11)])
    return answer if result != 0 else [-1]

n, info = 9, [0,0,1,2,0,1,1,1,1,1,1]
print(f'{solution(n, info)}')
f.close()
f.close()

