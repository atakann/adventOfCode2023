with open('text1.txt') as f:
    lines = [line.rstrip() for line in f]

val = 0

for line in lines:
    i = 0
    inval = ""
    while i < len(line):
        if line[i].isnumeric():
            inval += line[i]
        i += 1
    if len(inval) > 2:
        inval = inval[0] + inval[-1]
    elif len(inval) == 1:
        inval = inval[0] * 2
    val += int(inval)

print(val) 