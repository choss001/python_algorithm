import sys
input = sys.stdin.readline

def backtracking():
    if len(array) == M:
        print(' '.join(map(str, array)))
        return
    for i in range(1, N+1):
        if i not in array:
            if len(array) > 0:
                if array[-1] < i:
                    array.append(i)
                    backtracking()
                    array.pop()
            else:    
                array.append(i)
                backtracking()
                array.pop()

N,M = map(int,input().split())
array = []
backtracking()
