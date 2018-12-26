# Selection Sort implementation in Python
"""
ALGORITHM
Step 1: Traverse the array keep track of it (i.e un_sorted[j])
Step 2: Store the current element as key and declare i = j
Step 3: Traverse back using i and compare elements larger than key if yes then swap
"""
un_sorted = [0, 4, 2, 3, 5, 1, 3, 5, 6, 3, 5, 6, 2, 4, 6, 3, 5]

for j in range(1, un_sorted.__len__()):
    key = un_sorted[j]
    i = j
    # Back Traversing and comparing
    while i >= 0 and un_sorted[i - 1] > key:
        un_sorted[i] = un_sorted[i - 1]
        un_sorted[i - 1] = key
        i = i - 1

print(un_sorted)
