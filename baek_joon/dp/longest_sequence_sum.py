import sys
input = sys.stdin.readline

m = int(input())
input_list = list(map(int, input().split()))

dp_list = [1] * m

for i in range(1,m):
    for j in range(i):
        if input_list[i] > input_list[j]:
           dp_list[i] = max(dp_list[j] +1 , dp_list[i]) 
print(max(dp_list))
