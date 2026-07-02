# for i in range(n - 1):       i = current iteration/pass (not an array index)

# for j in range(n - i - 1):   j = current array index used to compare arr[j] and arr[j+1]




def bubble_sort(arr):                 # Function to sort the given array using Bubble Sort
    n = len(arr)                      # Store the total number of elements in the array

    for i in range(n - 1):            # Repeat the sorting process (n - 1) times
        for j in range(n - i - 1):    # Compare adjacent elements; skip the sorted part at the end
            if arr[j] > arr[j + 1]:   # If the left element is bigger than the right element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap them

arr = [5, 1, 3, 4, 2]                 # Create an unsorted array
print(arr)                            # Print the original array

bubble_sort(arr)                      # Call the sorting function
print(arr)                            # Print the sorted array