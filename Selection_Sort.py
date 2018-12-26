# Selection Sort implementation in Python

un_sorted = [0, 4, 2, 3, 5, 1, 3, 5, 6, 3, 5, 6, 2, 4, 6, 3, 5]

for i in range(0, un_sorted.__len__()):
    for j in range(i + 1, un_sorted.__len__()):
        if un_sorted[j] < un_sorted[i]:
            temp = un_sorted[j]
            un_sorted[j] = un_sorted[i]
            un_sorted[i] = temp

print(un_sorted)
