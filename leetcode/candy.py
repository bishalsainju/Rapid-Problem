# N = 57
# # b = [1, 3, 7, 10]
# b = "56 46 20 3 17".split(" ")
# b = [int(i) for i in b]

b = [16, 17, 5]
N = 24

a = []
for i in range(N+1):
    a.append(-1)
a[0] = 0

for i in b:
    for j in range(1, N+1):
        if(j-i >= 0 and a[j-i] != -1):
            if(a[j] == -1):
                a[j] = a[j-i] + 1
            else:
                a[j] = min(a[j-i] + 1, a[j])
print(a[N])
