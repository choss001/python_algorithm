left_depth_count = 1
right_depth_count = 1
def mergeSort(arr):
    global left_depth_count, right_depth_count
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # Into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        left_depth_count +=1
        mergeSort(L)
        left_depth_count -=1

 
        # Sorting the second half
        right_depth_count +=1
        mergeSort(R)
        right_depth_count -=1
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
 
 
# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
 
 
# Driver Code
if __name__ == '__main__':
#   arr = [12, 11, 13, 5, 6, 7]
    arr = [1,6,5,2,10,9,20]
    print("Given array is")
    printList(arr)
    mergeSort(arr)
    print("\nSorted array is ")
    printList(arr)

# This code is contributed by Mayank Khanna

I don't understand why merge sort time complexity is NlognN, espectially logN this mean is depth in this script " script here "
if n = 8  depth is 3 but recursive method call 12time but if use binary search algoritm recursive method call just max 3 times
i don't know why two algorithm depth that mean time complexity logn is same.
i think actually time is different Could you explain why and give me example with python code
