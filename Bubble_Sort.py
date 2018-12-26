# Bubble Sort implementation in Python
"""
ALGORITHM
Step 1: Traverse the array 1st time.
Step 2: Traverse the array 2nd time and check if the current element i.e.(un_sorted[j]) is
        less than previous one i.e. (un_sorted[j-1])if yes then swap.
"""
un_sorted = [0, 4, 2, 3, 5, 1, 3, 5, 6, 3, 5, 6, 2, 4, 6, 3, 5]

for i in range(0, un_sorted.__len__()):
    for j in range(1, un_sorted.__len__() - i):
        if un_sorted[j] < un_sorted[j - 1]:
            temp = un_sorted[j]
            un_sorted[j] = un_sorted[j - 1]
            un_sorted[j - 1] = temp

print(un_sorted)
