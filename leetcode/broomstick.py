# a = [2, 4, 13, 5, 9]
# a = [52, 64, 78, 28]
# a = [1, 4, 13, 15]
a = [4, 3, 2, 1]



prev = next = a[0]
print(prev)
for i in range(1, len(a)):
    if (i%2 != 0):
        med = max(a[i], prev, next)
    else:
        med = min(a[i], prev)
        next = max(a[i], prev)
    print(prev, med, next)
    # print(med)
    prev = med
