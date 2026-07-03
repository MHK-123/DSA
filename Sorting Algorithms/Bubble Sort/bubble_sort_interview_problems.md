# Problem 1 - Maximum Swaps Required in Bubble Sort

## Problem Statement

Find the **maximum number of swaps** required by Bubble Sort to sort an array of length **n**.

---

## Observation

The maximum number of swaps occurs when the array is in **reverse sorted order**.

Example for n = 5

```text
5 4 3 2 1
```

Every inversion must be swapped.

---

## Formula

Maximum swaps:

```text
n(n-1)/2
```

---

### Example

For

```text
n = 6
```

```text
6 × 5 / 2 = 15
```

Maximum swaps = **15**

---

## Why?

During Bubble Sort,

Pass 1 performs

```text
n-1
```

comparisons.

Pass 2 performs

```text
n-2
```

comparisons.

Pass 3 performs

```text
n-3
```

...

Total

```text
(n-1)+(n-2)+...+1
```

Using the sum formula,

```text
n(n-1)/2
```

---

## Code

```python
def bubble_sort_swap_count(arr):
    n = len(arr)
    swap_count = 0

    for i in range(n - 1):

        is_sorted = True

        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                swap_count += 1
                is_sorted = False

        if is_sorted:
            break

    return swap_count


arr = [5, 4, 3, 2, 1]

print("Sorted Array :", end=" ")
print(*sorted(arr))

print("Total Swaps :", bubble_sort_swap_count(arr))
```

---

## Dry Run

Input

```text
5 4 3 2 1
```

Swaps

### Pass 1

```text
5↔4
5↔3
5↔2
5↔1
```

Swaps = 4

---

### Pass 2

```text
4↔3
4↔2
4↔1
```

Swaps = 3

---

### Pass 3

```text
3↔2
3↔1
```

Swaps = 2

---

### Pass 4

```text
2↔1
```

Swaps = 1

---

Total

```text
4+3+2+1 = 10
```

Which is

```text
5(5-1)/2

=10
```

---

## Time Complexity

| Case | Complexity |
|------|------------|
| Best | O(n) |
| Average | O(n²) |
| Worst | O(n²) |

---

## Space Complexity

```text
O(1)
```

---

## Key Points

- Reverse sorted array gives maximum swaps.
- Maximum swaps = n(n−1)/2.
- Optimized Bubble Sort can stop early if no swaps occur.
