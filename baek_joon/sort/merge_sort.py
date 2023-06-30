left_depth_count = 1
right_depth_count = 1
def mergeSort(arr):
    global left_depth_count, right_depth_count
    print(f'mergeSort start ! arr={arr} left_depth = {left_depth_count}, right_depth={right_depth_count}')
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # Into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        print(f'mid = {mid}, L={L}, R={R}')
        left_depth_count +=1
        print(f'in mergeSort(L) L={L} ${left_depth_count}$')
        mergeSort(L)
        left_depth_count -=1
        print(f'out mergeSort(L) L = {L}  ${left_depth_count}$')

 
        # Sorting the second half
        right_depth_count +=1
        print(f'in mergeSort(R) R={R} ${right_depth_count}$')
        mergeSort(R)
        right_depth_count -=1
        print(f'out mergeSort(R) R = {R}  ${right_depth_count}$')
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            print(f'L[i] = {L[i]}, R[j] = {R[j]}')
            print(f'i={i}, j={j}, k={k}')
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            print(f'first while after arr = {arr}')
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            print(f'second while after arr = {arr}')
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            print(f'third while after arr = {arr}')
 
 
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
