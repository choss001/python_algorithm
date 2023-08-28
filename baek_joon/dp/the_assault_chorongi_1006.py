def solve(start):
    global n, w, a, b, c
    print(f'solve = {solve}')
    print(f'n={n}, w={w}, a={a}, b={b}, c={c}')
    for i in range(start, n):
        a[i+1] = min(b[i] + 1, c[i] + 1)
        print(f'a[i+1] = {a[i+1]}, b[i]+1= {b[i]+1}, c[i]+1 = {c[i]+1}')
        if e[i][0] + e[i][1] <= w:
            a[i+1] = min(a[i+1], a[i] + 1)
        if i > 0 and e[i-1][0] + e[i][0] <= w and e[i-1][1] + e[i][1] <= w:
            a[i+1] = min(a[i+1], a[i-1] + 2)
        if i < n-1:
            b[i+1] = a[i+1] + 1
            if e[i][0] + e[i+1][0] <= w:
                b[i+1] = min(b[i+1], c[i] + 1)
            c[i+1] = a[i+1] + 1
            if e[i][1] + e[i+1][1] <= w:
                c[i+1] = min(c[i+1], b[i] + 1)

t = int(input())

while t > 0:
    n, w = map(int, input().split())
    res = 30000
    e = [[0] * 2 for _ in range(10000)]
    a = [0] * 10001
    b = [0] * 10000
    c = [0] * 10000
    e_first_list = list(map(int, input().split()))
    e_second_list = list(map(int, input().split()))
    for i in range(n):
        e[i][0] = e_first_list[i]
    for i in range(n):
        e[i][1] = e_second_list[i]
    print(f'e = {e[:9]}')
    a[0] = 0
    b[0] = c[0] = 1
    solve(0)
    res = min(res, a[n])

    if n > 1 and e[0][0] + e[n-1][0] <= w:
        a[1] = 1
        b[1] = 2
        c[1] = 1 if e[0][1] + e[1][1] <= w else 2
        solve(1)
        res = min(res, c[n-1] + 1)

    if n > 1 and e[0][1] + e[n-1][1] <= w:
        a[1] = 1
        b[1] = 1 if e[0][0] + e[1][0] <= w else 2
        c[1] = 2
        solve(1)
        res = min(res, b[n-1] + 1)

    if n > 1 and e[0][0] + e[n-1][0] <= w and e[0][1] + e[n-1][1] <= w:
        a[1] = 0
        b[1] = c[1] = 1
        solve(1)
        res = min(res, a[n-1] + 2)

    print(res)
    t -= 1

