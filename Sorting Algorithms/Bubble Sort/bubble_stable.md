# Stable and Unstable Sorting

## What is Stability in Sorting?

A sorting algorithm is called **stable** if it **preserves the relative order of equal elements** after sorting.

To understand this, imagine two elements have the same value. Since they look identical, we label one of them to track its position.

Example:

```text
Original Array:
2  6  4  1  2'
```

Here,

- `2` = First occurrence
- `2'` = Second occurrence

Both have the same value (`2`), but we use `2'` only to identify the second one.

---

## Stable Sort

After sorting:

```text
1  2  2'  4  6
```

Notice that:

- `2` was before `2'` originally.
- `2` is still before `2'` after sorting.

The original order of equal elements is preserved.

**This is called a Stable Sort.**

---

## Unstable Sort

After sorting:

```text
1  2'  2  4  6
```

Now,

- `2'` comes before `2`.
- Their order has changed.

The relative order of equal elements is **not preserved**.

**This is called an Unstable Sort.**

---

# Bubble Sort Example

Bubble Sort compares **adjacent elements**.

It swaps them **only when the left element is greater than the right element**.

### Bubble Sort Code

```python
arr = [2, 6, 4, 1, 2]

n = len(arr)

for i in range(n - 1):
    for j in range(n - i - 1):

        # Swap only if left > right
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)
```

### Output

```text
[1, 2, 2, 4, 6]
```

---

# Why is Bubble Sort Stable?

Bubble Sort swaps elements only when:

```python
if arr[j] > arr[j + 1]:
```

Notice it uses **`>`**, not **`>=`**.

Suppose we have:

```text
2  6  4  1  2'
```

During sorting,

Eventually we compare:

```text
2   2'
```

Since

```text
2 > 2
```

is **False**, Bubble Sort **does not swap them**.

So the order remains:

```text
2  2'
```

After complete sorting:

```text
1  2  2'  4  6
```

The first `2` is still before the second `2'`.

Therefore, **Bubble Sort is Stable.**

---

# What if Bubble Sort used `>=`?

Suppose the condition was:

```python
if arr[j] >= arr[j + 1]:
```

Now, when comparing

```text
2   2'
```

Since

```text
2 >= 2
```

is **True**, they would be swapped.

Result:

```text
1  2'  2  4  6
```

The order of equal elements changed.

The algorithm would become **Unstable**.

---

# Key Point

Bubble Sort swaps **only when**

```text
Left Element > Right Element
```

It **never swaps equal elements**.

Because equal elements never change their relative order, **Bubble Sort is a Stable Sorting Algorithm.**

---

# Quick Summary

| Stable Sort | Unstable Sort |
|--------------|----------------|
| Preserves the order of equal elements | May change the order of equal elements |
| Example: `1 2 2' 4 6` | Example: `1 2' 2 4 6` |
| Bubble Sort is Stable | Selection Sort and Heap Sort are Unstable |