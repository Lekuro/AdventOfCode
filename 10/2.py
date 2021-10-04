# get string from file
lines = []
with open('data.txt', 'r') as file:
    for line in file:
        if line[-1:] == '\n':
            lines.append(int(line[:-1]))
        else:
            lines.append(int(line))
print(lines)

# adds start
lines.append(0)
num_sorted = sorted(lines)
# adds end
num_sorted.append(num_sorted[-1] + 3)
print(num_sorted)

# choose parts with number that have difference == 1
len_parts_dif_1 = []
len_num = len(num_sorted)
index2 = 0
while index2 < len_num - 1:
    if num_sorted[index2 + 1] - num_sorted[index2] == 1:
        count_dif_1 = 1
        for index in range(index2, len_num - 1):
            if num_sorted[index + 1] - num_sorted[index] == 1:
                count_dif_1 += 1
            else:
                index2 = index
                len_parts_dif_1.append(count_dif_1)
                break
    index2 += 1
print('len_parts_dif_1', len_parts_dif_1)

# choose number that have diference == 2
count_dif_2 = 0
for index in range(len(num_sorted)-1):
    if num_sorted[index + 1] - num_sorted[index] == 2:
        count_dif_2 += 1
print('count_dif_2', count_dif_2)

# calculate amount the distinct sets
magic_dict = {2: 1, 3: 2, 4: 4, 5: 7, 6: 11}
product = 1
for item in len_parts_dif_1:
    product *= magic_dict[item]
print('distinct sets', product)
