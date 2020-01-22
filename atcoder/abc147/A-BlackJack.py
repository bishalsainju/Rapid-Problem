num = input().split()

sum = int(num[0]) + int(num[1]) + int(num[2])
if sum >= 22:
    print("bust")
else:
    print("win")