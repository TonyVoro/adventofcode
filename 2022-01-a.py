f = open('input.txt')
lines = f.readlines()

cal = 0
sums = []

for line in lines:
    line = line.strip()
    if line != '':
        cal = cal + int(line)
    else:
        sums.append(cal)
        cal = 0

sums.sort()
print(max(sums))
print('Part 2 :' (sum(sums[-3:])))
