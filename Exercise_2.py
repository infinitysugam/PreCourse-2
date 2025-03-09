#Time Complexity = O(nlogn)
#Space Complexity = O(logn)
# Python program for implementation of Quicksort Sort 
  
# give you explanation for the approach
def partition(arr,low,high):
    pivot = arr[high] # Choosing the last element as pivot 
    i = low-1   #Smaller element

    for j in range(low,high):
        if arr[j] < pivot: # If current element is smaller than pivot 
            i += 1
            arr[i],arr[j]= arr[j],arr[i] # Swap element 

    #Place pivot in the correct position
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1 
  
  

# Function to do Quick sort 
def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)

        # Recursively sort elements before and after pivot
        quickSort(arr,low,pi-1) # Left subarray
        quickSort(arr,pi+1,high) # Right Subarray


    

  
# Driver code to test above 
arr = [10, 7, 8, 9, 1, 5] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %arr[i]), 
  
 
