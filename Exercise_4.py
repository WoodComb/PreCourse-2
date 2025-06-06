# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Did this code successfully run on Leetcode: 
# Any problem you faced while coding this: no
# Python program for implementation of MergeSort 
def mergeSort(arr):
  if len(arr) > 1:
    # Finding the middle of the array
    mid = len(arr) // 2  
    # Dividing the array elements into 2 halves
    L = arr[:mid]        
    R = arr[mid:]

    mergeSort(L)
    mergeSort(R)

    i = j = k = 0

    # Merging the two halves into original array
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Checking for any remaining elements
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
  for i in arr:
    print(i, end=" ")
  print()

  
# driver code to test the above code 
if __name__ == '__main__': 
    arr = [12, 11, 13, 5, 6, 7]  
    print ("Given array is", end="\n")  
    printList(arr) 
    mergeSort(arr) 
    print("Sorted array is: ", end="\n") 
    printList(arr) 
