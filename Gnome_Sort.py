# Gnome Sort implementation in Python
"""
ALGORITHM:
Step 1: Start from the current position i.e. cp = 1
Step 2: Loop through the array and check if the previous element is smaller than
        current element if yes then increment the position
Step 3: Else swap the element and decrement the cp
"""


def swap(a, b):
    temp = un_sorted[a]
    un_sorted[a] = un_sorted[b]
    un_sorted[b] = temp


un_sorted = [0, 4, 2, 3, 5, 1, 3, 5, 6, 3, 5, 6, 2, 4, 6, 3, 5]

cp = 1
while cp < un_sorted.__len__():
    if un_sorted[cp - 1] <= un_sorted[cp]:
        cp = cp + 1
    else:
        swap(cp, cp - 1)
        cp = cp - 1
print(un_sorted)
