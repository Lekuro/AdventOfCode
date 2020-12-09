import re  # 186
# get numbers from file
lines = []
with open('data.txt', 'r') as f:  # adventofcode/
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
# sort data
for i in parted:
    i.sort()
# print(parted)
# choose right data
task1_data = []
for i in parted:
    if len(i) == 8:
        task1_data.append(i)
    elif len(i) == 7:
        for j in i:
            if j[0] == 'cid':
                break
        else:
            task1_data.append(i)
print(task1_data)
print(len(task1_data))
# task2
valid_passport = []
for i in task1_data:
    if len(i) == 8:
        if int(i[0][1]) < 1920 or int(i[0][1]) > 2002:
            continue
        # if i[2][1] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        #     continue
        if int(i[3][1]) < 2020 or int(i[3][1]) > 2030:
            continue
        if i[5][1][-2:] == 'cm' and (int(i[5][1][:-2]) < 150 or int(i[5][1][:-2]) > 193):
            continue
        if i[5][1][-2:] == 'in' and (int(i[5][1][:-2]) < 59 or int(i[5][1][:-2]) > 76):
            continue
        if int(i[6][1]) < 2010 or int(i[6][1]) > 2020:
            continue
        if re.findall("^0[0-9]{8}", i[7][1]) and re.findall("^#[0-9a-f]{6}", i[4][1]) and i[2][1] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            print(re.findall("^0[0-9]{8}", i[7][1]),
                  re.findall("^#[0-9a-f]{6}", i[4][1]))
            valid_passport.append(i)
    if len(i) == 7:
        if int(i[0][1]) < 1920 or int(i[0][1]) > 2002:
            continue
        # if i[1][1] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        #     continue      # amb blu brn gry grn hzl oth
        if int(i[2][1]) < 2020 or int(i[2][1]) > 2030:
            continue
        if i[4][1][-2:] == 'cm' and (int(i[4][1][:-2]) < 150 or int(i[4][1][:-2]) > 193):
            continue
        if i[4][1][-2:] == 'in' and (int(i[4][1][:-2]) < 59 or int(i[4][1][:-2]) > 76):
            continue
        if int(i[5][1]) < 2010 or int(i[5][1]) > 2020:
            continue
        if re.findall("^0[0-9]{8}", i[6][1]) and re.findall("^#[0-9a-f]{6}", i[3][1]) and i[1][1] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            # print(re.findall("^0[0-9]{8}", i[6][1]), re.findall("^#[0-9a-f]{6}", i[3][1]))
            valid_passport.append(i)

# print(valid_passport)
for line in valid_passport:
    print(line)
print(len(valid_passport))
