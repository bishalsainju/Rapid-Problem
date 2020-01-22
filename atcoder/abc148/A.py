no_of_lines = 2
lines = ""
for i in range(no_of_lines):
    lines+=input()+"\n"

lines = lines.splitlines()
a = int(lines[0])
b = int(lines[1])

print(6-a-b)