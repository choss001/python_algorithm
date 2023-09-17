import sys
input = sys.stdin.readline


ix, iy = map(int, input().split())

print(f'{ix} {iy}')
input_list = []
for dy in range(iy):
    ix_list = list(map(int, input().split()))
    input_list.append(ix_list)

print(f'{input_list}')
