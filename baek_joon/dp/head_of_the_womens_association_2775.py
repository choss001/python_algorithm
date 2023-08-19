import sys
input = sys.stdin.readline

T = int(input())
apartment = [[i for i in range(16)]]
for _ in range(15):
    apartment.append([-1]*16)
def sum_dp(floor, ho):
    if apartment[floor][ho] != -1:
        return apartment[floor][ho]
    if floor == 0:
        return apartment[floor][ho]
    if ho == 0:
        return 0
    apartment[floor-1][ho] = sum_dp(floor-1, ho)
    apartment[floor][ho-1] = sum_dp(floor, ho-1)

    return apartment[floor-1][ho] + apartment[floor][ho-1]
sum_dp(15,15)

#for y in range(14, -1, -1):
#    print()
#    for x in range(14):
#        print(f'{apartment[y][x]:8d}', end='')

for _ in range(T):
    floor = int(input())
    ho = int(input())
    print(apartment[floor][ho])
    

