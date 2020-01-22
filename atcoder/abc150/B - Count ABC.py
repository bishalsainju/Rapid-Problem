no_of_lines = 2
lines = ""
for i in range(no_of_lines):
    lines+=input()+"\n"

lines = lines.splitlines()

N = int(lines[0])
S = lines[1]

c = 0
for i in range(N-2):
    if(S[i:i+3] == "ABC"):
        c+=1

print(c)
