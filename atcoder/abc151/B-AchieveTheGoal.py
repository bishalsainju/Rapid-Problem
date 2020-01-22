no_of_lines = 2
lines = ""
for i in range(no_of_lines):
    lines+=input()+"\n"

lines = lines.splitlines()
first = lines[0].split()
second = lines[1].split()

N = int(first[0])
K = int(first[1])
M = int(first[2])

nums = [int(i) for i in second]

min = M * N - sum(nums)
if(min <= K) :
    if(min <= 0):
        print(0)
    else:
        print(min)
else:
    print(-1)
