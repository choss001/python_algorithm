import sys
sys.setrecursionlimit(10**4)

N =  int(input())
end = False
answer = -1
visited = [-1 for _ in range(10000)]
def recursive(package, count, sum_pack):

    if visited[sum_pack] == -1:
        visited[sum_pack] = count
    else:
        return

    global end
    if end == True:
        return
    if sum_pack > N or sum_pack < 0:
        return
    elif sum_pack == N:
        global answer
        answer = count
        end = True
        return

    recursive(5, count +1, sum_pack + 5)
    recursive(3, count + 1, sum_pack + 3)

    return


recursive(0, 0, 0)
print(answer)

