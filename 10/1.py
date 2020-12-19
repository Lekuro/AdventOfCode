# get string from file
lines = []
with open('data.txt', 'r') as file:
    for line in file:
        if line[-1:] == '\n':
            lines.append(int(line[:-1]))
        else:
            lines.append(int(line))
print(lines)

num_sorted = sorted(lines)
print(num_sorted)

# choose number that have diference == 3
count_dif_3 = 1
for index in range(len(num_sorted)-1):
    if num_sorted[index + 1] - num_sorted[index] == 3:
        count_dif_3 += 1
print(count_dif_3)

# choose number that have diference == 1
count_dif_1 = 1
for index in range(len(num_sorted)-1):
    if num_sorted[index + 1] - num_sorted[index] == 1:
        count_dif_1 += 1
print(count_dif_1)
print('product', count_dif_1 * count_dif_3)
