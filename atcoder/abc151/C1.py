from collections import defaultdict

lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

correct = 0
penalty = 0
d = dict()
d = defaultdict(lambda: 0, d)

for line in lines[1:]:
    n = line.split()[0]
    m = line.split()[1]

    if d[n] == -1:
        continue
    if m == "WA":
        d[n] += 1
    else:
        penalty += d[n]
        d[n] = -1
        correct += 1

print(str(correct) + " " + str(penalty))

