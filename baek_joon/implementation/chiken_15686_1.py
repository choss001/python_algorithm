from itertools import combinations

N,M = map(int, input().split())
chi_map = [list(map(int, input().split())) for _ in range(N)]

#y, x
houses = []
chikens = []
answer_dis = 1e9

for i in range(N):
    for j in range(N):
        if chi_map[i][j] == 1:
            houses.append((i, j))
        elif chi_map[i][j] == 2:
            chikens.append((i, j))
for chiken in list(combinations(chikens,M)):
    each_dis = 0
    for house in houses:
        h_dis = 1e9
        for chi in chiken:
            h_dis = min(abs(house[0]-chi[0])+abs(house[1]-chi[1]), h_dis)
        each_dis += h_dis
    answer_dis = min(answer_dis, each_dis)
print(answer_dis)
