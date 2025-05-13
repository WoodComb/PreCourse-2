# Time Complexity: O(n^2)
# Space Complexity: O(log n)
# Did this code successfully run on Leetcode: yes
# Any problem you faced while coding this: no

# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    #write your code here
    # taking the last element as pivot
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high:
    #write your code here
        p_index = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quickSort(arr, low, p_index - 1)
        quickSort(arr, p_index + 1, high)
  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
