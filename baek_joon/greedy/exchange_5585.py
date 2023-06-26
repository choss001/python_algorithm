import sys
input = sys.stdin.readline

M = int(input())

ex = 1000-M

exchange_money = [500, 100, 50, 10, 5, 1]

answer = 0

for i in exchange_money:
    while ex >= i:
        ex = ex - i
        answer += 1

print(answer)
