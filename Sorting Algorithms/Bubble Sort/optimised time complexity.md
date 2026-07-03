# Optimized Bubble Sort

## Definition

Optimized Bubble Sort is an improved version of the basic Bubble Sort algorithm.

It uses a **flag variable (`is_sorted`)** to check whether any swapping occurred during a pass.

- If at least one swap occurs, the algorithm continues.
- If no swaps occur, it means the array is already sorted, so the algorithm stops immediately.

This optimization improves the **Best Case Time Complexity** from **O(n²)** to **O(n)**.

---

## Why Do We Need Optimization?

Consider an already sorted array.

```text
1 2 3 4 5
```

### Basic Bubble Sort

Even though the array is already sorted, the algorithm still performs:

```text
Pass 1
Pass 2
Pass 3
Pass 4
```

This wastes unnecessary comparisons.

---

### Optimized Bubble Sort

After the first pass:

- No elements are swapped.
- The algorithm realizes the array is already sorted.
- It immediately stops.

Only **one pass** is required.

---

## Algorithm

1. Read the number of elements (`n`).
2. Read the array.
3. Assume the array is already sorted by setting:

```python
is_sorted = True
```

4. Compare adjacent elements.
5. If a swap occurs:
   - Swap the elements.
   - Set `is_sorted = False`.
6. After one complete pass:
   - If `is_sorted` is still `True`, stop the algorithm.
   - Otherwise, continue with the next pass.

---

## Code

```python
def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):

        is_sorted = True

        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:
                is_sorted = False
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if is_sorted:
            break


n = int(input())
arr = list(map(int, input().split()))

bubble_sort(arr)

print(*arr)
```

---

## Dry Run 1 (Already Sorted Array)

### Input

```text
5
1 2 3 4 5
```

Initial Array

```text
[1, 2, 3, 4, 5]
```

### Pass 1

| Comparison | Swap? |
|------------|-------|
| 1 > 2 | ❌ No |
| 2 > 3 | ❌ No |
| 3 > 4 | ❌ No |
| 4 > 5 | ❌ No |

Since no swaps occurred,

```python
is_sorted = True
```

Therefore,

```python
if is_sorted:
    break
```

The algorithm stops after the first pass.

Final Output

```text
1 2 3 4 5
```

---

## Dry Run 2 (Unsorted Array)

### Input

```text
5
5 2 1 9 4
```

Initial Array

```text
[5, 2, 1, 9, 4]
```

### Pass 1

| Comparison | Swap? | Array |
|------------|-------|-------|
| 5 > 2 | ✅ | [2, 5, 1, 9, 4] |
| 5 > 1 | ✅ | [2, 1, 5, 9, 4] |
| 5 > 9 | ❌ | [2, 1, 5, 9, 4] |
| 9 > 4 | ✅ | [2, 1, 5, 4, 9] |

Since swaps occurred,

```python
is_sorted = False
```

The algorithm continues to the next pass.

After several passes, the final array becomes:

```text
1 2 4 5 9
```

---

## Why Does This Work?

Initially,

```python
is_sorted = True
```

This means we assume the array is already sorted.

Whenever a swap occurs,

```python
is_sorted = False
```

This tells the algorithm that the array was **not** sorted.

After finishing a pass:

- If `is_sorted == True`
  - No swaps occurred.
  - The array is already sorted.
  - Stop the algorithm.

- If `is_sorted == False`
  - Swaps occurred.
  - Continue sorting.

---

## Time Complexity

| Case | Basic Bubble Sort | Optimized Bubble Sort |
|------|------------------:|----------------------:|
| Best Case | **O(n²)** | **O(n)** |
| Average Case | **O(n²)** | **O(n²)** |
| Worst Case | **O(n²)** | **O(n²)** |

### Why?

### Best Case

The array is already sorted.

```text
1 2 3 4 5
```

Only one pass is required.

Number of comparisons:

```text
n - 1
```

Therefore,

```text
O(n)
```

---

### Average Case

The array is partially unsorted.

Multiple passes are required.

Time Complexity:

```text
O(n²)
```

---

### Worst Case

The array is sorted in reverse order.

```text
5 4 3 2 1
```

Almost every comparison results in a swap.

Number of comparisons:

```text
(n-1) + (n-2) + ... + 1
= n(n-1)/2
```

Therefore,

```text
O(n²)
```

---

## Space Complexity

```text
O(1)
```

### Why?

The algorithm sorts the array **in place**.

It only uses a few extra variables:

- `n`
- `i`
- `j`
- `is_sorted`

No additional array is created.

---

## Key Points

- Optimized Bubble Sort uses a boolean flag called `is_sorted`.
- If no swaps occur during a pass, the algorithm stops immediately.
- Improves the **Best Case Time Complexity** from **O(n²)** to **O(n)**.
- Average and Worst Case remain **O(n²)**.
- Space Complexity remains **O(1)**.
- This is the version of Bubble Sort commonly used in interviews and textbooks.