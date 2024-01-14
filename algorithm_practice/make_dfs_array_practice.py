import sys
input = sys.stdin.readline

def solution(size, max_number):
    print(f'size = {size} max_number={max_number}')

    lst = [0]*size
    def dfs(lst, idx, m):
        if max_number == m:
            print(f'lst = {lst}')
            return -1

        for i in range(idx, size):
            lst[i] +=1
            dfs(lst, i, m+1)
            lst[i] -= 1
            
        return -1
    dfs(lst, 0, 0)
    return -1

#size = input()
#max_number = input()
size, max_number = int(input()), int(input())

solution(size, max_number)


