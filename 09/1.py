# get string from file
lines = []
with open('data.txt', 'r') as file:
    for line in file:
        if line[-1:] == '\n':
            lines.append(line[:-1])
        else:
            lines.append(line)
# print(lines)

# take data like integer list
data = []
for line in lines:
    data.append(int(line))
# print(data)

# from 26 position must be sum of two previous from last [0,26)
magic = 26  # 5
paired = []
find = False
not_paired = None
len_data = len(data)
for index in range(magic, len_data):
    if find:
        break
    find_pair = False
    for index2 in range(index-magic, index):
        if find_pair:
            break
        for index3 in range(index2+1, index):
            if data[index2] + data[index3] == data[index]:
                # print(data[index2], data[index3],
                #       data[index3]+data[index2], data[index])
                paired.append(data[index])
                find_pair = True
                break
    else:
        find = True
        not_paired = data[index]
        print('Not paired', not_paired)
print('not_paired', not_paired)
# print(paired)

# task2 find sets that is equal not_paired
find = False
for index in range(len_data):
    if find:
        break
    sets = [data[index]]
    suma = data[index]
    for index2 in range(index + 1, len_data):
        suma += data[index2]
        sets.append(data[index2])
        if suma < not_paired:
            continue
        if suma == not_paired:
            find = True
            print('Sets is', sets)
            print('result =', max(sets)+min(sets))
            break
        if suma > not_paired:
            break
