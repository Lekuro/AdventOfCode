# get string from file
lines = []
with open('data.txt', 'r') as file:
    for line in file:
        if line[-1:] == '\n':
            lines.append(line[:-1])
        else:
            lines.append(line)
# print(lines)

# take data like nested list
datas = []
for line in lines:
    datas.append(line.split())
# print(datas)


# walk in this forest

used_index = []
loop_go = True
index = 0
accumulator = 0
while loop_go:
    # for i in range(10):
    if datas[index][0] == 'nop':
        if index in used_index:
            break
        used_index.append(index)
        index += 1
        continue
    if datas[index][0] == 'acc':
        if index in used_index:
            break
        used_index.append(index)
        if datas[index][1][:1] == '+':
            accumulator += int(datas[index][1][1:])
        elif datas[index][1][:1] == '-':
            accumulator -= int(datas[index][1][1:])
        index += 1
        continue
    if datas[index][0] == 'jmp':
        if index in used_index:
            break
        used_index.append(index)
        if datas[index][1][:1] == '+':
            index += int(datas[index][1][1:])
        elif datas[index][1][:1] == '-':
            index -= int(datas[index][1][1:])
        continue

print('accumulator', accumulator)
print('used_index', used_index)
