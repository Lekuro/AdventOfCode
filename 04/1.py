# get numbers from file
lines = []
with open('data.txt', 'r') as f:  # 04/
    for line in f:
        # print(line)
        lines.append(line)
# print(lines)
# take needed data
parted_bad = []
part = ''
for item in lines:
    if item == '\n':
        parted_bad.append(part)
        part = ''
    else:
        part += item + ' '
# print(parted_bad)
parted = []
parted_on_str = []
for i in parted_bad:
    parted_on_str.append(i.split())
    line = i.split()
    line_splite = []
    for j in line:
        line_splite.append(j.split(':'))
    parted.append(line_splite)
# print(parted)
# print(parted_on_str)
# choose right data
good_data = []
for i in parted:
    if len(i) == 8:
        good_data.append(i)
    elif len(i) == 7:
        for j in i:
            if j[0] == 'cid':
                break
        else:
            good_data.append(i)
# print(good_data)
print(len(good_data))
