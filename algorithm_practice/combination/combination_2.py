from itertools import combinations
from itertools import permutations
from bisect import bisect_left
from bisect import bisect_right

def solution():
    perm = permutations([1,2,3], 2)
    print(f'perm = {list(perm)}')
    combi = list(combinations(['A','B','C'], 2))
    print(f'combi = {combi}')

    return
#solution()

def binary_search(a,x):
    print(f'a ={a}, x = {x}')
    print(f'i = bisect left {bisect_left(a,x)}')
    print(f'i = bisect right {bisect_right(a,x)}')
    return

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i >= len(a) or a[i] != x:
        print(f'not found')
    else:
        print(f'i = {i}')
def find_lt(a,x):
    i = bisect_left(a,x)
    if i == len(a):

a = [1, 2, 4, 4,5, 9]
x = 10
a.sort()
#binary_search(a, x)
index(a,x)
