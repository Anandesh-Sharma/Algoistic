import math

# Comb Sort implementation in Python
"""
Improvement of Bubble sort.
In case of bubble sort the gap of 1 is maintained while checking two elements
Here a certain gap is maintained which is reduced per loop using a shrink factor
Generally shrink factor is always 1.3
"""


def swap(a, b):
    temp = un_sorted[a]
    un_sorted[a] = un_sorted[b]
    un_sorted[b] = temp


un_sorted = [0, 4, 2, 3, 5, 1, 3, 5, 6, 3, 5, 6, 2, 4, 6, 3, 5]
gap = un_sorted.__len__()
shrink_factor = 1.3
sorted = False
while not sorted:
    gap = math.floor(gap / shrink_factor)
    if gap <= 1:
        gap = 1
        sorted = True
    i = 0
    while i + gap < un_sorted.__len__():
        if un_sorted[i] > un_sorted[i + gap]:
            swap(i, i + gap)
            sorted = False
        i = i + 1
print(un_sorted)
