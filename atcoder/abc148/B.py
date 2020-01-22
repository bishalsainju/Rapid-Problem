no_of_lines = 2
lines = ""
for i in range(no_of_lines):
    lines+=input()+"\n"

lines = lines.splitlines()
n = int(lines[0])
str = lines[1].split()
s = str[0]
t = str[1]

new_str = ""
for i in range(n):
    new_str += s[i] + t[i]

print(new_str)