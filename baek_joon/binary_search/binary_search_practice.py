import sys
input = sys.stdin.readline

int_list = list(map(int, input().split()))
value = int(input())
length = len(int_list) - 1

int_list.sort()

def binary_search(h, l):
    print(f'h = {h}, l = {l}, value = {value}, int_list = {int_list}')
    m = (h+l)//2
    if l > h :
        return -1
    if int_list[m] < value :
        return binary_search(h, m+1)
    elif int_list[m] > value:
        return binary_search(m-1, l)
    else:
        return m

print(binary_search(length, 0))



