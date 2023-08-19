import sys
t=int(sys.stdin.readline())
for i in range(t):
    k=int(sys.stdin.readline())
    n=int(sys.stdin.readline())
    d=[i for i in range(1, n+1)]
    print(f'd = {d}')
    for j in range(k):
        for x in range(1, n):
            d[x]+=d[x-1]
            print(f'j = {j}, x = {x}')
            print(f'd = {d}')
    print(d[-1])
