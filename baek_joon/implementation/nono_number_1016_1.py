minn, maxx = map(int,input().split())
a = [i**2 for i in range(2,int(maxx**0.5)+1)]
print(f'a = {a}')
num = [1] * (maxx-minn+1)
print(f'num = {num}')
for i in a:
    n = minn//i*i
    while(n < maxx+1):
        if n >= minn:
            num[n-minn] = 0
        n += i
print(f'num = {num}')
print(sum(num))
