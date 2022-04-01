a = [1, 4, 10, 11]
b = [2, 3, 3, 4, 8]

i = 0
j = 0

N = len(a)
M = len(b)

sort_mas = []

while i < N  and j < M:
    if a[i] < b[j]:
        sort_mas.append(a[i])
        i += 1
    else:
        sort_mas.append(b[j])
        j += 1


sort_mas += a[i:] + b[j:]

print(sort_mas)
