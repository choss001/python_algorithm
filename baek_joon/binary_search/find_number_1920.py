import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
m = int(input())
find_lst = list(map(int, input().split()))


sorted_lst = sorted(lst)
print(f'{sorted_lst}')
def binary_search(find_target):
    start, end = min(lst), max(lst)
    while start < end :

        mid = (start + end) // 2
        if find_target < mid:
            end = mid -1
        else if find_target > mid:
            start = mid + 1
        else:

            break
