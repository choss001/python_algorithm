n = int(input())
t= []
for i in range(n):
  a = list(map(int,input().split()))
  t.append(a)
print(f'a = {a}')
print(f't = {t}')
for i in range(1,n):
  for j in range(i+1):
    if j == 0:
      t[i][0] += t[i-1][0]
    elif j == i:
      t[i][j] += t[i-1][j-1]
    else:
      t[i][j] += max(t[i-1][j-1],t[i-1][j])
print(f'after t = {t}')
print(max(t[n-1]))
