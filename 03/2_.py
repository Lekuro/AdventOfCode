# get string from file
lines = []
with open('data.txt', 'r') as file:
    for line in file:
        lines.append(line)
print(lines)
# build longer string
height = len(lines)
print(height)
width = len(lines[-1])
print(width)
multipler = (int(height/width)+1)*7

long_lines = []
len_lines = len(lines)
for index in range(len_lines):
    if index == len_lines-1:
        long_lines.append(lines[index]*multipler)
    else:
        long_lines.append((lines[index])[:-1]*multipler)

long_lines.append('0'*(width*multipler))
long_lines.append('0'*(width*multipler))
for line in long_lines:
    print(line)

# look for O and X
rules = [
    {'right': 1, 'down': 1},
    {'right': 3, 'down': 1},
    {'right': 5, 'down': 1},
    {'right': 7, 'down': 1},
    {'right': 1, 'down': 2},
]
counters = []
for rule in rules:
    right = rule['right']
    down = rule['down']
    counter = 0
    row = 0
    col = 0
    while row < height:
        row += down
        col += right
        if long_lines[row][col] == '#':
            # print(long_lines[row][col])
            counter += 1
    counters.append(counter)
print(counters)

product = 1
for item in counters:
    product *= item
print(product)
