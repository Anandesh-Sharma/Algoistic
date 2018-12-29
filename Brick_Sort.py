# Brick Sort implementation in Python also called odd-even sort
"""
ALGORITHM:
Source: https://en.wikipedia.org/wiki/Odd%E2%80%93even_sort
Compare all odd/even indexed pairs of adjacent elements in the list and,
if a pair is in the wrong order (the first is larger than the second) the elements are switched.
The next step repeats this for even/odd indexed pairs (of adjacent elements).
Then it alternates between odd/even and even/odd steps until the list is sorted.
"""


def swap(a, b):
    temp = un_sorted[a]
    un_sorted[a] = un_sorted[b]
    un_sorted[b] = temp


un_sorted = [0, 4, 2, 3, 5, 1, 3, 5, 6, 3, 5, 6, 2, 4, 6, 3, 5]
sorted = False
while not sorted:
    sorted = True
    # Even pair checks
    for i in range(0, un_sorted.__len__() - 1, 2):
        if un_sorted[i] > un_sorted[i + 1]:
            swap(i, i + 1)
            sorted = False
    # Odd pair checks
    for i in range(1, un_sorted.__len__() - 1, 2):
        if un_sorted[i] > un_sorted[i + 1]:
            swap(i, i + 1)
            sorted = False

print(un_sorted)
