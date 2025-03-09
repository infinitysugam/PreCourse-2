#Time Complexity = O(nlogn)
#Space Complexity = O(logn)

# Python program for implementation of Quicksort

# This function is same in both iterative and recursive
def partition(arr, l, h):
    pivot = arr[h] # Choosing the last element as pivot 
    i = l-1   #Smaller element

    for j in range(l,h):
        if arr[j] < pivot: # If current element is smaller than pivot 
            i += 1
            arr[i],arr[j]= arr[j],arr[i] # Swap element 

    #Place pivot in the correct position
    arr[i+1],arr[h] = arr[l],arr[i+1]
    return i+1 


def quickSortIterative(arr, l, h):
    stack = []
    
    # Push initial values of l and h onto the stack
    stack.append((l, h))

    # Keep popping from the stack while it is not empty
    while stack:
        l, h = stack.pop()  # Get the last range
        
        # Partition the array and get the pivot index
        pivot_index = partition(arr, l, h)

        # If there are elements on the left side of the pivot, push left subarray onto the stack
        if pivot_index - 1 > l:
            stack.append((l, pivot_index - 1))

        # If there are elements on the right side of the pivot, push right subarray onto the stack
        if pivot_index + 1 < h:
            stack.append((pivot_index + 1, h))

