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

# Problem 2 - Sort String Based on Marks After Removing Marks Less Than X

## Problem Statement

You are given a string where every **name** is followed by its corresponding **marks**.

Example:

```text
"Ravi 78 Bob 99 Sunny 88 Alice 86"
```

Also given an integer `X`.

Your task is to:

1. Remove every `(name, marks)` pair whose marks are less than `X`.
2. Sort the remaining pairs in **decreasing order of marks**.
3. If two students have the same marks, sort them alphabetically by name.
4. Return the final string.

---

## Example

### Input

```text
String = "Ravi 78 Bob 99 Sunny 88 Alice 86"

X = 79
```

---

## Step 1 - Convert String into List

```python
[
"Ravi", "78",
"Bob", "99",
"Sunny", "88",
"Alice", "86"
]
```

Notice the pattern:

| Index | Value | Meaning |
|-------:|------|---------|
| 0 | Ravi | Name |
| 1 | 78 | Marks |
| 2 | Bob | Name |
| 3 | 99 | Marks |
| 4 | Sunny | Name |
| 5 | 88 | Marks |
| 6 | Alice | Name |
| 7 | 86 | Marks |

Even indices store **names**.

Odd indices store **marks**.

---

## Step 2 - Remove Marks Less Than X

Since

```text
78 < 79
```

Remove

```text
Ravi 78
```

Now the list becomes

```python
[
"Bob","99",
"Sunny","88",
"Alice","86"
]
```

---

## Step 3 - Sort Remaining Pairs

Compare marks only.

```text
99
88
86
```

Already sorted.

Final Output

```text
Bob 99 Sunny 88 Alice 86
```

---

## Another Example

Input

```text
"Aman 90 Bob 95 Charlie 90"

X = 80
```

Remaining pairs

```text
Aman 90
Bob 95
Charlie 90
```

Sort by marks

```text
Bob 95
Aman 90
Charlie 90
```

Aman and Charlie have the same marks.

So compare names alphabetically.

```text
Aman
Charlie
```

---

## Algorithm

1. Convert the string into a list.
2. Remove all pairs having marks less than `X`.
3. Bubble Sort the remaining pairs.
4. Compare marks.
5. If marks are equal, compare names.
6. Join the list back into a string.

---

## Code

```python
def bubble_string_sort(s, x):

    # Convert string into list
    my_list = s.split()

    n = len(my_list)

    # Remove pairs whose marks are less than X
    for i in range(n - 1, 0, -2):
        if int(my_list[i]) < x:
            del my_list[i - 1:i + 1]

    n = len(my_list)

    # Bubble Sort
    for i in range(1, n, 2):
        for j in range(1, n - i, 2):

            marks1 = int(my_list[j])
            marks2 = int(my_list[j + 2])

            if (marks1 < marks2) or (
                marks1 == marks2 and
                my_list[j - 1] > my_list[j + 1]
            ):

                # Swap marks
                my_list[j], my_list[j + 2] = my_list[j + 2], my_list[j]

                # Swap names
                my_list[j - 1], my_list[j + 1] = (
                    my_list[j + 1],
                    my_list[j - 1]
                )

    return " ".join(my_list)


string = "Ravi 78 Bob 99 Sunny 88 Alice 86"

print(bubble_string_sort(string, 79))
```

---

## Time Complexity

Removing pairs

```text
O(n)
```

Bubble Sort

```text
O(n²)
```

Overall

```text
O(n²)
```

---

## Space Complexity

```text
O(n)
```

The string is first converted into a list.

---

## Key Points

- Process the list in pairs.
- Compare marks, not names.
- Swap both name and marks together.
- If marks are equal, compare names alphabetically.



# Problem 3 - Push All Zeroes to the End While Maintaining Relative Order

## Problem Statement

Given an array, move all the zeroes to the end while maintaining the **relative order** of all non-zero elements.

---

## Example

### Input

```python
[1, 2, 0, 4, 3, 0, 5, 0]
```

### Output

```python
[1, 2, 4, 3, 5, 0, 0, 0]
```

Notice that

```text
1 2 4 3 5
```

remain in exactly the same order.

Only the zeroes are moved.

---

## Dry Run

Initial Array

```text
[1,2,0,4,3,0,5,0]
```

Create a temporary array

```text
[0,0,0,0,0,0,0,0]
```

Copy non-zero elements

```text
1
```

```text
[1,0,0,0,0,0,0,0]
```

Copy

```text
2
```

```text
[1,2,0,0,0,0,0,0]
```

Skip

```text
0
```

Copy

```text
4
```

```text
[1,2,4,0,0,0,0,0]
```

Copy

```text
3
```

```text
[1,2,4,3,0,0,0,0]
```

Skip

```text
0
```

Copy

```text
5
```

```text
[1,2,4,3,5,0,0,0]
```

The remaining positions already contain zero.

Copy the temporary array back into the original array.

Final Output

```text
[1,2,4,3,5,0,0,0]
```

---

## Algorithm

1. Create another array of the same size.
2. Copy every non-zero element into it.
3. Fill the remaining positions with zero.
4. Copy the temporary array back to the original array.

---

## Code

```python
def push_zero_end(arr):

    n = len(arr)

    temp = [0] * n

    count = 0

    for i in range(n):

        if arr[i] != 0:
            temp[count] = arr[i]
            count += 1

    while count < n:
        temp[count] = 0
        count += 1

    for i in range(n):
        arr[i] = temp[i]


arr = [1, 2, 0, 4, 3, 0, 5, 0]

push_zero_end(arr)

print(arr)
```

---

## Time Complexity

Traversing the array

```text
O(n)
```

Copying back

```text
O(n)
```

Overall

```text
O(n)
```

---

## Space Complexity

```text
O(n)
```

An extra temporary array is used.

---

## Key Points

- Preserve the order of non-zero elements.
- Only move zeroes.
- Linear time solution.
- Uses an auxiliary array.
- Can also be solved using the Two Pointer Technique with **O(1)** extra space.