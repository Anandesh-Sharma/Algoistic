# Cocktail Shaker Sort implementation in Python
"""
TIP : Just like bubble but it works backwards also
Its a variant of bubble sort
"""


def swap(a, b):
    temp = un_sorted[a]
    un_sorted[a] = un_sorted[b]
    un_sorted[b] = temp


un_sorted = [0, 4, 2, 3, 5, 1, 3, 5, 6, 3, 5, 6, 2, 4, 6, 3, 5]

for i in range(0, int(un_sorted.__len__() / 2)):
    for j in range(0, un_sorted.__len__() - i - 1):
        if un_sorted[j + 1] < un_sorted[j]:
            swap(j + 1, j)

    for k in range(un_sorted.__len__() - 2, i, -1):
        if un_sorted[k] < un_sorted[k - 1]:
            swap(k, k - 1)

print(un_sorted)
