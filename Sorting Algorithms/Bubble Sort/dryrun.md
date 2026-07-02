## Dry Run

### Input

```text
5
5 1 3 4 2
```

After taking input,

```python
arr = [5, 1, 3, 4, 2]
```

---

### Pass 1 (`i = 0`)

Current Array:

```text
[5, 1, 3, 4, 2]
```

| j | Comparison | Swap? | Array After |
|---|------------|-------|-------------|
| 0 | 5 > 1 | ✅ Yes | [1, 5, 3, 4, 2] |
| 1 | 5 > 3 | ✅ Yes | [1, 3, 5, 4, 2] |
| 2 | 5 > 4 | ✅ Yes | [1, 3, 4, 5, 2] |
| 3 | 5 > 2 | ✅ Yes | [1, 3, 4, 2, 5] |

Largest element (**5**) reaches the last position.

---

### Pass 2 (`i = 1`)

Current Array:

```text
[1, 3, 4, 2, 5]
```

| j | Comparison | Swap? | Array After |
|---|------------|-------|-------------|
| 0 | 1 > 3 | ❌ No | [1, 3, 4, 2, 5] |
| 1 | 3 > 4 | ❌ No | [1, 3, 4, 2, 5] |
| 2 | 4 > 2 | ✅ Yes | [1, 3, 2, 4, 5] |

Now **4** reaches its correct position.

---

### Pass 3 (`i = 2`)

Current Array:

```text
[1, 3, 2, 4, 5]
```

| j | Comparison | Swap? | Array After |
|---|------------|-------|-------------|
| 0 | 1 > 3 | ❌ No | [1, 3, 2, 4, 5] |
| 1 | 3 > 2 | ✅ Yes | [1, 2, 3, 4, 5] |

Now **3** reaches its correct position.

---

### Pass 4 (`i = 3`)

Current Array:

```text
[1, 2, 3, 4, 5]
```

| j | Comparison | Swap? | Array After |
|---|------------|-------|-------------|
| 0 | 1 > 2 | ❌ No | [1, 2, 3, 4, 5] |

No swaps are needed.

---

## Final Output

```text
1 2 3 4 5
```

---

## Number of Comparisons

| Pass | Comparisons |
|------|------------:|
| Pass 1 | 4 |
| Pass 2 | 3 |
| Pass 3 | 2 |
| Pass 4 | 1 |

Total Comparisons:

```text
4 + 3 + 2 + 1 = 10
```

This is why the inner loop is written as:

```python
for j in range(n - i - 1):
```

After every pass, the largest unsorted element is already at its correct position, so there is no need to compare it again.