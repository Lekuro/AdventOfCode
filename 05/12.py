# get string from file
lines = []
with open('05/data.txt', 'r') as file:
    for line in file:
        if line[-1:] == '\n':
            lines.append(line[:-1])
        else:
            lines.append(line)
# print(lines)

ids = []
for line in lines:
    # take a row
    tree = [[0, 63], [64, 127]]
    # print(tree)
    # print(line)
    row = 0
    for i in line[:6]:
        if i == 'F':
            tree = tree[0]
            t0, t1 = tree
            # print(i)
            tree[0] = [int(tree[0]), int(t0+(t1-t0+1)/2-1)]
            tree[1] = [int(t0+(t1-t0+1)/2), int(tree[1])]
            # print(tree)
        elif i == 'B':
            tree = tree[1]
            t0, t1 = tree
            # print(i)
            tree[0] = [int(tree[0]), int(t0+(t1-t0+1)/2-1)]
            tree[1] = [int(t0+(t1-t0+1)/2), int(tree[1])]
            # print(tree)
    for i in line[6:7]:
        if i == 'F':
            tree = tree[0]
            t0, t1 = tree
            # print(i)
            # print(tree)
            row = t0
        elif i == 'B':
            tree = tree[1]
            t0, t1 = tree
            # print(i)
            # print(tree)
            row = t1
    # print(row)

    # take a col
    tree = [[0, 3], [4, 7]]
    # print(tree)
    # print(line)
    col = 0
    for i in line[7:9]:
        if i == 'L':
            tree = tree[0]
            t0, t1 = tree
            # print(i)
            tree[0] = [int(tree[0]), int(t0+(t1-t0+1)/2-1)]
            tree[1] = [int(t0+(t1-t0+1)/2), int(tree[1])]
            # print(tree)
        elif i == 'R':
            tree = tree[1]
            t0, t1 = tree
            # print(i)
            tree[0] = [int(tree[0]), int(t0+(t1-t0+1)/2-1)]
            tree[1] = [int(t0+(t1-t0+1)/2), int(tree[1])]
            # print(tree)
    for i in line[-1]:
        if i == 'L':
            tree = tree[0]
            t0, t1 = tree
            # print(i)
            # print(tree)
            col = t0
        elif i == 'R':
            tree = tree[1]
            t0, t1 = tree
            # print(i)
            # print(tree)
            col = t1
    # print(col)
    id_ = row * 8 + col
    # print(id_)
    ids.append(id_)
print(ids)
print(max(ids))

# task2
print(sorted(ids))
ids_sorted = sorted(ids)
print(len(ids))
print(min(ids))
mini = min(ids)
for place in ids_sorted:
    #print(mini, place)
    if mini == place:
        mini += 1
    else:
        print('place', place, 'mini!!! There is no', mini)
        mini = place + 1
