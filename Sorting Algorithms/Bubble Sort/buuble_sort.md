# Bubble Sort

## Definition

Bubble Sort is a simple sorting algorithm that repeatedly compares **two adjacent (neighboring) elements** and swaps them if they are in the wrong order.

After every pass (iteration), the **largest unsorted element moves to the end of the array**, just like an air bubble rises to the surface. That's why it's called **Bubble Sort**.

---

## Example

Given an array:

```python
arr = [5, 1, 3, 4, 2]
```

### Pass 1

```
[5, 1, 3, 4, 2]
 ↓
5 > 1 → Swap

[1, 5, 3, 4, 2]
    ↓
5 > 3 → Swap

[1, 3, 5, 4, 2]
       ↓
5 > 4 → Swap

[1, 3, 4, 5, 2]
          ↓
5 > 2 → Swap

[1, 3, 4, 2, 5]
```

Notice that **5**, the largest element, has reached the last position.

The next pass places **4** in its correct position, then **3**, and so on until the array is completely sorted.

---

## Algorithm

1. Compare two adjacent elements.
2. If the left element is greater than the right element, swap them.
3. Continue comparing until you reach the end of the array.
4. Repeat the process until the array is sorted.

---

## Code

```python
def bubble_sort(arr):
    n = len(arr)                      # Number of elements

    for i in range(n - 1):            # Repeat the process (n - 1) times
        for j in range(n - i - 1):    # Compare adjacent elements
            if arr[j] > arr[j + 1]:   # If left > right
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap


arr = [5, 1, 3, 4, 2]

print(arr)

bubble_sort(arr)

print(arr)
```

---

## Time Complexity

* **Best Case:** O(n²) *(for this basic implementation)*
* **Average Case:** O(n²)
* **Worst Case:** O(n²)

### Why?

Bubble Sort uses **two nested loops**.

* The outer loop runs approximately **n** times.
* The inner loop also runs approximately **n** times.

So the total number of comparisons is roughly:

```
n × n = n²
```

Therefore, the time complexity is:

```
O(n²)
```

---

## Space Complexity

```
O(1)
```

### Why?

Bubble Sort sorts the array **in place**. It only uses a few extra variables (`i`, `j`, and `n`) and does not create another array.

---

## Key Points

* Compares adjacent elements.
* Swaps only when the left element is greater than the right element.
* After each pass, the largest unsorted element reaches the end.
* Simple to understand and implement.
* Not efficient for large datasets because it has O(n²) time complexity.
