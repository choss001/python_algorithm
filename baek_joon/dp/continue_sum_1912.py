n = int(input())
a = list(map(int, input().split()))

for i in range(1, n):
    print(f'i = {i}, a[{i}] = {a[i]}, a[{i-1}] + a[{i}] = {a[i - 1] + a[i]}')
    a[i] = max(a[i], a[i - 1] + a[i])
    print(f'after a[{i}] = {a[i]}')

print(f'a = {a}')
print(max(a))
