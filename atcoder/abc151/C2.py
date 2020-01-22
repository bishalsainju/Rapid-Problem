from collections import defaultdict

params = input().split()
n = int(params[0])
m = int(params[1])

penaltyCount = dict()
penaltyCount = defaultdict(lambda: 0, penaltyCount)

correct = 0
penalty = 0

for i in range(m):
    submission = input().split()
    p = int(submission[0]) - 1
    status = submission[1]

    if penaltyCount[p] == -1:
        continue
    if status == "WA":
        penaltyCount[p] += 1
    else:
        penalty += penaltyCount[p]
        penaltyCount[p] = -1
        correct += 1

print(str(correct) + " " + str(penalty))

