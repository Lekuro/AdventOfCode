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
multipler = (int(height/width)+1)*3

long_lines = []
len_lines = len(lines)
for index in range(len_lines):
    if index == len_lines-1:
        long_lines.append(lines[index]*multipler)
    else:
        long_lines.append((lines[index])[:-1]*multipler)

long_lines.append('0'*(width*multipler))
for line in long_lines:
    print(line)

# look for O and X
right = 3
down = 1
counter = 0
row = 0
col = 0
while row < height:
    row += down
    col += right
    if long_lines[row][col] == '#':
        # print(long_lines[row][col])
        counter += 1

print(counter)
