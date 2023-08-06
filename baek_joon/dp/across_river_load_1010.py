store_list = [[-1] * 30 for _ in range(30)]

def dp(i, j):
    if i == j:
        return 1
    if i == 1:
        return j
    if store_list[i][j] == -1 :
        store_list[i][j] = dp(i-1, j-1) + dp(i, j-1)
    return store_list[i][j]

for _ in range(int(input())):
    i, j = map(int, input().split())
    print(dp(i, j))

