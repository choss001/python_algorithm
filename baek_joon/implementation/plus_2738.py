N, M = map(int, input().split())
N_list = [list(map(int, input().split())) for _ in range(N)]
M_list = [list(map(int, input().split())) for _ in range(N)]

A_list = []
for i in range(N):
    line_list =[]
    for j in range(M):
        line_list.append(N_list[i][j] + M_list[i][j])
    A_list.append(line_list)
for i in range(N):
    for j in range(M):
        print(A_list[i][j],end=' ')
    print()
