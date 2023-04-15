n = int(input())
nList = list(map(int, input().split()))

m = int(input())
mList = list(map(int, input().split()))

nList.sort()

def binary_search(start, end, target):
    if start == end:
        print('0')
        return
    middle = int((start + end) / 2)
    if nList[middle] == target:
        print('1')
        return 
    elif nList[middle] > target:
        binary_search(start,middle,target)
    else:
        binary_search(middle + 1,end,target)
        
for target in mList:
    binary_search(0, n, target)
