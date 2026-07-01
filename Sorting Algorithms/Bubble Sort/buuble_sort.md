# Bubble Sort

## Definition

Bubble Sort is a simple sorting algorithm that repeatedly compares **two adjacent (neighboring) elements** and swaps them if they are in the wrong order.

After every pass (iteration), the **largest unsorted element moves to the end of the array**, just like an air bubble rises to the surface. That's why it's called **Bubble Sort**.

---

## Input Format

The first line contains an integer **n**, representing the number of elements in the array.

The second line contains **n** space-separated integers.

### Example Input

```text
5
5 1 3 4 2
```

---

## Example

Initial Array:

```text
[5, 1, 3, 4, 2]
```

### Pass 1

```text
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

The next pass places **4** in its correct position, then **3**, and finally **2**, resulting in a fully sorted array.

---

## Algorithm

1. Read the number of elements (`n`).
2. Read the array containing `n` integers.
3. Compare two adjacent elements.
4. If the left element is greater than the right element, swap them.
5. Continue comparing until reaching the end of the unsorted portion.
6. Repeat the process until the array is sorted.
7. Print the sorted array.

---

## Code

```python
def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Read the number of elements
n = int(input())

# Read the array
arr = list(map(int, input().split()))

bubble_sort(arr)

# Print the sorted array
print(*arr)
```

---

## Sample Input

```text
5
5 1 3 4 2
```

## Sample Output

```text
1 2 3 4 5
```

---

## Understanding the Input

### Reading the Size of the Array

```python
n = int(input())
```

Suppose the user enters:

```text
5
```

Then:

```python
n = 5
```

This tells the program that the array contains **5 elements**.

---

### Reading the Array

```python
arr = list(map(int, input().split()))
```

Suppose the next input line is:

```text
5 1 3 4 2
```

Let's break it down step by step.

#### Step 1

```python
input()
```

Reads the entire line as a string.

```text
"5 1 3 4 2"
```

---

#### Step 2

```python
.split()
```

Splits the string wherever there is a space.

```python
['5', '1', '3', '4', '2']
```

Notice that these are **strings**, not numbers.

---

#### Step 3

```python
map(int, ...)
```

Converts each string into an integer.

```python
5
1
3
4
2
```

---

#### Step 4

```python
list(...)
```

Stores all those integers inside a list.

```python
[5, 1, 3, 4, 2]
```

So,

```python
arr = list(map(int, input().split()))
```

is equivalent to writing:

```python
arr = [5, 1, 3, 4, 2]
```

except that the values come from the user instead of being hardcoded in the program.

---

## Time Complexity

| Case | Complexity |
|------|------------|
| Best Case (Basic Implementation) | **O(n²)** |
| Average Case | **O(n²)** |
| Worst Case | **O(n²)** |

### Why?

Bubble Sort uses **two nested loops**.

- The outer loop runs **(n − 1)** times.
- During each pass, the inner loop compares adjacent elements.

The total number of comparisons is:

```text
(n - 1) + (n - 2) + ... + 2 + 1
= n(n - 1) / 2
```

Ignoring constants and lower-order terms in Big-O notation:

```text
O(n²)
```

---

## Space Complexity

```text
O(1)
```

### Why?

Bubble Sort sorts the array **in place**, meaning it modifies the original array instead of creating a new one.

It only uses a few extra variables (`n`, `i`, and `j`), so the extra memory required remains constant.

---

## Key Points

- Reads the array from user input.
- Compares adjacent elements.
- Swaps only when the left element is greater than the right element.
- After every pass, the largest unsorted element moves to the end.
- Sorts the array in place.
- Uses constant extra memory **O(1)**.
- Simple to understand and implement.
- Not suitable for large datasets because its time complexity is **O(n²)**.
