# get numbers from file
lines = []
with open('data.txt', 'r') as f:  # adventofcode/
    for line in f:
        # print(line)
        lines.append(line)
# print(lines)
# take needed data
parted_bad = []
for item in lines:
    parted_bad.append(item.split())
# print(parted_bad)
parted = []
for i in parted_bad:
    limits = i[0].split('-')
    # print(limits)
    parted.append((int(limits[0]), int(limits[1]), i[1][:-1], i[2]))
# print(parted)
# choose right data
good_data = []
for i in parted:
    if i[0] <= i[3].count(i[2]) <= i[1]:
        good_data.append(i)
# print(good_data)
print(len(good_data))
