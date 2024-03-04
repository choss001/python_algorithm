#def insertion_sort(lst):
#
#    return
#
#lst = [5,2,3,1,1,1,10,100]


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [12, 11, 13, 5, 5]
insertionSort(arr)
print(arr)


#
#pseudo code 
#make key
#and make element using smaller then key index
#if key is smaller then element move element right until that element sorted
#
#i, j = 1, 0
#arr[1] = arr[0]
#[11,11]
#j -1

    
