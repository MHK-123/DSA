# Bubble Sort (Stable Sorting Algorithm)

arr = [2, 6, 4, 1, 2]

print("Original Array:", arr)

n = len(arr)

for i in range(n - 1):
    for j in range(n - i - 1):

        # Swap only when left element is greater
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted Array :", arr)