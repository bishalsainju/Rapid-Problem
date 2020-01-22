# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
# import numpy
# import scipy

def jump_fwd(aList):
    n = len(aList)
    newList = aList.copy()
    newList.append(aList[-1])
    newList[0] = -1
    newList[1:n] = aList[0:n-1]
    del aList
    return newList


n = get_number()
p = get_number()
t = get_number()

# print(jump_fwd([0, 0, 1, 2, 3]))
aList = []
for i in range(n):
    aList.append(i+1)


k = int(t/9)
m = t % 9

for i in range(k):
    for j in range(3):
        aList = jump_fwd(aList)


if m == 5:
    aList = jump_fwd(aList)
elif m == 7:
    aList = jump_fwd(aList)
elif m == 8:
    for i in range(2):
        aList = jump_fwd(aList)


if p > len(aList):
    print(-1)
else:
    print(aList[p-1])
