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
print(datas)


# walk in this forest
len_data = len(datas)
find = False
loop_go = True
for index_changed in range(len_data):
    print('index_changed', index_changed)
    changes = None
    # print(f'Before change: datas[{index_changed}][0] =',          datas[index_changed][0], changes)
    if datas[index_changed][0] == 'acc':
        continue
    if datas[index_changed][0] == 'nop':
        changes = 'nop'
        datas[index_changed][0] = 'jmp'
    elif datas[index_changed][0] == 'jmp':
        changes = 'jmp'
        datas[index_changed][0] = 'nop'
    used_index = []
    index = 0
    accumulator = 0
    # print(f'Before loop: datas[{index_changed}][0] =',          datas[index_changed][0], changes)
    while loop_go:
        if index >= len_data:
            find = True
            print('Find accumulator', accumulator)
            print('index_changed', index_changed)
            break
        if datas[index][0] == 'nop':
            if index in used_index:
                print('Second circle acumulator')
                break
            used_index.append(index)
            index += 1
            continue
        if datas[index][0] == 'acc':
            if index in used_index:
                print('Second circle acumulator')
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
                print('Second circle acumulator')
                break
            used_index.append(index)
            if datas[index][1][:1] == '+':
                index += int(datas[index][1][1:])
            elif datas[index][1][:1] == '-':
                index -= int(datas[index][1][1:])
            continue
    if find:
        break
    # print(f'After loop: datas[{index_changed}][0] =',          datas[index_changed][0], changes)
    datas[index_changed][0] = changes
    # print(f'After change: datas[{index_changed}][0] =',          datas[index_changed][0], changes)

    print('accumulator', accumulator)

print('accumulator', accumulator)
# print('used_index', used_index)
